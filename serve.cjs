const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

const DIST = path.resolve(__dirname, 'dist');
const PORT = parseInt(process.env.PORT || '8090', 10);

// ---------- 访问计数（2026-10-02 上线）----------
// 口径：每次页面请求 +1，不去重、不识别爬虫、不排除任何来源。
// 刷新一次算一次，这是页面浏览量（PV）的通行算法。
// 与 Cloudflare Web Analytics 并存：CF 给你「独立访客」视角，这里给你「总浏览量」和购买漏斗。
const STATS_DIR = path.join(__dirname, 'stats');
const STATS_FILE = path.join(STATS_DIR, 'views.json');
const STATS_SEED = 2300;               // 起始基数：近 30 天真实 PV（Cloudflare 统计 2.3k）

// 记录购买链接点击，这是 CF 看不到的漏斗环节
const FUNNEL_KEYS = ['mbd.pub', 'aliyun.com', 'my.racknerd.com'];

const stats = {
  total: STATS_SEED,
  byPath: {},
  byDay: {},
  referrers: {},
  funnel: { view99: 0, clickBuy: 0 },
};

function loadStats() {
  try {
    const raw = JSON.parse(fs.readFileSync(STATS_FILE, 'utf8'));
    Object.assign(stats, {
      total: Number(raw.total) || STATS_SEED,
      byPath: raw.byPath || {},
      byDay: raw.byDay || {},
      referrers: raw.referrers || {},
      funnel: { view99: Number(raw.funnel && raw.funnel.view99) || 0,
                clickBuy: Number(raw.funnel && raw.funnel.clickBuy) || 0 },
    });
  } catch (e) {
    console.log('[stats] seed start, total =', STATS_SEED);
  }
}
loadStats();

let statsDirty = false;
function saveStats() {
  if (!statsDirty) return;
  statsDirty = false;
  try {
    fs.mkdirSync(STATS_DIR, { recursive: true });
    fs.writeFileSync(STATS_FILE, JSON.stringify(stats), 'utf8');
  } catch (e) {
    console.error('[stats] save failed:', e.message);
  }
}
setInterval(saveStats, 5000).unref();
process.on('exit', saveStats);
process.on('SIGINT', () => { saveStats(); process.exit(0); });
process.on('SIGTERM', () => { saveStats(); process.exit(0); });

function bjDay(d) {
  return new Date(d.getTime() + 8 * 3600 * 1000).toISOString().slice(0, 10);
}

function countView(url, ref) {
  const day = bjDay(new Date());
  stats.total += 1;
  statsDirty = true;
  stats.byDay[day] = (stats.byDay[day] || 0) + 1;
  // 只统计页面请求，不统计图片/样式/视频等静态资源
  if (!/\.[a-z0-9]{2,5}$/i.test(url)) {
    stats.byPath[url] = (stats.byPath[url] || 0) + 1;
  }
  if (ref) {
    let host = 'direct';
    try { host = new URL(ref).hostname; } catch (e) { host = ref.slice(0, 60); }
    stats.referrers[host] = (stats.referrers[host] || 0) + 1;
  }
  if (url.indexOf('zaihouse-template-99') >= 0) {
    stats.funnel.view99 += 1;
  }
}

// ---------- 载入 zaikafei 的 TG 凭据（不改动 zaikafei 任何文件）----------
const ZAIKAFEI_ENV = '/home/ubuntu/zaikafei-site/server.env';
function loadEnv(file) {
  const out = {};
  try {
    for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
      const m = line.match(/^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.*)\s*$/);
      if (!m) continue;
      let v = m[2].trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      out[m[1]] = v;
    }
  } catch (e) {
    console.error('[blog] load env failed:', e.message);
  }
  return out;
}
const ENV = loadEnv(ZAIKAFEI_ENV);
const TG_BOT_TOKEN = ENV.CSZAIHOUSE_BOT_TOKEN || ENV.TG_BOT_TOKEN || '';
const TG_CHAT_ID = ENV.TG_CHAT_ID || '';
const TG_PROXY = ENV.TG_PROXY || '';

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.mp4': 'video/mp4',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
};

// 2026-10-03: 改异步。之前用 statSync，单线程 Node 里同步 IO 会卡住事件循环，
// 一个慢请求就能让整个源站不响应 → Cloudflare 隧道转发超时 → 公网 1033。
async function tryFile(p) {
  try {
    const st = await fs.promises.stat(p);
    if (st.isFile()) return p;
  } catch {}
  return null;
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
function isValidEmail(e) {
  return typeof e === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e.trim()) && e.length <= 190;
}

// ---------- Telegram 通知 ----------
function tgSend(text) {
  return new Promise(resolve => {
    if (!TG_BOT_TOKEN || !TG_CHAT_ID) return resolve({ ok: false, skipped: 'no token/chat' });
    const body = JSON.stringify({ chat_id: TG_CHAT_ID, text, parse_mode: 'HTML' });
    const urlStr = 'https://api.telegram.org/bot' + TG_BOT_TOKEN + '/sendMessage';
    const args = ['-sS', '-m', '20', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', body];
    if (TG_PROXY) args.push('-x', TG_PROXY);
    args.push(urlStr);
    execFile('curl', args, { timeout: 25000 }, (err, stdout) => {
      if (err) return resolve({ ok: false, error: String(err.message).slice(0, 200) });
      try { resolve(JSON.parse(stdout)); } catch (e) { resolve({ ok: false, error: 'bad json' }); }
    });
  });
}

// 限流已按需求取消（2026-09-29）：买家从第 1 步到付款可能只有几秒，
// 任何阻止都会直接导致漏单。防刷改由 Cloudflare 侧承担。
function json(res, code, obj) {
  const b = Buffer.from(JSON.stringify(obj), 'utf8');
  res.writeHead(code, { 'content-type': 'application/json; charset=utf-8', 'content-length': b.length, 'access-control-allow-origin': '*' });
  res.end(b);
}

function readBody(req, limit = 8 * 1024) {
  return new Promise((resolve, reject) => {
    let n = 0; const chunks = [];
    req.on('data', c => {
      n += c.length;
      if (n > limit) { reject(new Error('payload too large')); req.destroy(); return; }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

const server = http.createServer((req, res) => { handle(req, res).catch(e => {
  console.error('[blog] handler error:', e && e.message);
  if (!res.headersSent) { res.statusCode = 500; }
  try { res.end(); } catch {}
}); });

async function handle(req, res) {
  const url = req.url.split('?')[0];

  // ---------- CORS 预检 ----------
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'access-control-allow-origin': '*',
      'access-control-allow-methods': 'POST, OPTIONS',
      'access-control-allow-headers': 'content-type',
    });
    return res.end();
  }

  // ---------- 订单通知接口 ----------
  if (url === '/api/order' && req.method === 'POST') {
    const ip = (req.headers['x-forwarded-for'] || '').split(',')[0].trim() || req.socket.remoteAddress || 'unknown';

    readBody(req).then(raw => {
      let d;
      try { d = JSON.parse(raw || '{}'); } catch { return json(res, 400, { ok: false, error: 'bad json' }); }
      const stage = String(d.stage || '').trim();
      if (stage !== 'email' && stage !== 'paid') {
        return json(res, 400, { ok: false, error: 'bad stage' });
      }

      const email = String(d.email || '').trim();
      const note = String(d.note || '').trim().slice(0, 400);
      const domain = String(d.domain || '').trim().slice(0, 120);
      const price = String(d.price || '99').trim().slice(0, 20);

      // 「输入邮箱」这一步必须合法邮箱；「已付款」这一步允许留空（方便只点一下）
      if (stage === 'email' && !isValidEmail(email)) {
        return json(res, 400, { ok: false, error: '邮箱格式不对' });
      }

      let text;
      if (stage === 'email') {
        text = '🛒 <b>新的模板包购买 · 已输入邮箱</b>\n\n' +
               '📮 邮箱：<code>' + escapeHtml(email || '（未填）') + '</code>\n' +
               '🌐 域名：' + escapeHtml(domain || '（未填）') + '\n' +
               '💰 金额：¥' + escapeHtml(price) + '\n' +
               '🕐 ' + new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' }) + '\n\n' +
               '来自 blog.zaihouse.com 模板包页。等他付款。';
      } else if (stage === 'paid') {
        text = '💰 <b>模板包 · 买家点了「我已付款」</b>\n\n' +
               '📮 邮箱：<code>' + escapeHtml(email || '（未填）') + '</code>\n' +
               '🌐 域名：' + escapeHtml(domain || '（未填）') + '\n' +
               '💰 金额：¥' + escapeHtml(price) + '\n' +
               '🕐 ' + new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' }) + '\n\n' +
               '来自 blog.zaihouse.com。**请核对收款记录后再发货。**';
      } else {
        return json(res, 400, { ok: false, error: 'bad stage' });
      }

      if (note) text += '\n\n📝 备注：' + escapeHtml(note);

      tgSend(text).then(r => {
        if (r && r.ok) return json(res, 200, { ok: true });
        console.error('[blog] tg failed:', JSON.stringify(r).slice(0, 200));
        json(res, 502, { ok: false, error: '通知发送失败' });
      });
    }).catch(e => json(res, 400, { ok: false, error: String(e.message).slice(0, 80) }));
    return;
  }

  // ---------- 统计接口 ----------
  if (url === '/api/stats' && req.method === 'GET') {
    saveStats();
    const top = Object.entries(stats.byPath).sort((a, b) => b[1] - a[1]).slice(0, 15);
    const refs = Object.entries(stats.referrers).sort((a, b) => b[1] - a[1]).slice(0, 10);
    const days = Object.keys(stats.byDay).sort().slice(-14).map(d => ({ day: d, views: stats.byDay[d] }));
    return json(res, 200, {
      ok: true,
      total: stats.total,
      seed: STATS_SEED,
      today: stats.byDay[bjDay(new Date())] || 0,
      funnel: {
        view99: stats.funnel.view99,
        clickBuy: stats.funnel.clickBuy,
        rate: stats.funnel.view99 ? (stats.funnel.clickBuy / stats.funnel.view99 * 100).toFixed(1) + '%' : 'n/a',
      },
      topPages: top.map(([p, v]) => ({ path: p, views: v })),
      referrers: refs.map(([r, v]) => ({ ref: r, views: v })),
      days,
    });
  }

  // ---------- 购买链接点击计数（漏斗第二环，CF 看不到）----------
  if (url === '/go/buy' && (req.method === 'GET' || req.method === 'HEAD')) {
    if (req.method === 'GET') {
      stats.funnel.clickBuy += 1;
      statsDirty = true;
      saveStats();
    }
    res.writeHead(302, { location: 'https://mbd.pub/o/bread/YZaVlZxxZg==', 'cache-control': 'no-store' });
    return res.end();
  }

  // ---------- 静态文件 ----------
  let p = path.join(DIST, url === '/' ? 'index.html' : url);
  let resolved = (await tryFile(p)) || (await tryFile(p + '.html')) || (await tryFile(p + '/index.html'));
  if (!resolved) {
    const parts = url.split('/').filter(Boolean);
    let cur = DIST;
    for (const part of parts) {
      cur = path.join(cur, part);
      const idx = await tryFile(path.join(cur, 'index.html'));
      if (idx) { resolved = idx; break; }
    }
  }
  if (!resolved) {
    resolved = path.join(DIST, 'index.html');
    res.statusCode = 404;
  }
  const ext = path.extname(resolved).toLowerCase();
  res.setHeader('content-type', MIME[ext] || 'application/octet-stream');

  // /downloads/ 下的视频不能被 Cloudflare 缓存（2026-10-02）
  // 缓存整份 mp4 会让 Range 请求失效：源站返回 206，公网变成 200 发全量，
  // 结果是 iPhone Safari / 部分安卓浏览器拖进度条卡住或跳回开头。
  // 源站标记 no-store，Cloudflare 会直接透传，Range 得以保留。
  if (url.startsWith('/downloads/')) {
    res.setHeader('cache-control', 'no-store');
  }

  // ---------- 访问计数：只数真实浏览（GET 的页面请求），不数 HEAD 探测与图片视频 ----------
  if (ext === '.html' && req.method === 'GET') {
    const ref = req.headers.referer || req.headers.referrer || '';
    countView(url, String(ref).slice(0, 200));
  }

  // ---------- Range 请求（视频/大文件播放必需）----------
  // 只声明 accept-ranges 却不做实际分段，iPhone Safari 等播放器会卡在 00:00：
  // 它们先发 GET + Range: bytes=0- 探测，拿到 200 整份就不知道从哪续。
  const range = req.headers.range;
  let stat = null;
  try { stat = await fs.promises.stat(resolved); } catch (e) { /* 忽略 */ }
  if (range && stat && stat.isFile()) {
    const m = /^bytes=(\d*)-(\d*)$/.exec(String(range).trim());
    if (m) {
      const size = stat.size;
      let start = m[1] === '' ? null : parseInt(m[1], 10);
      let end = m[2] === '' ? null : parseInt(m[2], 10);
      if (start === null && end !== null) {           // bytes=-N 取末尾 N 字节
        start = Math.max(0, size - end);
        end = size - 1;
      } else {
        if (start === null) start = 0;
        if (end === null || end >= size) end = size - 1;
      }
      if (!Number.isFinite(start) || !Number.isFinite(end) || start > end || start >= size) {
        res.statusCode = 416;
        res.setHeader('content-range', 'bytes */' + size);
        res.end();
        return;
      }
      res.statusCode = 206;
      res.setHeader('content-range', 'bytes ' + start + '-' + end + '/' + size);
      res.setHeader('content-length', end - start + 1);
      res.setHeader('accept-ranges', 'bytes');
      if (req.method === 'HEAD') { res.end(); return; }
      fs.createReadStream(resolved, { start, end }).pipe(res);
      return;
    }
  }

  res.setHeader('accept-ranges', 'bytes');
  if (req.method === 'HEAD') {
    if (stat && stat.isFile()) res.setHeader('content-length', stat.size);
    res.end();
    return;
  }
  fs.createReadStream(resolved).pipe(res);
}

server.listen(PORT, '127.0.0.1', () => {
  console.log(`blog.zaihouse.com serve ready on http://127.0.0.1:${PORT}`);
  console.log(`[blog] TG notify: ${TG_BOT_TOKEN ? 'bot ok, chat ' + TG_CHAT_ID : 'DISABLED (no token)'}`);
});
