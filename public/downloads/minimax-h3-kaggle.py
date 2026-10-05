import os
import shutil
import subprocess
import time
import re

# ==========================================
# MiniMax-H3 生视频 · Kaggle 免费 GPU
#
# 关键点：模型 29.82 GiB，Kaggle 自带磁盘只有 19.5 GB，
# 装不下。所以走 Kaggle Datasets 挂载 —— 把模型先传成自己的
# Dataset（不占 Notebook 磁盘），运行时挂到 /kaggle/input 读。
#
# 用法：
#   1. 新建一个 Private Dataset，把 5 个模型文件传进去（名字见 FILES）
#   2. 新建 Notebook → 添加你的 Dataset → Accelerator 选 GPU T4×2、Internet On
#   3. 把本脚本整个粘进一个 Cell，Run All
#
# 不花钱：Kaggle 免费 30 小时/周 GPU，Dataset 存储也不收费。
# ==========================================

# ---------- 需要改成你自己的 ----------
MY_DATASET = "你的用户名/minimax-h3-models"
# --------------------------------------

DATASET_DIR = f"/kaggle/input/{MY_DATASET.split('/')[-1]}"

# 5 个文件（名字必须和 Dataset 里一致）
FILES = {
    "unet":  "MiniMax-H3-Ref2VA-Pruned-Q4_K_M.gguf",                 # 10.77 GiB
    "clip":  "Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-IQ4_XS.gguf",  # 12.52 GiB
    "mmproj":"Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-mmproj-BF16.gguf",  # 1.12 GiB
    "video_vae": "minimax_h3_video_vae_fp16.safetensors",           # 4.85 GiB
    "audio_vae": "minimax_h3_audio_vae_fp32.safetensors",           # 0.56 GiB
}

# 找不到时的兜底：直接从 huggingface 拉（不用 Dataset，但会占磁盘）
HF_FALLBACK = {
    "unet":  "https://huggingface.co/Abiray/MiniMax-H3-Pruned-GGUF/resolve/main/MiniMax-H3-Ref2VA-Pruned-Q4_K_M.gguf",
    "clip":  "https://huggingface.co/nif0/Qwen3-VL-32B-Instruct-MiniMax-H3-GGUF/resolve/main/Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-IQ4_XS.gguf",
    "mmproj":"https://huggingface.co/nif0/Qwen3-VL-32B-Instruct-MiniMax-H3-GGUF/resolve/main/Qwen3-VL-32B-Instruct-MiniMax-H3-L0-49-mmproj-BF16.gguf",
    "video_vae": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors",
    "audio_vae": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors",
}

# ==========================================
# 1. 清空旧环境
# ==========================================
print("🧹 1/6 正在清空旧环境...")
if os.path.exists("/kaggle/working/ComfyUI"):
    shutil.rmtree("/kaggle/working/ComfyUI")
os.makedirs("/kaggle/working", exist_ok=True)

# ==========================================
# 2. 克隆 ComfyUI 与 GGUF 插件
# ==========================================
print("📦 2/6 克隆 ComfyUI 与 GGUF 插件...")
subprocess.run("git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git",
               shell=True, cwd="/kaggle/working")
# GGUF 加载器：跑 .gguf 主模型必需
subprocess.run("git clone --depth 1 https://github.com/city96/ComfyUI-GGUF",
               shell=True, cwd="/kaggle/working/ComfyUI/custom_nodes")

# ---------- 这里换成你自己的节点仓库 ----------
# H3 节点由你自己装，示例：
# subprocess.run("git clone --depth 1 <你的节点仓库>",
#                shell=True, cwd="/kaggle/working/ComfyUI/custom_nodes")
# ----------------------------------------------------

# ==========================================
# 3. 安装依赖
# ==========================================
print("⚡ 3/6 安装依赖...")
subprocess.run("pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121",
               shell=True)
subprocess.run("pip install -q -r /kaggle/working/ComfyUI/requirements.txt", shell=True)
subprocess.run("pip install -q einops transformers accelerate safetensors imageio-ffmpeg gguf sentencepiece av",
               shell=True)

# 隧道工具（拿 ComfyUI 的公网地址）
subprocess.run("wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb",
               shell=True)
subprocess.run("dpkg -i cloudflared-linux-amd64.deb", shell=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# ==========================================
# 4. 挂载模型（核心：绕开 19.5 GB 磁盘限制）
# ==========================================
print("💾 4/6 挂载 MiniMax-H3 模型...")
C = "/kaggle/working/ComfyUI"
os.makedirs(f"{C}/models/unet", exist_ok=True)
os.makedirs(f"{C}/models/clip", exist_ok=True)
os.makedirs(f"{C}/models/vae", exist_ok=True)

def find_in_dataset(fname):
    """在挂载的 Dataset 里找文件（Kaggle 会在子目录里平铺）"""
    if not os.path.isdir(DATASET_DIR):
        return None
    for root, _, files in os.walk(DATASET_DIR):
        if fname in files:
            return os.path.join(root, fname)
    return None

for key, fname in FILES.items():
    src = find_in_dataset(fname)
    if src:
        # 用软链接而不是复制 —— 复制会占 Notebook 磁盘（就是我们要避开的）
        dst_dir = {"unet": "unet", "clip": "clip", "mmproj": "clip",
                   "video_vae": "vae", "audio_vae": "vae"}[key]
        dst = f"{C}/models/{dst_dir}/{fname}"
        if os.path.lexists(dst):
            os.remove(dst)
        os.symlink(src, dst)
        gb = os.path.getsize(src) / 1024**3
        print(f"  ✅ {fname}  ({gb:.2f} GiB) ← 来自 Dataset")
    else:
        # 没挂到就退回直接下载（会吃磁盘，慢但能跑）
        url = HF_FALLBACK[key]
        dst_dir = {"unet": "unet", "clip": "clip", "mmproj": "clip",
                   "video_vae": "vae", "audio_vae": "vae"}[key]
        dst = f"{C}/models/{dst_dir}/{fname}"
        print(f"  ⚠️  {fname} 不在 Dataset，回退到直接下载（吃磁盘）...")
        subprocess.run(f'wget -c -L "{url}" -O "{dst}"', shell=True)

# ==========================================
# 5. 启动 ComfyUI
# ==========================================
print("🚀 5/6 启动 ComfyUI...")
log_file = open("/kaggle/working/comfyui.log", "w")
subprocess.Popen(
    "python main.py --listen 0.0.0.0 --port 8188",
    shell=True, cwd=C, stdout=log_file, stderr=log_file
)
time.sleep(20)

# ==========================================
# 6. 开临时隧道，拿公网地址
# ==========================================
print("\n" + "=" * 60)
print("🔗 正在生成访问链接，请稍候...")
print("=" * 60)

tunnel = subprocess.Popen(
    "cloudflared tunnel --url http://127.0.0.1:8188",
    shell=True, stderr=subprocess.PIPE, text=True
)

while True:
    line = tunnel.stderr.readline()
    if not line:
        break
    if "trycloudflare.com" in line:
        m = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
        if m:
            print("\n" + "🎉" * 20)
            print(f"👉 ComfyUI 地址: {m.group(0)}")
            print("🎉" * 20 + "\n")
            break
