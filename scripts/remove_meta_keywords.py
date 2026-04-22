# -*- coding: utf-8 -*-
"""
remove_meta_keywords.py
删除所有工具页和首页的 meta keywords 标签（Google 不参考此字段，堆词影响 SEO 评分）
"""
import re
from pathlib import Path

BASE = Path("d:/网站开发-json")

def remove_keywords(html: str) -> str:
    # 删除 <meta name="keywords" ...>
    cleaned = re.sub(r'<meta name="keywords"[^>]+>', '', html)
    # 清理多余空白
    cleaned = re.sub(r'>\s+<meta ', '> <meta ', cleaned)
    return cleaned

# 首页
index = BASE / "index.html"
text = index.read_text(encoding="utf-8")
text = remove_keywords(text)
index.write_text(text, encoding="utf-8")
print("Fixed index.html")

# tools 目录所有工具页
count = 0
for f in sorted((BASE / "tools").glob("*.html")):
    text = f.read_text(encoding="utf-8")
    if 'meta name="keywords"' in text:
        text = remove_keywords(text)
        f.write_text(text, encoding="utf-8")
        count += 1
        print(f"Fixed {f.name}")

# 静态页
for d in ["about", "best-practices", "changelog", "news"]:
    f = BASE / d / "index.html"
    if f.exists():
        text = f.read_text(encoding="utf-8")
        if 'meta name="keywords"' in text:
            text = re.sub(r'<meta name="keywords"[^>]+>', '', text)
            f.write_text(text, encoding="utf-8")
            print(f"Fixed {d}/index.html")

print(f"\nDone! Fixed {count} tool pages + 1 homepage + static pages")
