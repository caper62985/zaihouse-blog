import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    // 所属系列（2026-10-04 新增）。首页左侧分类栏按它筛选。
    //   free    0 元白嫖
    //   starter 0 基础小白
    //   script  一键脚本
    series: z.enum(['free', 'starter', 'script']).optional(),
    // 最后修改时间。首页排序优先用它（倒叙），没填的回落到 date。
    // 目的：改过内容的旧帖应该排到前面，而不是永远钉在最初发布的位置。
    updated: z.coerce.date().optional(),
    readTime: z.string().optional(),
    tags: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
    pinned: z.boolean().default(false),
    // 置顶内部的手动顺序（数字小的排前面）。不填则按 999 处理，
    // 排到所有填了 pinOrder 的置顶帖之后。首页排序用，见 src/pages/index.astro。
    pinOrder: z.number().optional(),
    // 封面图（可选），如 cover: /ppt/cover.png。不填则首页卡片用系列渐变封面兜底。
    cover: z.string().optional(),
  }),
});

export const collections = { blog };