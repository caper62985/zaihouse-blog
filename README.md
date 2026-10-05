# zaihouse-blog

在舍博客（blog.zaihouse.com）源码，Astro 静态站。

## 本地开发

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # 输出到 dist/
```

## 线上部署（VPS）

```bash
cd /home/ubuntu/zaihouse-site/blog
git pull
npm install
npm run build
# 重启 serve.cjs（按实际方式：pm2 / systemd）
```

`serve.cjs` 是自带的静态文件服务器，顺带提供 `/api/stats` 浏览量计数。
Telegram 通知走环境变量（`CSZAIHOUSE_BOT_TOKEN` / `TG_BOT_TOKEN` / `TG_CHAT_ID`），不要写进代码。

## 说明

- `public/downloads/*.mp4` 三个演示视频体积大，没有进仓库，部署时从 VPS 原目录保留/复制。
- 文章在 `src/content/blog/*.md`，frontmatter 可选字段：`cover`（封面图路径，不填则按系列自动生成渐变封面）。
