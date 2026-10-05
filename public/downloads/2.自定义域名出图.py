import os
import shutil
import subprocess
import time
import urllib.request

# ==========================================
# 1. 彻底清空旧环境（干净重来）
# ==========================================
print("🧹 1/5 正在彻底清空旧环境...")
if os.path.exists("/kaggle/working/ComfyUI"):
    shutil.rmtree("/kaggle/working/ComfyUI")
    print("   ↳ 已清理 ComfyUI 旧目录")

%cd /kaggle/working

# ==========================================
# 2. 克隆 ComfyUI & GGUF 节点
# ==========================================
print("📦 2/5 正在克隆 ComfyUI 及 GGUF 插件...")
!git clone https://github.com/comfyanonymous/ComfyUI.git

%cd /kaggle/working/ComfyUI/custom_nodes
!git clone https://github.com/city96/ComfyUI-GGUF

%cd /kaggle/working/ComfyUI

# ==========================================
# 3. 安装依赖包
# ==========================================
print("⚡ 3/5 正在安装 Python 环境与图像处理依赖...")
!pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
!pip install -q -r requirements.txt
!pip install -q einops transformers accelerate safetensors imageio-ffmpeg gguf sentencepiece

# 安装 Cloudflare 穿透工具
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb > /dev/null 2>&1

# ==========================================
# 4. 下载全套 FLUX.1 模型 (包含 ModelScope 稳定 VAE)
# ==========================================
print("📥 4/5 正在一键下载全套 FLUX.1 模型...")

unet_dir = "/kaggle/working/ComfyUI/models/unet"
clip_dir = "/kaggle/working/ComfyUI/models/clip"
vae_dir = "/kaggle/working/ComfyUI/models/vae"

for d in [unet_dir, clip_dir, vae_dir]:
    os.makedirs(d, exist_ok=True)

# 1. GGUF 主模型 (~6.3GB)
print("   ↳ 1/3 下载 FLUX.1 Schnell GGUF 主模型...")
!wget -c -L "https://huggingface.co/city96/FLUX.1-schnell-gguf/resolve/main/flux1-schnell-Q4_K_S.gguf" -O "{unet_dir}/flux1-schnell-Q4_K_S.gguf"

# 2. 文本编码器 (~4.6GB + 240MB)
print("   ↳ 2/3 下载 T5xxl & CLIP_L 文本编码器...")
!wget -c -L "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors" -O "{clip_dir}/t5xxl_fp8_e4m3fn.safetensors"
!wget -c -L "https://hf-mirror.com/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors" -O "{clip_dir}/clip_l.safetensors"

# 3. ModelScope 稳定原生 VAE (335MB)
print("   ↳ 3/3 从 ModelScope 下载 FLUX 原生 VAE...")
!wget -c "https://modelscope.cn/models/AI-ModelScope/FLUX.1-schnell/resolve/master/ae.safetensors" -O "{vae_dir}/ae.safetensors"

# 校验 VAE 完整性
if os.path.exists(f"{vae_dir}/ae.safetensors") and os.path.getsize(f"{vae_dir}/ae.safetensors") > 300000000:
    print("\n✅ 所有模型（包含 VAE）全套下载完成且完整无损！")
else:
    raise RuntimeError("❌ VAE 下载有误，请重新运行！")

# ==========================================
# 5. 启动 ComfyUI 与 Cloudflare 穿透
# ==========================================
print("🚀 5/5 正在启动 ComfyUI...")
log_file = open("comfyui.log", "w")
cmd = "python main.py --listen 0.0.0.0 --port 8188 --gpu-only"
subprocess.Popen(cmd, shell=True, stdout=log_file, stderr=log_file)

time.sleep(10)

MY_CF_TOKEN = "eyJhIjoiYWE0ZGE1MzE3OTk5NTI5NWI3YjVjMTI3MmVhZDYxNzUiLCJ0IjoiNTUxMDQ2YzAtM2MzNS00Y2MzLWJiMjEtOWZjNWFlMDk2YzE5IiwicyI6Ik16VTRNV1ZsWkdVdE16YzNNUzAwTldZd0xXRm1ZalV0WVdJMk5qWmlaR05rTVRrMiJ9"

print("\n" + "=" * 60)
print(f"👉 启动成功！请访问你的自定义域名: https://kaggle.zaihouse.cc.cd")
print("=" * 60 + "\n")

!cloudflared tunnel --no-autoupdate --protocol http2 run --token {MY_CF_TOKEN}