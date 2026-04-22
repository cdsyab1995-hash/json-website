# -*- coding: utf-8 -*-
"""
fix_article_dates.py
修复所有博客/新闻文章页的 JSON-LD datePublished/dateModified
通过读取 article:published_time meta 标签获取真实日期。
"""
import re
from pathlib import Path

BASE = Path("d:/网站开发-json")

def get_article_date(html: str) -> str:
    """从页面提取真实发布日期"""
    # 优先从 meta article:published_time 提取
    m = re.search(r'<meta property="article:published_time" content="(\d{4}-\d{2}-\d{2})"', html)
    if m:
        return m.group(1)
    # 其次从 visible "Published: YYYY-MM-DD" 提取
    m = re.search(r'Published:\s*(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    return "2026-04-22"  # fallback

def fix_article_dates(article_dir: Path, label: str):
    fixed = 0
    for subdir in sorted(article_dir.iterdir()):
        if not subdir.is_dir():
            continue
        index = subdir / "index.html"
        if not index.exists():
            continue

        html = index.read_text(encoding="utf-8")
        pub_date = get_article_date(html)

        # 检查 JSON-LD 里的日期
        ld_dates = re.findall(r'"datePublished":\s*"([^"]+)"', html)
        if not ld_dates:
            print(f"  WARN: No datePublished in {label}/{subdir.name}")
            continue

        current = ld_dates[0]
        if current == pub_date:
            print(f"  OK:   {label}/{subdir.name} = {pub_date}")
            continue

        # 更新 JSON-LD
        html = re.sub(r'"datePublished":\s*"[^"]+"', f'"datePublished": "{pub_date}"', html)
        html = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{pub_date}"', html)

        # 更新 article:published_time meta
        html = re.sub(
            r'<meta property="article:published_time" content="[^"]+"',
            f'<meta property="article:published_time" content="{pub_date}"',
            html
        )

        index.write_text(html, encoding="utf-8")
        print(f"  FIX:  {label}/{subdir.name}: {current} → {pub_date}")
        fixed += 1

    return fixed

print("=== Fixing blog article dates ===")
b = fix_article_dates(BASE / "blog", "blog")
print(f"  {b} blog articles fixed")

print("\n=== Fixing news article dates ===")
n = fix_article_dates(BASE / "news", "news")
print(f"  {n} news articles fixed")

print(f"\nTotal: {b + n} articles fixed")
