# -*- coding: utf-8 -*-
"""
fix_homepage_dirty_html.py
修复首页 index.html 的脏 HTML 问题：
1. 删除重复的 CSS 块
2. 修复重复 class="..." class="..."
3. 修复多余的 "> (class 属性结尾)
4. 更新文章链接从 pages/blog/xxx.html → /blog/xxx
"""
import re
from pathlib import Path

BASE = Path("d:/网站开发-json")
html = (BASE / "index.html").read_text(encoding="utf-8")

# ─── 1. 删除重复的 CSS 块 ────────────────────────────────
# 第二个 <style> 块（Critical CSS 重复）到 </style>
# 找所有 <style>...</style> 块，保留第一个
css_blocks = list(re.finditer(r'<style[^>]*>(.*?)</style>', html, re.DOTALL))
print(f"Found {len(css_blocks)} <style> blocks")
if len(css_blocks) > 1:
    # 删除第2个及之后的 style 块（从后往前删避免偏移）
    for m in reversed(css_blocks[1:]):
        print(f"  Removing duplicate style block at {m.start()}-{m.end()}")
        html = html[:m.start()] + html[m.end():]

# ─── 2. 修复重复 class 属性 ─────────────────────────────
html = re.sub(r'class="([^"]+)"\s+class="([^"]+)"', r'class="\1 \2"', html)
print("Fixed duplicate class attributes")

# ─── 3. 修复 class="xxx"> 的多余引号 ─────────────────
html = re.sub(r'class="([^"]+)">', r'class="\1">', html)
print("Fixed extra quote in class attributes")

# ─── 4. 更新文章链接 ────────────────────────────────────
# pages/blog/xxx.html → /blog/xxx
def fix_blog_link(m):
    slug = m.group(1)
    return f'/blog/{slug}'

html = re.sub(r'href="pages/blog/([^"]+\.html)"', fix_blog_link, html)
print("Fixed blog article links")

# ─── 5. 更新 Tutorial 链接 ───────────────────────────────
html = re.sub(r'href="pages/blog\.html"', 'href="/blog"', html)
print("Fixed blog index link")

(BASE / "index.html").write_text(html, encoding="utf-8")
print("Done! index.html cleaned up.")
