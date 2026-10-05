// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// https://astro.build/config
// GitHub Pages 预览时 workflow 会传入 PAGES_BASE=/zaihouse-blog/
export default defineConfig({
  site: 'https://blog.zaihouse.com',
  base: process.env.PAGES_BASE || '/',
  integrations: [mdx()],
  build: {
    inlineStylesheets: 'auto',
  },
  vite: {
    build: {
      assetsInlineLimit: 4096,
    },
  },
});