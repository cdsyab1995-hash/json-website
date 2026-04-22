# -*- coding: utf-8 -*-
"""
remove_meta_keywords.py
删除所有页面的 meta keywords 标签
"""
import re
from pathlib import Path

BASE = Path("d:/网站开发-json")
count = 0

def remove_keywords(text):
    return re.sub(r'<meta name="keywords"[^>]+>', '', text)

# 首页
f = BASE / "index.html"
if f.exists() and 'meta name="keywords"' in f.read_text(encoding="utf-8"):
    text = remove_keywords(f.read_text(encoding="utf-8"))
    f.write_text(text, encoding="utf-8")
    print(f"Fixed index.html")
    count += 1

# tools 目录
for f in sorted((BASE / "tools").glob("*.html")):
    text = f.read_text(encoding="utf-8")
    if 'meta name="keywords"' in text:
        text = remove_keywords(text)
        f.write_text(text, encoding="utf-8")
        print(f"Fixed tools/{f.name}")
        count += 1

# 静态页
for d in ["about", "best-practices", "changelog", "blog", "news"]:
    f = BASE / d / "index.html"
    if f.exists() and 'meta name="keywords"' in f.read_text(encoding="utf-8"):
        text = remove_keywords(f.read_text(encoding="utf-8"))
        f.write_text(text, encoding="utf-8")
        print(f"Fixed {d}/index.html")
        count += 1

# 博客文章
for subdir in (BASE / "blog").iterdir():
    if subdir.is_dir():
        f = subdir / "index.html"
        if f.exists() and 'meta name="keywords"' in f.read_text(encoding="utf-8"):
            text = remove_keywords(f.read_text(encoding="utf-8"))
            f.write_text(text, encoding="utf-8")
            print(f"Fixed blog/{subdir.name}/index.html")
            count += 1

# 新闻文章
for subdir in (BASE / "news").iterdir():
    if subdir.is_dir():
        f = subdir / "index.html"
        if f.exists() and 'meta name="keywords"' in f.read_text(encoding="utf-8"):
            text = remove_keywords(f.read_text(encoding="utf-8"))
            f.write_text(text, encoding="utf-8")
            print(f"Fixed news/{subdir.name}/index.html")
            count += 1

print(f"\nDone! Removed meta keywords from {count} pages")
