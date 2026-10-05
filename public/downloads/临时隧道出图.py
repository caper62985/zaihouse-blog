import os
import shutil
import subprocess
import time
import urllib.request
import re

# ==========================================
# 1. 彻底清空旧环境
# ==========================================
print("🧹 1/5 正在彻底清空旧环境...")
if os.path.exists("/kaggle/working/ComfyUI"):
    shutil.rmtree("/kaggle/working/ComfyUI")

%cd /kaggle/working

# ==========================================
# 2. 克隆 ComfyUI & GGUF 插件
# ==========================================
print("📦 2/5 克隆 ComfyUI 与 GGUF 插件...")
!git clone https://github.com/comfyanonymous/ComfyUI.git

%cd /kaggle/working/ComfyUI/custom_nodes
!git clone https://github.com/city96/ComfyUI-GGUF

%cd /kaggle/working/ComfyUI

# ==========================================
# 3. 安装依赖包
# ==========================================
print("⚡ 3/5 安装 Python 环境与依赖...")
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
!pip install -q -r requirements.txt
!pip install -q einops transformers accelerate safetensors imageio-ffmpeg gguf sentencepiece

# 下载穿透工具 (无需配置 Token)
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb > /dev/null 2>&1

# ==========================================
# 4. 一键下载全套 FLUX.1 模型
# ==========================================
print("📥 4/5 一键下载全套 FLUX.1 模型...")

unet_dir = "/kaggle/working/ComfyUI/models/unet"
clip_dir = "/kaggle/working/ComfyUI/models/clip"
vae_dir = "/kaggle/working/ComfyUI/models/vae"

for d in [unet_dir, clip_dir, vae_dir]:
    os.makedirs(d, exist_ok=True)

# 1. GGUF 主模型
!wget -c -L "https://huggingface.co/city96/FLUX.1-schnell-gguf/resolve/main/flux1-schnell-Q4_K_S.gguf" -O "{unet_dir}/flux1-schnell-Q4_K_S.gguf"

# 2. 文本编码器
!wget -c -L "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors" -O "{clip_dir}/t5xxl_fp8_e4m3fn.safetensors"
!wget -c -L "https://hf-mirror.com/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors" -O "{clip_dir}/clip_l.safetensors"

# 3. ModelScope 稳定原生 VAE
!wget -c "https://modelscope.cn/models/AI-ModelScope/FLUX.1-schnell/resolve/master/ae.safetensors" -O "{vae_dir}/ae.safetensors"

print("\n✅ 所有模型（包含 VAE）下载完成！")

# ==========================================
# 5. 启动 ComfyUI 与 免注册临时隧道
# ==========================================
print("🚀 5/5 启动 ComfyUI...")
log_file = open("comfyui.log", "w")
cmd = "python main.py --listen 0.0.0.0 --port 8188 --gpu-only"
subprocess.Popen(cmd, shell=True, stdout=log_file, stderr=log_file)

time.sleep(15)

# 启动临时隧道 (不带 --token 节点，完全免注册)
print("\n" + "=" * 60)
print("🔗 正在生成免注册临时访问链接，请稍候...")
print("=" * 60)

tunnel_process = subprocess.Popen(
    "cloudflared tunnel --url http://127.0.0.1:8188",
    shell=True,
    stderr=subprocess.PIPE,
    text=True
)

# 实时抓取生成的 trycloudflare 临时网址
while True:
    line = tunnel_process.stderr.readline()
    if not line:
        break
    if "trycloudflare.com" in line:
        match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
        if match:
            url = match.group(0)
            print("\n" + "🎉" * 20)
            print(f"👉 临时生图网址: {url}")
            print("🎉" * 20 + "\n")
            break