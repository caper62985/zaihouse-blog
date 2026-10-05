---
title: "0 元白嫖 AI 生图 · Kaggle 免费 GPU 跑 ComfyUI 完整流程"
description: "本地电脑 0 配置、0 安装、0 翻墙，用 Kaggle 免费 GPU + ComfyUI + FLUX.1-Schnell 出图。4 步注册即用，代码工作流全打包，新手小白也能跟着做完。FLUX.1 出图 / Wan2.1 视频教程测试中。"
series: free
date: 2026-09-21
pinned: false
updated: 2026-10-02
readTime: "15 分钟"
tags: ["免费 AI 生图", "不花一分钱", "Kaggle 免费 GPU", "ComfyUI", "FLUX.1"]
---

# 0 元白嫖 AI 生图 · Kaggle 免费 GPU 跑 ComfyUI 完整流程

> 本文 + 代码 + 工作流，**全程不花一分钱**。本地电脑 0 配置、0 安装、0 翻墙。

## 🎬 先看视频 · B 站 / YouTube 同一支

<a class="yt-hero-card" href="https://www.bilibili.com/video/BV1Lhhn6hEjM" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/BV1Lhhn6hEjM.jpg" width="1920" height="1080" alt="Kaggle 云端 GPU 跑 ComfyUI 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">📺 B 站 · 国内不卡</span>
<span class="yt-hero-card-title">不花一分钱｜Kaggle 云端 GPU 跑 ComfyUI-新手小白复制粘贴-免费AI生图完整流程</span>
<span class="yt-hero-card-sub">KAGGLE 免费 GPU → ComfyUI → 复制粘贴 → 免费 AI 生图 · 16 分 49 秒</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> B 站观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

<a class="yt-hero-card" href="https://youtu.be/BhkCPN3Gb1s" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/BV1Lhhn6hEjM.jpg" width="1920" height="1080" alt="Kaggle 云端 GPU 跑 ComfyUI 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">▶️ YouTube · 海外顺</span>
<span class="yt-hero-card-title">不花一分钱｜Kaggle 云端 GPU 跑 ComfyUI-新手小白复制粘贴-免费AI生图完整流程</span>
<span class="yt-hero-card-sub">KAGGLE 免费 GPU → ComfyUI → 复制粘贴 → 免费 AI 生图 · 16 分 49 秒</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> YouTube 观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

<p style="margin:0 0 20px;font-size:14px;color:#666">两支是同一支视频，<strong>国内点上面 B 站、海外点下面 YouTube</strong>，都能看。</p>

## 为什么写这篇？

**花 5000 元/月买 Midjourney？** 不需要。
**本地 RTX 4090 跑大模型？** 不需要。
**全套 ComfyUI 工作流？** 也不用花一分钱。

Kaggle 免费给你 **T4×2 + 32 GB 显存**（每周 30 小时 GPU）—— **足够跑 FLUX.1-Schnell 出图**。

## 4 步流程（不花一分钱）

### Step 1：注册 Kaggle（不花一分钱）
- 打开 https://www.kaggle.com 注册（**完全免费**）
- 不需要绑卡
- 不需要翻墙
- 邮箱 + Google 账号即可

### Step 2：开 Notebook + 装 ComfyUI（不花一分钱）
- New Notebook → Settings → GPU T4×2 → Internet On
- 粘贴代码（装环境 + 克隆 ComfyUI + 下 FLUX.1 模型）
- Kaggle 自带 Python 环境，无需本地配置

> 💡 **手机号验证说明**：第一次开 GPU 时 Kaggle 会要求**手机号验证**（防滥用）—— **中国 +86 手机号也可以**，验证后**永久免费**，不会扣费。

### Step 3：下载 FLUX.1 模型（不花一分钱）
- Kaggle 自带 19.5 GB 磁盘
- FLUX.1-Schnell GGUF（开源）
- HuggingFace + ModelScope 镜像（免 Token）

### 📹 Wan2.1 AI 视频教程 · 测试中

> 本帖专注**生图**。Wan2.1 视频生成教程正在测试中（Kaggle 免费 GPU 跑 Wan2.1-14B INT8 + ComfyUI），预计下周上线。
>
> 视频教程将覆盖：
> - Kaggle 下载 Wan2.1-14B INT8（13 GB，ModelScope 镜像）
> - ComfyUI + WanVideoWrapper 节点配置
> - 15 秒 720p 视频生成 prompt 模板
> - trycloudflare 隧道公网访问
>
> 视频教程包将在完成后与生图教程包合并打包发布。

### Step 4：跑工作流（不花一分钱）
- ComfyUI Web UI 通过 cloudflared 临时隧道开公网
- 拖入工作流 JSON → 改 prompt → Queue Prompt
- 整个流程 Kaggle GPU **不花一分钱**

## 不花一分钱的具体清单

| 资源 | 工具 | 价格 |
|---|---|---|
| 云端 GPU | Kaggle T4×2 32GB | **不花一分钱** |
| AI 绘图模型 | FLUX.1-Schnell GGUF（开源）| **不花一分钱** |
| 工作流引擎 | ComfyUI（MIT）| **不花一分钱** |
| 公网隧道 | Cloudflare Tunnel | **不花一分钱** |
| 教程 + 代码 | 本文 | **不花一分钱** |

## 为什么不花一分钱？

| 其他方案 | 月费 |
|---|---|
| Midjourney | $10/月（≈ ¥70）|
| Adobe Firefly | $5/月 |
| Stable Diffusion Cloud | $20/月 |
| **Kaggle 免费方案** | **不花一分钱** |

## 📥 完整代码下载

🔗 **下载链接**：[https://blog.zaihouse.com/downloads/kaggle-v3.zip](https://blog.zaihouse.com/downloads/kaggle-v3.zip)

（右键"另存为"即可下载）

### 包内容

```
kaggle-license-v2.zip
├── 临时隧道出图.py    ✅ 直接运行，无需配置
└── 2.自定义域名出图.py  需填 CF Token
```

### 两个版本怎么选？

| 场景 | 用哪个 |
|---|---|
| 只想快速跑一遍 | **临时隧道版**（临时隧道出图.py）|
| 长期用 + 自定义域名 | **自定义域名版**（2.自定义域名出图.py）|

## 5 步使用流程

1. **登录 Kaggle**（不花一分钱）
2. **New Notebook** → Settings → GPU T4×2 + Internet On
3. **Cell 1**：粘贴 `临时隧道出图.py`（或 `2.自定义域名出图.py`）
   - 临时隧道版：直接 Run，等 5-10 分钟自动出链接
   - 自定义域名版：先把 CF Token 填进 `MY_CF_TOKEN`，再 Run
4. **浏览器打开** trycloudflare.com 链接（或自定域名）
5. **Load Workflow** → `3.生图.json` → 改 prompt → Queue Prompt

## 谁适合？

✅ 想学 AI 但**不花一分钱**的小白
✅ 有 Kaggle 账号但不知道能干嘛的人
✅ 想做 AI 绘图 + 视频副业但没预算的人
✅ 跨境电商想批量生成产品图的人

## 常见问题

**Q：不花一分钱真的不花一分钱？**
A：真不花一分钱。Kaggle 免费版足够。

**Q：能跑视频吗？**
A：本帖专注**出图**。视频用 Wan2.1（另一帖）。

**Q：能商用吗？**
A：FLUX.1-Schnell + ComfyUI 全部 Apache 2.0 / MIT。

**Q：手机能用吗？**
A：不能。Kaggle Notebook 需要电脑。

## ⚠️ 免责声明

- 本教程仅供学习用途
- 商用前请检查模型 license
- 不花一分钱 ≠ 100% 免费（Kaggle 限速 + 模型 license）
- 实际结果取决于模型版本 + 硬件配置