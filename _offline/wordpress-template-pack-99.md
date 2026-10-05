---
title: "99 元 · WordPress 独立站模板包（省掉装完 WP 后那 3-4 小时）"
description: "一键脚本跑完之后，站点还是个空壳：默认主题、空政策页、没运费、没商品。这包补齐这 3-4 小时，99 元一人一站。"
date: 2026-09-29
readTime: "8 分钟"
tags: ["独立站", "WordPress", "WooCommerce", "模板包", "跨境电商"]
pinned: false
---

> 一键脚本免费，也永远免费 —— 算是我的一点福利分享。
> **但脚本跑完之后，站点还是个空壳。**
> 这包补的就是那 3-4 小时。**99 元，一人一个站。**

## 先看成品（92 秒完整演示）

<video controls preload="metadata" playsinline style="width:100%;border-radius:10px;margin:20px 0;box-shadow:0 8px 32px rgba(0,0,0,.12)">
  <source src="/downloads/zh-template-demo.mp4" type="video/mp4">
  你的浏览器不支持 video 标签，<a href="/downloads/zh-template-demo.mp4">点这里下载看</a>。
</video>

> 全片是真实截图 —— 空壳站和装完的站都是实跑的，后台操作、店铺参考也都是真实截图。

## 先看问题在哪

脚本跑完，你的 VPS 上确实有了一个 WordPress。打开一看：

- 主题是 WordPress 默认的灰白色
- **政策页是空的** —— 支付平台认证会逐条查这几页
- 没有运费模板，结算页算不出运费
- 商品分类是空的，商品一个都没有
- 页脚什么都没有

**这些就是「空壳子」。**

它们不难，但加起来是 **3-4 小时**的手工操作。而且大部分人会卡在政策页 —— 没人告诉你平台到底查哪几页、写到什么程度算过。

## 装完你有了什么

<div class="free-pack-promo" style="background:linear-gradient(135deg,#ecfdf5 0%,#d1fae5 100%);border:2px solid #10b981;border-radius:12px;padding:20px;margin:24px 0">
<div style="font-size:18px;font-weight:700;color:#065f46;margin-bottom:12px">📦 包里有什么</div>
<ul style="margin:0;padding-left:20px;color:#065f46;line-height:2">
<li><strong>Astra 子主题</strong> —— 站点不再是默认外观</li>
<li><strong>4 套政策页</strong> —— 隐私 / 条款 / 退款 / 配送</li>
<li><strong>占位符清单</strong> —— 哪几页要改、漏了会怎样，列成表</li>
<li><strong>运费模板</strong> —— 3 个区域，含免运费门槛建议</li>
<li><strong>商品 CSV</strong> —— 5 条示例，改 SKU 和价格就能上架</li>
<li><strong>占位图 7 张</strong> —— 程序生成，不含任何他人素材</li>
</ul>
</div>

**安装约 3 分钟。** 跑一个脚本，问几个问题，装完就有个能上架的站。

## 装完怎么改？全部后台点，不碰代码

这是很多人担心的部分 —— 「我不懂代码怎么办」。

<div class="disclosure-note" style="background:#eff6ff;border:1px solid #93c5fd;border-left:4px solid #3b82f6;padding:14px 16px;border-radius:6px;margin:20px 0">
ℹ️ <strong>改配色、换 logo、改政策页文字、改商品、加运费、换主题 —— 全是后台点。</strong>
</div>

| 想改什么 | 在哪改 |
|---|---|
| **配色**（主色 / 辅助色 / 页脚） | 后台左侧「🏪 店铺设置」，取色器点一下，保存 |
| **logo** | 外观 → 自定义 → 站点标识 |
| **政策页文字** | 页面 → 找到那 4 页直接编辑 |
| **商品** | 商品 → 全部商品；批量用「商品 → 导入」选 CSV |
| **运费** | WooCommerce → 设置 → 配送 |
| **换主题** | 外观 → 主题（子主题在用，换之前先备份） |

**「店铺设置」页里还有一张导航表**，上面每一项都直接链到对应的后台页面 —— **你不用记路径**。

改完颜色去前台 **Ctrl+F5 强刷**就生效。

## 域名怎么绑？手把手

模板包**跟域名无关** —— 你可以先用免费域名跑通，真开店了再换正式域名。

### 第 1 步 · 拿到你的 VPS IP

登录买 VPS 的那个面板（或者在本地终端跑一下）：

```bash
curl -4 ifconfig.me
```

回车会给你一串数字，比如 `123.45.67.89` —— **这就是你的 IP，先存好**。

### 第 2 步 · 域名加一条 A 记录

不管你用的是免费域名还是付费域名，**操作是一样的**：

1. 打开你的域名服务商后台（dnshe / Cloudflare / 阿里云 / Namecheap 都行）
2. 找到「域名解析」或「DNS 记录」
3. 填四行信息：

| 字段 | 填什么 |
|---|---|
| **类型** | `A` |
| **主机记录** | `@`（代表根域名，不带 www） |
| **记录值** | 你上一步拿到的 VPS IP |
| **TTL** | `600` 或「自动」 |

4. 再加一条给 www：

| 字段 | 填什么 |
|---|---|
| **类型** | `CNAME` |
| **主机记录** | `www` |
| **记录值** | 你的根域名（比如 `myshop.com`） |

### 第 3 步 · 等它生效

**5 分钟到 24 小时**，大部分情况 5-10 分钟就好。

想确认好了没，在本地终端跑：

```bash
ping 你的域名
```

出来的 IP 跟你的 VPS IP 一致就说明生效了。

### 第 4 步 · WordPress 后台改网址

进入你的站点后台 → **设置 → 常规**，改两个地方：

- **WordPress 地址（URL）** → `https://你的域名`
- **站点地址（URL）** → `https://你的域名`

**改之前先备份** —— 设置 → 常规 页面最下方有备份入口，或者找主机商导出数据库。改错会进不去后台。

改完点保存，前台地址立刻就变了。

### 第 5 步 · 装 SSL 证书（必做）

**现在地址栏应该是「不安全」** —— 因为还是 http。

免费方案二选一：

- **宝塔面板方案**：VPS 上装宝塔 → 网站 → SSL → Let's Encrypt → 申请。**全自动，一分钟。**
- **Cloudflare 方案**：把域名接到 Cloudflare → SSL/TLS → Overview → 选 **Full (strict)**。之后回 VPS 装证书。

**没有 SSL 的后果很严重**：浏览器标「不安全」，支付平台会拒，Google 收录也会降权。

<div class="disclosure-note" style="background:#fffbeb;border:1px solid #fcd34d;border-left:4px solid #f59e0b;padding:14px 16px;border-radius:6px;margin:20px 0">
⚠️ <strong>容易踩的坑</strong>：改完 URL 后如果后台变成「重定向循环」打不开，说明 http 和 https 撞了。回数据库把 <code>wp_options</code> 表里的 <code>siteurl</code> 和 <code>home</code> 两个值改成完全一样就行。
</div>

### 换域名会丢东西吗？

**不会。** 商品、政策页、设置全在数据库里，跟域名无关。

换域名的正确顺序：**先备份数据库 → 改 DNS → 改 WordPress URL → 重装 SSL**。

反过来做（先改 URL 再指 DNS）会让访客暂时访问不到。

---

### 还没买域名？先用免费的

**dnshe**（<a href="https://my.dnshe.com/go.php?code=***" target="_blank" rel="noopener">dnshe.com</a>）提供**新人永久免费域名**，支持 A 记录 / CNAME，国内访问友好，后台能直接接 Cloudflare。名字选好后按上面第 2 步操作就行。

<div class="disclosure-note" style="background:#eff6ff;border:1px solid #93c5fd;border-left:4px solid #3b82f6;padding:14px 16px;border-radius:6px;margin:20px 0">
ℹ️ <strong>提醒</strong>：免费域名适合先跑通、测试、做练手。正式开店建议买正式域名 —— 客户信任度、后续扩展都更好。<a href="/posts/newbie-rewards-2026/" style="color:#2563eb">四个域名方案对比</a>
</div>


## 为什么脚本免费，模板收费？

这个问题我应该直接说清楚。

**脚本免费**，因为它是我一直在分享的东西 —— 用最少的钱、最干净的方法，把一件想做的事做到能跑。4 脚本包 Apache-2.0 开源，会一直免费。

**模板包收费**，因为那 3-4 小时不是「装个软件」，是我自己做站时踩出来的：

- 政策页写到什么程度认证才过
- 免运费门槛设多少能提客单价又不亏运费
- 变体商品的 CSV 到底怎么写才对
- 哪些配置 WP 装完默认是错的

**你买的是我整理这些的时间，不是几个文件。**

文件本身你也能自己写。但你得先知道该写什么 —— 而这就是「3-4 小时」的意思。

## 参考：店铺长什么样

> 👉 **blog.zaihouse.com 旁边的 shop.zaihouse.com** —— 一个真实运行的店铺。

**不是效果图，是真在跑的站。**

你装完能做成这样，也能做成完全不同的样子 —— **配色、首页、分类、商品都是你的**。

<div class="disclosure-note" style="background:#fffbeb;border:1px solid #fcd34d;border-left:4px solid #f59e0b;padding:14px 16px;border-radius:6px;margin:20px 0">
⚠️ <strong>说明</strong>：这个参考站的品类和风格不一定适合你。模板包给的是<strong>结构 + 起步配置</strong>，不是「跟它长得一样」。
</div>

## 定价

| 档位 | 价格 | 内容 |
|---|---|---|
| **个人商用** | **99 元** | 模板全套 + 1 个站点商用许可 |

**就这一档。** 一个人做一个站，99 块。

**为什么不是 39？** 因为 39 我自己会睡不着 —— 你拿到的东西值不到那个数，我也不想赚这个钱。99 是我能接受的价格，也是你拿到的东西的真实成本。

**包内不含任何付费插件。** 父主题是 Astra 免费版，你不需要额外买任何东西。

## 另外

免费那版出图工具一直在 —— **Kaggle 免费 GPU，不用显卡，0 元**：

<a href="/posts/kaggle-comfyui-free-guide/" style="display:inline-block;background:#111827;color:#fff;padding:10px 20px;border-radius:6px;text-decoration:none;font-weight:600;margin:8px 0">📖 0 元白嫖 AI 生图 · 完整流程</a>

**我还做了一个 Plus** —— 中文提示词优化过的出图模型，已经能用了。更强的还在测，跑通了会单独出。

## 常见问题

**Q：需要多久能上架第一个商品？**
装模板 3 分钟，填政策页占位符约 30 分钟，配运费 3 分钟，建第一个商品 10 分钟。**总共一小时之内可以开始收款。**

**Q：图片怎么办？**
包里给的是占位图，程序画的，不含任何第三方素材，你放心用。你要是有实拍图直接换。没有的话可以用上面那个免费生图工具。

**Q：跟免费视频讲的有什么区别？**
视频讲「怎么做」—— 从注册到开卖一步步。**这包补的是「装完 WP 之后那 3-4 小时」**，视频里因为太长没细讲。

**Q：WordPress / WooCommerce 会不会不兼容？**
我测过多个版本，WooCommerce 会**自动适配**你的 WordPress 版本（高版本装不上会自动降级）。但大版本更新我不保证长期兼容。

**Q：政策页你帮我写还是我自己写？**
包里有完整模板 + 占位符清单，你改填。**我不代写** —— 政策页是要承担法律责任的东西，得你自己确认。

**Q：我能用它建 5 个店吗？**
不能。**99 是一人一站。** 要多站联系我。

## 例外说明（重要，请看完再买）

我不想让你以为「买了就一劳永逸」。下面这些**不在保障范围内**：

| 情况 | 说明 |
|---|---|
| **第三方收费插件 / 授权** | 本包不含付费插件。你若自行购买 Astra Pro 或其他收费插件，其授权、到期、兼容问题需自行承担。 |
| **WordPress / WooCommerce 大版本更新** | 我会尽力修，但不保证长期兼容。平台大版本变更可能导致需手动调整。 |
| **支付网关政策变化** | 支付平台的审核标准会变。政策页是否仍合规，需你自行核实。 |
| **政策页法律效力** | 我提供的是结构模板，**不构成法律或合规建议**。内容正确性由你核实并承担。 |
| **第三方服务条款变化** | 支付网关 / Cloudflare 等服务条款变更，不在我的责任范围。 |
| **税务与产品合规** | 税务申报、公司注册、产品认证需你自行处理。 |

**简单说：我卖的是我做的那部分，不卖结果保证。**

## 售后

- 装不上 → 联系我，我远程看
- 政策页认证被退回 → 把被退原因发我，我帮你改
- 报错 → 附上第几步 + 报错原文

**不承诺定期更新。** 平台政策、WordPress 大版本变更时我会在需要时修，但不排期。

---

## 💬 想要这份模板包？

**99 元一人一站。** 三步就好。

<div class="free-pack-promo" style="background:linear-gradient(135deg,#ecfdf5 0%,#d1fae5 100%);border:2px solid #10b981;border-radius:12px;padding:20px;margin:24px 0">

<div style="font-size:16px;font-weight:700;color:#065f46;margin-bottom:12px">第 1 步 · 留下联系方式</div>
<div id="zhDomainWrap" style="margin-bottom:12px">
<label for="zhDomain" style="display:block;font-size:13px;color:#047857;margin-bottom:5px;font-weight:600">想用哪个域名？（选填）</label>
<input id="zhDomain" type="text" placeholder="例：myshop.com —— 还没有就先空着"
  style="width:100%;padding:12px 14px;border:1px solid #a7f3d0;border-radius:8px;font-size:15px;background:#fff;color:#111">
<div style="font-size:12px;color:#059669;margin-top:5px;line-height:1.6">这里只是备注，不会自动建站。填了我就在发货邮件里告诉你怎么把它指过来。</div>
</div>
<div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
<input id="zhEmail" type="email" placeholder="你的邮箱（下载链接发到这里）"
  style="flex:1;min-width:220px;padding:12px 14px;border:1px solid #a7f3d0;border-radius:8px;font-size:15px;background:#fff;color:#111">
<button id="zhStep1" style="padding:12px 24px;background:#059669;color:#fff;border:none;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer">下一步</button>
</div>
<div id="zhMsg1" style="margin-top:10px;font-size:14px;color:#065f46"></div>

</div>

<div id="zhStep2Box" style="display:none;background:linear-gradient(135deg,#fffbeb 0%,#fef3c7 100%);border:2px solid #f59e0b;border-radius:12px;padding:20px;margin:24px 0">

<div style="font-size:16px;font-weight:700;color:#92400e;margin-bottom:6px">第 2 步 · 扫码付款 ¥99</div>
<div style="font-size:14px;color:#92400e;margin-bottom:14px">微信 / 支付宝都行 · 备注「模板包」</div>

<div style="display:flex;gap:18px;flex-wrap:wrap;justify-content:center;margin-bottom:16px">
<img src="/downloads/pay-wechat.png" alt="微信收款码" style="width:210px;border-radius:8px;border:1px solid #e5e7eb;background:#fff">
<img src="/downloads/pay-alipay.png" alt="支付宝收款码" style="width:210px;border-radius:8px;border:1px solid #e5e7eb;background:#fff">
</div>

<button id="zhPaid" style="width:100%;padding:14px;background:#d97706;color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:700;cursor:pointer">我已付款</button>
<div id="zhMsg2" style="margin-top:10px;font-size:14px;color:#92400e;text-align:center"></div>

</div>

<div id="zhStep3Box" style="display:none;background:#f0fdf4;border:2px solid #22c55e;border-radius:12px;padding:20px;margin:24px 0">
<div style="font-size:16px;font-weight:700;color:#166534;margin-bottom:8px">✓ 收到，我去核对</div>
<div style="font-size:15px;color:#166534;line-height:1.8">
我收到你的通知了，现在去核对收款记录。<br>
<b>确认到账后会发邮件到你填的邮箱</b>，附下载链接。<br>
当天回，最晚不过夜。
</div>
</div>

<div id="zhAlt" style="font-size:14px;color:#6b7280;margin-top:12px">
付款有问题？直接 <a href="mailto:support@zaihouse.com">support@zaihouse.com</a>
</div>

<script>
(function () {
  var API = '/api/order', PRICE = '99';
  var $ = function (id) { return document.getElementById(id); };
  var email = $('zhEmail'), domain = $('zhDomain');
  var b1 = $('zhStep1'), b2 = $('zhStep2Box'), b3 = $('zhStep3Box'), paid = $('zhPaid');
  var m1 = $('zhMsg1'), m2 = $('zhMsg2');
  var got = { email: '', domain: '' };

  function post(stage, extra) {
    return fetch(API, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ stage: stage, email: got.email, domain: got.domain, price: PRICE })
    }).then(function (r) { return r.json().catch(function () { return { ok: false }; }); });
  }

  b1.addEventListener('click', function () {
    var v = (email.value || '').trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) {
      m1.textContent = '✗ 邮箱填一下，我发下载链接要用'; m1.style.color = '#dc2626'; return;
    }
    got.email = v;
    got.domain = (domain.value || '').trim();
    m1.textContent = '✓ 记下了';
    b1.disabled = true; b1.style.opacity = '.55';
    b2.style.display = 'block';
    b2.scrollIntoView({ behavior: 'smooth', block: 'center' });
    post('email').then(function (r) {
      if (!r.ok) m1.textContent = '（邮箱已记下，通知没发出去，不影响付款）';
    });
  });

  paid.addEventListener('click', function () {
    paid.disabled = true; paid.textContent = '正在通知…';
    m2.textContent = '';
    post('paid').then(function (r) {
      if (r.ok) {
        b2.style.display = 'none';
        b3.style.display = 'block';
        b3.scrollIntoView({ behavior: 'smooth', block: 'center' });
      } else {
        paid.disabled = false; paid.textContent = '我已付款';
        m2.textContent = '✗ 通知没发出去（' + (r.error || '网络问题') + '），请直接邮件告诉我';
        m2.style.color = '#dc2626';
      }
    }).catch(function () {
      paid.disabled = false; paid.textContent = '我已付款';
      m2.textContent = '✗ 网络问题，请直接邮件告诉我';
      m2.style.color = '#dc2626';
    });
  });
})();
</script>

---

> **先看免费教程，再决定要不要买。**
> 一键建站脚本（Apache-2.0，永远免费）：
> <a href="/posts/openclaw-30min-guide/" style="display:inline-block;background:#059669;color:#fff;padding:10px 20px;border-radius:6px;text-decoration:none;font-weight:600;margin:8px 0">📖 30 分钟部署 OpenClaw + 4 脚本免费下载</a>
