---
title: "0 元白嫖 AI 生视频 · Kaggle 免费 GPU 跑 MiniMax-H3 完整流程"
description: "MiniMax-H3 视频+音频生成模型 32GB，Kaggle 自带 19.5GB 磁盘装不下。用 Kaggle Datasets 挂载突破磁盘限制，全程 0 元，一键包下载，小白也能跑通。"
series: free
date: 2026-10-02
pinned: false
updated: 2026-10-02
readTime: "12 分钟"
tags: ["免费 AI 生图", "不花一分钱", "Kaggle 免费 GPU", "ComfyUI", "AI 视频"]
---

# 0 元白嫖 AI 生视频 · Kaggle 免费 GPU 跑 MiniMax-H3 完整流程

> 本文 + 一键包，**全程不花一分钱**。本地电脑 0 配置、0 安装。

## 🎬 先看视频 · B 站 / YouTube 同一支

<a class="yt-hero-card" href="https://www.bilibili.com/video/BV16qa26jEAX" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/BV16qa26jEAX.jpg" width="1672" height="940" alt="Kaggle 免费 GPU 跑 MiniMax H3 参考图生视频 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">📺 B 站 · 国内不卡</span>
<span class="yt-hero-card-title">不花一分钱｜Kaggle免费GPU跑MiniMax H3 参考图生视频 3步跑通</span>
<span class="yt-hero-card-sub">32GB 模型绕开 19.5GB 磁盘限制 · 一键脚本 + 工作流 JSON · 7 分 19 秒</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> B 站观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

<a class="yt-hero-card" href="https://youtu.be/GACyBamzSHo" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/GACyBamzSHo.jpg" width="1280" height="720" alt="Kaggle 免费 GPU 跑 MiniMax H3 参考图生视频 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">▶️ YouTube · 海外顺</span>
<span class="yt-hero-card-title">不花一分钱｜Kaggle免费GPU跑MiniMax H3 参考图生视频 3步跑通</span>
<span class="yt-hero-card-sub">32GB 模型绕开 19.5GB 磁盘限制 · 一键脚本 + 工作流 JSON</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> YouTube 观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

<p style="margin:0 0 20px;font-size:14px;color:#666">两支是同一支视频，<strong>国内点上面 B 站、海外点下面 YouTube</strong>。视频里把 <strong>32GB 装进 19.5GB 磁盘</strong> 那一步讲得最细，文字版这里有。</p>

## 为什么写这篇？

[生图那篇](/posts/kaggle-comfyui-free-guide/)里的 FLUX.1 只有 1.3 GB，Kaggle 那 19.5 GB 磁盘随便装。

**MiniMax-H3 不一样** —— 它是**视频 + 音频一起生成**（人物说话，嘴型和声音对得上），模型一共 **32.02 GB**：

| 文件 | 大小 | 作用 |
|---|---|---|
| `MiniMax-H3-Ref2VA-Pruned-Q4_K_M.gguf` | 11.56 GB | H3 主模型（视频+音频） |
| `Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-IQ4_XS.gguf` | 13.44 GB | 文本编码器 |
| `Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-mmproj-BF16.gguf` | 1.20 GB | 视觉投影 |
| `minimax_h3_video_vae_fp16.safetensors` | 5.21 GB | 视频 VAE |
| `minimax_h3_audio_vae_fp32.safetensors` | 605.25 MB | 音频 VAE |
| **合计** | **32.02 GB** | |

**32 GB 装不进 19.5 GB 的磁盘** —— 这就是绝大多数人卡住的地方。

**这帖的解法：把模型传成 Kaggle Dataset 挂载 —— 不占 Notebook 磁盘。**

## 这帖解决什么

```
✅ 突破 Kaggle 19.5 GB 磁盘限制（Dataset 挂载 + 软链接）
✅ 一键包下载，代码不用手抄
✅ 自动开隧道、自检节点、固定 ComfyUI 版本
✅ 全程 0 元（GPU 免费 30 小时/周，Dataset 存储也免费）
```

## 3 步流程

### Step 1：注册 Kaggle

- 打开 https://www.kaggle.com 注册（**完全免费**）
- 不需要绑卡，不需要翻墙
- 邮箱 + Google 账号即可

> 💡 **手机号验证**：第一次开 GPU 时 Kaggle 会要求**手机号验证**（防滥用）—— **中国 +86 手机号也可以**，验证后**永久免费**。

### Step 2：把 5 个模型传成 Dataset

**这一步是本帖的核心。** 模型不进 Notebook 磁盘，进 Dataset —— 所以不受 19.5 GB 限制。

1. Kaggle 右上角 → **Datasets** → **+ New Dataset**
2. 名字建议填 `minimaxh3`，可见性选 **Private**（别公开）
3. **上传那 5 个文件**（下载地址在下面第 4 节，**全部实测可访问**）
4. 上传完点 **New Version** → 勾选 **Make dataset available**（这句决定能不能挂载）

> ⚠️ **这一步最花时间**：32 GB 上传，看网速，**建议睡前传**。
>
> 5 个文件一个都不能少，**名字必须完全一致**（大小写敏感）。

### Step 3：开 Notebook 跑脚本

1. **New Notebook** → **Add Input** → 选你刚传的 Dataset
2. **Settings** → Accelerator 选 **GPU T4×2**、**Internet On**
3. 点 **+ Code**，把 `1.Kaggle一键运行.py` 整个粘进去
4. **改第 7 行**：把 `casper62985/minimaxh3` 换成你自己的
5. **Run All**，等 5-10 分钟出链接

> 💡 第 7 行填错也能跑 —— 脚本下面会自动在 `/kaggle/input` 里扫描兜底。

## 📥 一键包下载

🔗 **[minimax-h3-kaggle.zip](https://blog.zaihouse.com/downloads/minimax-h3-kaggle.zip)**

（右键"另存为"即可 —— 比从网页复制长脚本靠谱，**少一行就报错**）

```
minimax-h3-kaggle/
├── 1.Kaggle一键运行.py            整个粘进一个 Cell
├── 2.H3工作流_参考图生视频.json    跑完后在 ComfyUI 里导入
└── 3.使用说明.txt                  完整步骤 + 常见问题
```

### 脚本已经帮你处理好的事

```
✅ 自动扫描 /kaggle/input 兜底（填错路径也能跑）
✅ 固定 ComfyUI 到含 H3 原生节点的 commit（不会自动升级跑崩）
✅ 软链接挂模型，不复制、不占 Notebook 磁盘
✅ 保留 Kaggle 自带的 CUDA 版 PyTorch（不重装，避免版本冲突）
✅ 自动修一个已知类型标注兼容问题
✅ 自动开 cloudflared 隧道并打印公网地址
✅ 启动后自检 7 个关键节点，缺哪个会明确报出来
```

## 📄 核心逻辑（看懂 3 段就够了）

```python
# 1) 你的 Dataset 路径（第 7 行，改这里）
DATA = Path('/kaggle/input/datasets/你的用户名/minimaxh3')

# 2) 软链接，不是复制 —— 复制会吃磁盘，正是要避开的东西
for folder, names in FILES.items():
    for name in names:
        (COMFY/'models'/folder/name).symlink_to(DATA/name)

# 3) 启动 + 开临时隧道拿公网地址
server = Popen([python, 'main.py', '--listen', '127.0.0.1', '--port', port, ...])
proxy  = Popen([cloudflared, 'tunnel', '--url', f'http://127.0.0.1:{port}'])
```

**为什么用软链接**：Kaggle 把 Dataset 挂在 `/kaggle/input`（只读、不占磁盘）。**复制**到 Notebook 磁盘 = 白吃 32 GB，还是会爆；**软链接**只是指过去，实际文件不占地方。

## 🎬 跑起来之后

1. 脚本会打印一个 `trycloudflare.com` 链接
2. 浏览器打开 → **Load Workflow** → 导入 `2.H3工作流_参考图生视频.json`
3. **在 `LoadImage` 节点上传你的参考图**（建议正脸清晰照）
4. 改 prompt → **Queue Prompt**
5. 视频输出在 `ComfyUI/output/`

**工作流默认参数**（先照默认跑一次确认能通）：

```
分辨率 512 × 288      帧数 73      采样 12 步
输出 H3_口播_第一段.mp4（视频 + 音频一起出）
```

**参考图决定什么**：它会**保持参考图里的脸部特征、发型、服装、背景和机位不变**。所以参考图越清晰正脸，效果越稳。

## 📥 5 个模型下载地址

**以下链接全部实测可访问（HTTP 200）**，每个都能直接点开下载：

| # | 文件 | 大小 | 用途 | 下载 |
|---|---|---|---|---|
| 1 | `MiniMax-H3-Ref2VA-Pruned-Q4_K_M.gguf` | 11.56 GB | H3 主模型 | [点此下载](https://huggingface.co/Abiray/MiniMax-H3-Pruned-GGUF/resolve/main/MiniMax-H3-Ref2VA-Pruned-Q4_K_M.gguf) |
| 2 | `Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-IQ4_XS.gguf` | 13.44 GB | 文本编码器 | [点此下载](https://huggingface.co/nif0/Qwen3-VL-32B-Instruct-MiniMax-H3-GGUF/resolve/main/Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-IQ4_XS.gguf) |
| 3 | `Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-mmproj-BF16.gguf` | 1.20 GB | 视觉投影 | [点此下载](https://huggingface.co/nif0/Qwen3-VL-32B-Instruct-MiniMax-H3-GGUF/resolve/main/Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-mmproj-BF16.gguf) |
| 4 | `minimax_h3_video_vae_fp16.safetensors` | 5.21 GB | 视频 VAE | [点此下载](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) |
| 5 | `minimax_h3_audio_vae_fp32.safetensors` | 605.25 MB | 音频 VAE | [点此下载](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |

> ℹ️ 32 GB 建议**用电脑下载**再传 Kaggle。**Kaggle 服务器能直连 huggingface**（IP 段没被墙），在 Notebook 里拉不用翻墙。

## 不花一分钱的具体清单

| 资源 | 工具 | 价格 |
|---|---|---|
| 云端 GPU | Kaggle T4×2 32GB | **不花一分钱** |
| 模型存储 | Kaggle Private Dataset | **不花一分钱** |
| AI 视频模型 | MiniMax-H3（开源权重）| **不花一分钱** |
| 工作流引擎 | ComfyUI（MIT）| **不花一分钱** |
| 公网隧道 | Cloudflare Tunnel | **不花一分钱** |
| 教程 + 代码 | 本文 | **不花一分钱** |

## 为什么不花一分钱？

| 其他方案 | 月费 |
|---|---|
| Runway Gen-4 | $15/月（≈ ¥108）|
| Pika | $8/月（≈ ¥58）|
| Kling / 可灵 | ¥几十起 |
| **Kaggle 免费方案** | **不花一分钱** |

**差别在于**：Runway 那类给你的是**封装好的网页**，Kaggle 给的是**完整 GPU** —— 你想跑什么模型都行。

## 常见问题

**Q：为什么要传 Dataset，不能直接下吗？**
A：能，但 32 GB 装不进 19.5 GB 磁盘。脚本有直连兜底，但大概率失败。

**Q：Dataset 有容量限制吗？**
A：Private Dataset 存储免费，容量远够 32 GB。

**Q：免费额度够用吗？**
A：每周 30 小时 GPU。**注意免费额度同时只能跑一个 Notebook** —— 跟你[生图那个教程](/posts/kaggle-comfyui-free-guide/)会互相抢，**同时只能开一个**。

**Q：出视频要多久？**
A：T4 上跑 73 帧 512×288 通常**几分钟到十几分钟**。**建议先照默认参数跑一次。**

**Q：为什么脚本要固定 ComfyUI 的 commit？**
A：H3 节点需要特定版本。**不固定的话 ComfyUI 一升级就可能跑不起来** —— 这是踩过的坑。

**Q：能商用吗？**
A：**请自行向 MiniMax 确认模型 license**，以官方最新条款为准，商用前请自行确认。

**Q：手机能用吗？**
A：不能。Kaggle Notebook 需要电脑。

## ⚠️ 免责声明

- 本教程仅供学习用途
- **不花一分钱 ≠ 100% 免费**（Kaggle 有速率限制 + 模型 license 另有规定）
- 实际效果取决于模型版本 + 硬件配置
- 商用前请检查模型 license

## 📚 相关内容

- 📖 [0 元白嫖 AI 生图 · FLUX.1 完整流程](/posts/kaggle-comfyui-free-guide/)（同一套 Kaggle 环境，出图篇）
- 📖 [4 个一键脚本（全部免费 Apache-2.0）](/posts/openclaw-30min-guide/)
- 🎁 [新人注册优惠](/posts/newbie-rewards-2026/)（SiliconFlow 一毛钱换 16 元券）
