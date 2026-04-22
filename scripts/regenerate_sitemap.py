# -*- coding: utf-8 -*-
"""
regenerate_sitemap.py
根据当前文件结构，重新生成 sitemap.xml
新 URL 结构：
  /                           ← 首页
  /about                      ← 关于
  /changelog                  ← 更新日志
  /best-practices             ← 最佳实践
  /privacy                    ← 隐私政策
  /terms                      ← 服务条款
  /cookie                     ← Cookie 政策
  /blog                       ← 博客列表
  /blog/<slug>                ← 博客文章（16篇）
  /news                       ← 新闻列表
  /news/<slug>                ← 新闻文章（12篇）
  /tools/json-formatter 等     ← 工具页（24个）
"""

import re
from pathlib import Path
from datetime import date

BASE = Path("d:/网站开发-json")
TODAY = date.today().isoformat()

# ─── 工具列表 ────────────────────────────────────────────────
TOOLS = [
    ("json-formatter",    "JSON Formatter",    "0.9"),
    ("json-escape",       "JSON Escape",       "0.8"),
    ("json-extract",      "JSON Extract",      "0.8"),
    ("json-sort",         "JSON Sort",         "0.8"),
    ("json-clean",        "JSON Clean",        "0.8"),
    ("json-to-xml",       "JSON to XML",      "0.8"),
    ("json-to-yaml",      "JSON to YAML",     "0.8"),
    ("json-viewer",       "JSON Viewer",       "0.9"),
    ("json-to-csv",       "JSON to CSV",      "0.9"),
    ("json-compare",      "JSON Compare",      "0.9"),
    ("csv-to-excel",      "CSV to Excel",     "0.7"),
    ("merge-csv",         "Merge CSV",        "0.7"),
    ("excel-remove-duplicates", "Excel Remove Duplicates", "0.7"),
    ("css-minifier",      "CSS Minifier",     "0.7"),
    ("html-encoder",      "HTML Encoder",     "0.7"),
    ("url-encoder",       "URL Encoder",      "0.7"),
    ("base64",            "Base64",           "0.8"),
    ("jwt-decoder",       "JWT Decoder",      "0.8"),
    ("regex-tester",      "Regex Tester",     "0.7"),
    ("uuid-generator",    "UUID Generator",   "0.7"),
    ("timestamp-converter", "Timestamp Converter", "0.7"),
    ("hash-generator",    "Hash Generator",   "0.7"),
    ("pdf-split",         "PDF Split",        "0.6"),
    ("batch-renamer",     "Batch Renamer",    "0.6"),
]

# ─── 博客文章 slug ───────────────────────────────────────────
BLOG_SLUGS = sorted([
    "ai-tool-calling-mcp-2026",
    "compare-json-documents-find-differences",
    "curl-json-api-guide",
    "json-api-error-handling-2026",
    "json-edge-computing-cloudflare-workers",
    "json-parsing-performance-comparison",
    "json-patch-vs-merge-patch",
    "json-schema-complete-guide-2026",
    "json-viewer-tree-view-why-you-need-one",
    "jwt-security-best-practices-2026",
    "mcp-json-standardizing-ai-tools",
    "model-context-protocol-json-rpc-ai-tools",
    "postgresql-jsonb-vs-mongodb-document-store",
    "rfc9457-problem-details-json-api-errors",
    "sort-json-arrays-objects-guide",
    "zod-json-schema-validation-ai",
])

# ─── 新闻 slug ───────────────────────────────────────────────
NEWS_SLUGS = sorted([
    "api-transformations-2026",
    "browser-devtools-json-schema",
    "bun-2-json-serialization",
    "cursor-vscode-json-lint-ai",
    "json-schema-to-typescript-v6",
    "json-schema-w3c-recommendation",
    "json-streaming-api-browser",
    "jsonata-2-ai-query",
    "mcp-10000-servers",
    "nextjs-16-json-streaming",
    "nodejs-24-json-schema",
    "zod-v4-5m-downloads",
])

def entry(loc, lastmod=TODAY, changefreq="weekly", priority="0.8"):
    return f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>{changefreq}</changefreq>\n    <priority>{priority}</priority>\n  </url>"

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

# 首页
lines.append(entry("https://www.aijsons.com/", TODAY, "daily", "1.0"))

# 静态页
STATIC = [
    ("https://www.aijsons.com/about",             "monthly", "0.8"),
    ("https://www.aijsons.com/blog",              "weekly",  "0.9"),
    ("https://www.aijsons.com/news",              "daily",   "0.9"),
    ("https://www.aijsons.com/best-practices",    "weekly",  "0.8"),
    ("https://www.aijsons.com/changelog",         "weekly",  "0.6"),
    ("https://www.aijsons.com/privacy",           "monthly", "0.5"),
    ("https://www.aijsons.com/terms",             "monthly", "0.5"),
    ("https://www.aijsons.com/cookie",             "monthly", "0.4"),
]
for loc, freq, pri in STATIC:
    lines.append(entry(loc, TODAY, freq, pri))

# 工具页
for slug, name, pri in TOOLS:
    loc = f"https://www.aijsons.com/tools/{slug}"
    lines.append(entry(loc, TODAY, "weekly", pri))

# 博客文章
for slug in BLOG_SLUGS:
    loc = f"https://www.aijsons.com/blog/{slug}"
    lines.append(entry(loc, TODAY, "weekly", "0.8"))

# 新闻文章
for slug in NEWS_SLUGS:
    loc = f"https://www.aijsons.com/news/{slug}"
    lines.append(entry(loc, TODAY, "daily", "0.7"))

lines.append("</urlset>")

sitemap = "\n".join(lines) + "\n"
(BASE / "sitemap.xml").write_text(sitemap, encoding="utf-8")

total = 1 + len(STATIC) + len(TOOLS) + len(BLOG_SLUGS) + len(NEWS_SLUGS)
print(f"Done! Generated sitemap with {total} URLs:")
print(f"  - Static pages: {len(STATIC)}")
print(f"  - Tool pages: {len(TOOLS)}")
print(f"  - Blog articles: {len(BLOG_SLUGS)}")
print(f"  - News articles: {len(NEWS_SLUGS)}")
