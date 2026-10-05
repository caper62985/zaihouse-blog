---
title: "新人不用手·一键脚本 · VPS 当订阅节点 固定 IP · SOCKS5 / 小火箭 / Clash 三样直接用"
description: "一个 sing-box 一键脚本：VPS 上跑一条命令，直接出 SOCKS5（给指纹浏览器）、VLESS 链接（给小火箭 / V2rayNG）、Clash 订阅链接（给 Clash Verge / Mihomo）。附防火墙设置和故障恢复。"
series: script
date: 2026-10-02
pinned: false
updated: 2026-10-05
readTime: "3 分钟"
tags: ["一键脚本", "VPS", "固定 IP", "开源免费", "科学上网"]
---

# 新人不用手·一键脚本 · VPS 当订阅节点 固定 IP · SOCKS5 / 小火箭 / Clash 三样直接用

> 裸机 VPS → 跑一条命令 → **SOCKS5 + 小火箭链接 + Clash 订阅 + 防火墙全配好**。免费开源，Apache-2.0。

## 🎬 先看视频 · 9 分 28 秒全程实录

<a class="yt-hero-card" href="https://youtu.be/8np_kuR9Kno" target="_blank" rel="noopener">
<span class="yt-hero-card-thumb"><img src="/ppt/yt/8np_kuR9Kno.jpg" width="1280" height="720" alt="一条命令把 VPS 变成订阅节点 SOCKS5 VLESS Clash 三链接直接用 视频封面"></span>
<span class="yt-hero-card-body">
<span class="yt-card-eyebrow">▶️ YouTube · 海外顺</span>
<span class="yt-hero-card-title">新人不用手·一键脚本 | 一条命令把 VPS 变成订阅节点 SOCKS5/VLESS/Clash 三链接直接用</span>
<span class="yt-hero-card-sub">30 秒出三个订阅链接 · RoxyBrowser 实测测试成功 · Clash 订阅一起给你</span>
<span class="yt-hero-card-cta"><span class="yt-play-icon"></span> YouTube 观看完整版</span>
</span>
<span class="yt-hero-card-arrow">→</span>
</a>

ℹ️ <strong>推荐说明</strong>：本文含推荐 / 邀请链接（带 aff 或邀请码）。你通过链接注册时，商家会给本站一份推荐奖励，<strong>但不会向你多收任何一分钱</strong>——你自己注册该拿的优惠和现金奖励照拿不误，价格与你直接去注册完全一样。推荐这些服务是因为我自己就在用，但排序里不排除主观偏好，<strong>请自行比较后再决定</strong>。不用任何链接也一样能注册。

---

## 装完你会拿到三样东西

| | 是什么 | 填到哪 |
| --- | --- | --- |
| **①** | SOCKS5 + 用户名密码 | 指纹浏览器 / AdsPower / Chrome 的「代理」设置 |
| **②** | 一个 `vless://` 链接 | 小火箭 / Shadowrocket / V2rayNG 的「订阅」 |
| **③** | 一个 yaml 订阅地址 | Clash Verge / Mihomo Party 的「订阅」 |

**三样是同一个代理的三个入口，用哪个都行，出口 IP 都是你那台 VPS。**

## 第 1 步 · 买一台美国 VPS

**只记住一条要求：必须是静态 IP。**

🎁 <a href="https://my.racknerd.com/aff.php?aff=21343" target="_blank" rel="noopener">RackNerd 洛杉矶（推荐）</a> —— 几美元/月。

**买完在服务器上跑一句，确认是美国的**：

```bash
curl ipinfo.io
```

**看到 `country: US` 才继续。显示 CN 就换一家。**

## 第 2 步 · 跑脚本

**📦 下载（17 KB）**：

<a href="/downloads/singbox-us-v2.5.zip" download>⬇️ 下载 singbox-us-v2.5.zip</a>

**传上去并安装**（在自己电脑的终端里跑）：

```bash
scp singbox-us-v2.5.zip root@你的VPS公网IP:/root/
ssh root@你的VPS公网IP
cd /root && unzip singbox-us-v2.5.zip && cd singbox-us
bash install-singbox.sh
```

**⚠️ `bash` 不能省** —— 直接 `./install-singbox.sh` 会因没有执行权限报错。

等 1-2 分钟，**跑完会打印三样东西**：

```
① SOCKS5   你的IP:1080   用户 proxyuser  密码 xxxxx
② 链接     vless://xxxx@你的IP:2053?...
③ 链接     http://你的IP:8081/xxxxx.yaml
```

**📌 端口和密码以你实际看到的为准**，别照抄别人的数字。

## 第 3 步 · 三样东西分别怎么填

### ① SOCKS5 → 指纹浏览器 / AdsPower / Chrome

脚本打印的那组，直接填到「代理」设置里：

```
类型          SOCKS5      ← 别选 HTTP，也别留空
主机 / IP     你的 VPS 公网 IP
端口          脚本给你的实际端口
用户名        脚本给你的用户名
密码          脚本给你的密码
```

**AdsPower 填法**：账号管理 → 新增浏览器 → 代理类型选 `SOCKS5` → 填上面四项 → 代理检测选「美国」。

**Chrome 填法**：设置 → 系统 → 打开代理设置 → 手动代理 → SOCKS5 + 主机端口 + 用户名密码。

**填完先测一下**：把这个 IP 填进代理检测，**显示 US 才往下走**。

### ② 链接 → 小火箭 / Shadowrocket / V2rayNG

先把链接取出来：

```bash
cat /root/singbox-subscription.txt
```

复制这一行，粘到客户端里：

| 客户端 | 怎么粘 |
| --- | --- |
| Shadowrocket（iOS） | 首页右上「+」→ 类型选 Subscribe → 粘贴 |
| V2rayNG（Android） | 右上「+」→ 订阅组导入 → 粘贴 |

**换设备不用重装** —— 在新设备上再跑一次 `cat /root/singbox-subscription.txt`，粘同一行就行。

### ③ 链接 → Clash Verge / Mihomo Party

脚本打印的 `http://你的IP:8081/xxxxx.yaml`：

**订阅 → 新建 → 粘贴这个地址 → 导入。**

**⚠️ 别把 ② 那个 base64 粘给 Clash** —— 它的「订阅」只认 URL，粘 base64 会报格式错。

**⚠️ 导入完把这个服务关掉**：

```bash
systemctl stop singbox-clash-sub && systemctl disable singbox-clash-sub
```

**这个地址等于你的代理密码** —— 谁拿到都能用你的代理。关掉之后 Clash 里已导入的配置照样能用，只是不再自动更新。

**不想要这个地址**（不想多开一个端口）：

```bash
ENABLE_CLASH_SUB=0 bash install-singbox.sh
```

## 第 4 步 · 验证

**开代理后浏览器访问**：

```
https://ipinfo.io
```

**显示的 IP 跟你 VPS 的公网 IP 一样 = 成功。**

**隔几天再查一次，IP 一样就是真固定。**

---

## 常见问题

**Q：脚本跑一半没输出就退出了？**
会直接告诉你「第 N 行执行失败（退出码 X）」，把那几行发出来就行。

**Q：提示端口被占用？**
先看是谁：
```bash
ss -tulnp | grep 1080
```
**如果显示的不是 `sing-box`（很多 VPS 商家会预装 mihomo），别乱杀** —— 换个端口重装：
```bash
SOCKS_PORT=1081 bash install-singbox.sh
```

**Q：SOCKS5 连不上？**
```
① 端口对不对（用脚本打印的那个）
② 类型选的是不是 SOCKS5
③ 本机梯子关了没 ← 最常见的一条
④ 防火墙放行了没
```

**Q：防火墙改崩了连不上 SSH？**
```bash
bash FIREWALL-RESCUE.sh
```
**包里的救场脚本。**

**Q：想换端口？**
```bash
SOCKS_PORT=7890 bash install-singbox.sh
```

**Q：重启 VPS 后还有效吗？**
**服务设了自启，重启后自动恢复。** 但**如果你的 IP 是 DHCP 分配的，重启后公网 IP 会变，链接就失效了** —— 这就是第 1 步要静态 IP 的原因。

**Q：不用了怎么删干净？**
```bash
bash uninstall-singbox.sh
```

---

## 几条硬提醒

🔴 **③ 那个订阅地址 = 你的代理密码。** **录视频、分享屏幕之前先关掉它**（命令在第 3 步里）。

🔴 **凭据别贴到聊天窗口或群里。** 全部参数在：
```bash
cat /root/singbox-credentials.txt     # 权限 600
```

🔴 **指纹浏览器里的时区 / 语言要跟 IP 对上。** 挂着美国 IP 但时区显示东八区，某些平台的反作弊会直接判异常。

🔴 **别在代理开着时登录重要账号。** 建议先正常用几天再注册。

---

## 原理 · 为什么是这三样东西

**这一节是给你看完步骤之后想理解原理用的，跳过也不影响操作。**

### 为什么非要静态 IP

因为**所有客户端的「订阅」本质是一串含 IP 的链接**。IP 一变，链接就指向别的地方了。

```
DHCP 分配的 VPS 重启 → 换了 IP → 链接失效 → 机场节点也可能随时跑路
静态 IP 的 VPS      → 永远是你那个 IP → 链接一直有效
```

### 为什么机场的「美国节点」不能用来注册

**IP 检测的是归属地，不是流量在哪个机房。**

我实测踩过：有的机场「美国 01/02/03」出口 IP 在 IP 库里登记在**中国** —— 哪怕 Cloudflare 显示 `LAX`，注册照样被拒。**认准 VPS，查 `ipinfo.io` 显示 `US`。**

### 为什么 SOCKS5 和 VLESS 是两回事

```
SOCKS5   一个「代理协议」，要手填 IP/端口/用户/密码
         简单，但公网上是明文，公共 WiFi 下慎用
         ✅ 指纹浏览器、AdsPower、Chrome 都能直接填

VLESS    一个「代理协议 + 伪装 TLS」，用链接导入
         抗干扰更好、UDP 更稳（视频、语音、游戏都靠它）
         ✅ 小火箭、Shadowrocket、V2rayNG、Clash 都支持
```

**简单选：只要填代理就用 SOCKS5；要全局、想连手机就用 VLESS 链接。**

### Clash 为什么必须给一个 URL 而不是链接

**Clash Verge / Mihomo Party 的「订阅」要的是一个能拉取的地址**，不支持直接粘 `vless://`。所以脚本在服务器上开了个小 HTTP 服务，返回一份 YAML。

**所以那个地址本身是有价值的凭据** —— 这就是为什么提醒你用完关掉。

### 什么叫「套娃」

**你自己电脑上已经开着梯子（或 Clash）时，再去连 VPS，那条连接会先被你自己的代理接管，绕一圈才连回来** —— 结果就是超时 / 代理失败。

**解法两选一**：

```
① 填 SOCKS5 之前，先关掉本机梯子     ← 最简单
② Clash 配置里加一条直连规则（脚本已经加好，你不用管）
   - IP-CIDR,你的VPS公网IP/32,DIRECT
```

### 指纹浏览器为什么必要

**很多平台的风控不看你在哪个国家，看你是不是「一个真人」。**

指纹浏览器会伪装浏览器指纹（WebRTC、时区、语言、TLS 指纹），**一个环境 = 一套独立身份**，用于跨境多账号、AI 工具批量注册、独立站和电商后台。

**实测可用的两款**（免费版就够用）：

- 🎁 **Roxybrowser**：<a href="https://roxybrowser.cn/invite/T73jtz" target="_blank" rel="noopener">Roxybrowser 注册</a>
- 🎁 **AdsPower**：<a href="https://www.adspower.net/share/U00Khq" target="_blank" rel="noopener">AdsPower 注册</a>（功能更全，付费档位多）

### 这台 VPS 拿来日常用 Muse AI

**Meta 刚发的个人 AI 智能体 Muse。** 注意这两件事是分开的：

```
注册 Muse    → 不用 VPS，走云浏览器 + 平台代理
日常用 Muse  → 挂这台美国 VPS，保持美国固定 IP
```

**⚠️ 别拿这台 VPS 去注册** —— 实测过，用美国 VPS 挂指纹浏览器注册一样被拒，**问题在浏览器环境，不在 IP**。

**注册具体怎么过，下期出教程。** 这篇先把「日常用哪台 VPS」说清楚：就是你手上这台，不用多花钱。

---

## 相关教程

[4 个一键脚本（裸机 → OpenClaw → 公网 → 独立站）](/posts/openclaw-30min-guide/) · [WordPress 独立站一键安装模板包](/posts/zaihouse-template-99/) · [新人注册优惠大全](/posts/newbie-rewards-2026/) · [0 元白嫖 AI 生图（Kaggle 免费 GPU）](/posts/kaggle-comfyui-free-guide/)
