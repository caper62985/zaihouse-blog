# ============================================================
#  Kaggle Notebook - Cell 2: ComfyUI + MiniMax H3 + Cloudflare Tunnel
#  域名: kaggle.zaikafei.com
#  作者: zai 主理 · 部署时间: 2026-09-19
#
#  使用:
#  1. 复制整个 Cell 内容
#  2. 粘贴到 Kaggle Notebook 第二个 Cell
#  3. 跑 (Ctrl+Enter / Shift+Enter)
#  4. 看到 "👉 部署完成" 即可访问 https://kaggle.zaikafei.com
# ============================================================

import os
import subprocess
import time

# ============================================================
# 第 1 步: 初始化工作目录 + 克隆 ComfyUI
# ============================================================
print("=" * 60)
print("  第 1 步: 克隆 ComfyUI")
print("=" * 60)
%cd /kaggle/working

# 清理旧文件
!rm -rf /kaggle/working/ComfyUI

# 克隆 ComfyUI（最新稳定版）
!git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git 2>&1 | tail -3
%cd /kaggle/working/ComfyUI
print("  ✅ ComfyUI 克隆完成")

# ============================================================
# 第 2 步: 安装 PyTorch + ComfyUI 依赖（Kaggle T4 GPU 优化版）
# ============================================================
print()
print("=" * 60)
print("  第 2 步: 安装 PyTorch + 依赖")
print("=" * 60)
!pip install -q --upgrade pip
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
!pip install -q xformers==0.0.23.post1 --index-url https://download.pytorch.org/whl/cu121
!pip install -q -r /kaggle/working/ComfyUI/requirements.txt 2>&1 | tail -3
!apt-get update -qq && apt-get install -y -qq aria2 2>&1 | tail -3
print("  ✅ PyTorch + ComfyUI 依赖安装完成")

# ============================================================
# 第 3 步: 下载 MiniMax H3 越狱文本编码器 (约 14.6 GB)
# ============================================================
print()
print("=" * 60)
print("  第 3 步: 下载 MiniMax H3 越狱文本编码器（14.6 GB）")
print("=" * 60)

text_encoder_dir = "/kaggle/working/ComfyUI/models/clip"
os.makedirs(text_encoder_dir, exist_ok=True)

# MiniMax H3 Uncensored Encoder
print("  正在并行下载 MiniMax H3 越狱文本编码器...")
encoder_url = "https://huggingface.co/datasets/ZeroDegree/MiniMax-H3-Uncensored-Encoder/resolve/main/et_text_encoder_uncensored.safetensors"

!aria2c -x 16 -s 16 -k 1M "{encoder_url}" -d "{text_encoder_dir}" -o "et_text_encoder_uncensored.safetensors"

# 验证文件
import os
encoder_path = f"{text_encoder_dir}/et_text_encoder_uncensored.safetensors"
if os.path.exists(encoder_path):
    size_gb = os.path.getsize(encoder_path) / 1024**3
    print(f"  ✅ 模型下载完成: {size_gb:.2f} GB")
else:
    print("  ❌ 模型下载失败")

# ============================================================
# 第 4 步: 安装 Cloudflared
# ============================================================
print()
print("=" * 60)
print("  第 4 步: 安装 Cloudflared")
print("=" * 60)
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb 2>&1 | tail -3
!cloudflared --version
print("  ✅ Cloudflared 安装完成")

# ============================================================
# 第 5 步: 后台启动 ComfyUI 服务（高显存优化）
# ============================================================
print()
print("=" * 60)
print("  第 5 步: 后台启动 ComfyUI 服务")
print("=" * 60)

# Kaggle T4 32GB 显存优化参数
cmd = "python main.py --listen 127.0.0.1 --port 8188 --gpu-only --highvram --force-fp16"
comfy_process = subprocess.Popen(
    cmd,
    shell=True,
    stdout=open('/tmp/comfyui.log', 'w'),
    stderr=subprocess.STDOUT,
)
print(f"  ComfyUI PID: {comfy_process.pid}")
print("  等待 ComfyUI 完全加载（20 秒）...")

time.sleep(20)

# 验证 ComfyUI 是否启动
ret = os.system("curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8188/")
print(f"  ComfyUI 状态码: {ret} (期望 200)")

# ============================================================
# 第 6 步: 后台启动 Cloudflare Tunnel
# ============================================================
print()
print("=" * 60)
print("  第 6 步: 启动 Cloudflare Tunnel（kaggle.zaikafei.com）")
print("=" * 60)

CF_TOKEN = "***}"

tunnel_cmd = f"cloudflared tunnel --no-autoupdate run --token {CF_TOKEN}"
tunnel_process = subprocess.Popen(
    tunnel_cmd,
    shell=True,
    stdout=open('/tmp/tunnel.log', 'w'),
    stderr=subprocess.STDOUT,
)
print(f"  Tunnel PID: {tunnel_process.pid}")
print("  等待 tunnel 注册（10 秒）...")

time.sleep(10)

# ============================================================
# 部署完成
# ============================================================
print()
print("=" * 60)
print("  👉 部署完成！")
print("=" * 60)
print()
print("  📡 你的专属 URL: https://kaggle.zaikafei.com")
print()
print("  使用步骤：")
print("  1. 浏览器打开 https://kaggle.zaikafei.com")
print("  2. 导入 MiniMax H3 视频生成工作流 JSON")
print("  3. CLIP Loader 节点选 'et_text_encoder_uncensored.safetensors'")
print("  4. 渲染分辨率建议 0.4 Mpx 或 0.5 Mpx（防爆显存）")
print("  5. 初始测试生成 25 帧")
print()
print("  🔧 调试：")
print("  - ComfyUI 日志: !tail -50 /tmp/comfyui.log")
print("  - Tunnel 日志: !tail -30 /tmp/tunnel.log")
print("  - ComfyUI 进程: !ps -ef | grep 'main.py'")
print("  - Tunnel 进程: !ps -ef | grep cloudflared")
print()
print("  ⚠️ Kaggle 免费 GPU 周限制 30 小时，超时自动断")
print("  ⚠️ 不要关闭这个 Cell（关闭后 ComfyUI 会停）")
print("=" * 60)
