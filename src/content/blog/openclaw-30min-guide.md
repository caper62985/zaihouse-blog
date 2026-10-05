---
title: "新人不用手·一键脚本 · 裸机 VPS 5-15 分钟跑通 OpenClaw + 公网 + 跨境独立站"
description: "4 个一键脚本，对应 4 种 VPS 状态。裸机 VPS 3-5 分钟跑通 OpenClaw，已装的改配置 3-5 分钟，公网+TG bot 5-10 分钟，一键建完整跨境独立站 10-15 分钟。全部开源免费（Apache-2.0），直接下载。"
series: script
date: 2026-09-16
pinned: false
updated: 2026-10-02
readTime: "5-15 分钟"
tags: ["OpenClaw 部署脚本", "一键脚本", "VPS", "跨境电商出海", "免费脚本"]
# 2026-09-29: 取消置顶（首页第 2 位改给福利大全）。正文与导航入口不变，
# 仍可从 /posts/openclaw-30min-guide/ 和导航「4 脚本免费」直达。
---

# 新人不用手·一键脚本 · 裸机 VPS 5-15 分钟跑通 OpenClaw

> 裸机 VPS → OpenClaw → 公网 → 跨境独立站，**小白 30 秒对号入座**，5-15 分钟跑通。

---

## 🎬 先看视频 · 10 分 46 秒完整演示

<a class="yt-hero-card" href="https://youtu.be/0ev0_bMLxBM" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/0ev0_bMLxBM.jpg" width="1920" height="1080" alt="4 个一键脚本完整演示视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">YouTube</span>
<span class="yt-hero-card-title">新人不用手·一键脚本 · 裸机 VPS 5-15 分钟跑通 OpenClaw + 公网 + 跨境独立站</span>
<span class="yt-hero-card-sub">耗时一个月 + 花费近万沉淀出的 4 个一键脚本 · 全部开源免费</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> YouTube 观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

---

## 🎁 免费：4 个一键脚本全部开源

**裸机 VPS 3-5 分钟跑通 OpenClaw**，不用自己装任何东西。脚本在本页**下方下载区**，Apache-2.0 免费，商用 / 修改 / 分发都可以。

> ⚠️ **裸机脚本只装 OpenClaw + 配 API key**。要公网 / TG bot / 跨境站 → 用包里的 `openclaw_deploy.sh` / `zaihouse_build.sh`。
>
> 👉 先去 <a href="https://cloud.siliconflow.cn/i/kIJ2uUha" target="_blank" rel="noopener">cloud.siliconflow.cn/i/kIJ2uUha</a> 拿 API key（推荐链接 · 新人优惠）

---
## 🎯 你的 VPS 状态？完整 4 脚本决策

| VPS 状态 | 用哪个脚本 | 时间 | 下载 |
|---|---|---|---|
| 🆕 **全新 VPS（裸机 Ubuntu）** | **一键跑通_全新VPS.sh** | **3-5 分钟** | [下载区](#-完整-4-脚本免费下载) |
| ✅ OpenClaw 已装，没公网 | openclaw_deploy.sh | 5-10 分钟 | [下载区](#-完整-4-脚本免费下载) |
| ✅ OpenClaw 已跑，要改配置 | openclaw_quickstart.sh | 3-5 分钟 | [下载区](#-完整-4-脚本免费下载) |
| 🏗️ 直接做完整跨境独立站 | zaihouse_build.sh | 10-15 分钟 | [下载区](#-完整-4-脚本免费下载) |

---

## 📦 完整 4 脚本免费下载

**2026-09-23 更新：4 脚本 + 选择指南全部开源免费（Apache-2.0），面包多付费档已下架。**

**一键打包下载**（95 KB · 8 个文件 · Apache-2.0）：

<a href="/downloads/zaihouse-pack-v1.1.0.zip" style="display:inline-block;padding:10px 22px;background:#059669;color:#fff;border-radius:8px;font-weight:600;text-decoration:none">⬇️ 下载 zaihouse-pack v1.1.0</a>

> 💡 <strong>v1.1.0 修好了裸机首装装不上的问题</strong>：Node 版本、gateway 启动参数、配置路径三处都改过了。新买 VPS 直接下这个版本，不用再去 GitHub 拿源码。
> <strong>想要 GitHub 仓库</strong> → <a href="https://github.com/caper62985/zaihouse-pack" target="_blank" rel="noopener">caper62985/zaihouse-pack</a>

**包内含 8 个文件**：
- ✅ `一键跑通_全新VPS.sh` — 裸机 VPS 装 OpenClaw
- ✅ `openclaw_deploy.sh` — OpenClaw + 公网 + TG bot
- ✅ `openclaw_quickstart.sh` — 已装 OpenClaw 改配置
- ✅ `zaihouse_build.sh` — 完整跨境独立站一键建站
- ✅ `选哪个脚本.html` — 30 秒对号入座
- ✅ `LICENSE` — Apache-2.0 开源协议
- ✅ `README.md` — 使用说明
- ✅ `CHANGELOG.md` — 版本记录

> **API provider 支持**：百炼 / OpenAI / Anthropic / DeepSeek / **智谱 GLM（免费，不充值就能用）**

**怎么用（3 步）**：
```bash
# 1. 上传到 VPS（你电脑执行）
scp zaihouse-pack-v1.1.0.zip root@你的VPS-IP:/root/

# 2. 解压 + 跑
cd /root
unzip zaihouse-pack-v1.1.0.zip
bash 一键跑通_全新VPS.sh    # 或其他 3 个脚本（看选哪个脚本.html）

# 3. 验证
curl http://localhost:18789/healthz
```

---

## 🎬 视频演示 · 独立站模板 v1.4（真实安装实录）

**先看视频再决定要不要动手** —— 下面这段是 <a href="https://my.racknerd.com/aff.php?aff=21343" target="_blank" rel="noopener">**RackNerd 洛杉矶 VPS**</a> 上**从零安装**的完整实录，2 分 29 秒，包含装完的站点实拍：

<video controls preload="none" style="width:100%;max-width:860px;border-radius:12px;display:block;margin:16px 0" poster="">
  <source src="/downloads/zaihouse-install-demo.mp4" type="video/mp4">
  你的浏览器不支持 video 标签，<a href="/downloads/zaihouse-install-demo.mp4" target="_blank" rel="noopener">点这里用浏览器打开</a>。
</video>

**视频里能看到的**：装完的站点有完整样式、分类名正确、商品图配对、没有默认内容。

**在 B 站看同一支视频**（手机上看更方便，不卡）：

<a class="yt-hero-card" href="https://www.bilibili.com/video/BV1hBam6eEA9" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/BV1hBam6eEA9.jpg" width="1672" height="940" alt="独立站不用从零建 WordPress 一键安装模板包 10 分钟上线 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">📺 B 站</span>
<span class="yt-hero-card-title">独立站不用从零建 · WordPress 一键安装模板包 10 分钟上线</span>
<span class="yt-hero-card-sub">洛杉矶 VPS 实拍，从空服务器到能上架 · 2 分 30 秒</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> B 站观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

**配套 WordPress 模板包 v1.4（付费）** —— 视频看完想要包，或想直接拿现成的：

<a href="/posts/zaihouse-template-99/" style="display:inline-block;background:#10b981;color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:700;font-size:18px">
💬 咨询购买 zaihouse-template v1.4
</a>

> ℹ️ **推荐说明**：上面 RackNerd 是推荐 / 邀请链接，你通过它注册时商家会给本站一份**推荐奖励**，**但不会向你多收任何一分钱**——你自己该拿的优惠和奖励照拿不误，不用任何链接也能注册。

---

## 🎬 视频演示 · 海外也能直接看

> 📺 **YouTube**：<a href="https://youtu.be/0ev0_bMLxBM" target="_blank" rel="noopener">4个一键脚本 · 裸机 VPS 5-15 分钟跑通 OpenClaw + 公网 + 跨境独立站</a>（10 分 46 秒）
>
> 🎬 频道：YouTube **@ZAIHOUSE-COM**

> 🎬 **订阅 + 评论区留言**：想看 deploy / quickstart / zaihouse_build 单个脚本的详细演示。
>
> **完整 4 脚本** → 见上方「📦 完整 4 脚本免费下载」区（已开源）。

---

## 📚 配套资源

- 📖 **9 步跨境教程**：[blog.zaihouse.com/posts/cross-border-9step-ppt/](/posts/cross-border-9step-ppt/)
- 🎁 **新人全套注册优惠福利**（参考）：[/posts/newbie-rewards-2026/](/posts/newbie-rewards-2026/)
- 🛠️ **OpenClaw 文档**：[blog.zaihouse.com](https://blog.zaihouse.com)
- 💻 **硅基流动**（AI 模型 API）：[cloud.siliconflow.cn/i/kIJ2uUha](https://cloud.siliconflow.cn/i/kIJ2uUha)
- 📱 **mesimgo**（海外手机号）：[mesimgo.com/zh-tw?ref=2I3ZKMEJ](https://mesimgo.com/zh-tw?ref=2I3ZKMEJ)
- 💳 **Bybit**（海外支付/收款，最高 120 USDT）：[bybitglobal.com/invite?ref=ENAPZGG](https://www.bybitglobal.com/invite?ref=ENAPZGG)

---

## ⚠️ 合规提示

- 所有优惠链接仅供新人参考，实际优惠以平台官网为准
- 请使用真实身份信息注册，确保符合当地法律法规
- 跨境收款需海外主体（香港 / 英国 / 美国）