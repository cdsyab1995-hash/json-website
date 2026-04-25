# Tool Blog Daily - 执行记录

## 概要
每天 09:00 自动执行，生成工具相关的 SEO 博客文章。

## 执行记录

| 日期 | 目标工具 | 主题 | 状态 |
|------|----------|------|------|
| 2026-04-22 09:00 | viewer | json-viewer-tree-view-why-you-need-one | SKIP (文章已存在) |
| 2026-04-21 08:57 | compare | compare-json-documents-find-differences | SKIP (文章已存在) |
| 2026-04-21 08:59 | compare | compare-json-documents-find-differences | SKIP (文章已存在) |

## 最新执行 (2026-04-22 09:00)
- 状态：SKIP - 文章 json-viewer-tree-view-why-you-need-one 已存在
- 脚本路径：d:\网站开发-json\scripts\daily_tool_blog.py
- 说明：viewer 工具文章已由之前执行生成，脚本跳过

## 执行记录 (2026-04-23 08:57)
- 状态：SUCCESS
- 脚本：write_articles.py（注意：daily_tool_blog.py 不存在，使用此脚本替代）
- 生成文章：
  - json-patch-vs-merge-patch.html
  - curl-json-api-guide.html
- 修复：调整 BLOG_DIR 路径从 pages\blog → blog

## 执行记录 (2026-04-25 15:45)
- 状态：SUCCESS
- 脚本：daily_blog.py（daily_tool_blog.py 不存在，使用此替代）
- 生成文章：json-performance-optimization-2026
- 主题：JSON Performance Optimization: 12 Techniques for Faster Parsing in 2026
- 推送：已推送到 GitHub
