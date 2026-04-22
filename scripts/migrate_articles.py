# -*- coding: utf-8 -*-
"""
migrate_articles.py
将 pages/blog/*.html 和 pages/news/*.html 迁移到
  blog/<slug>/index.html  和  news/<slug>/index.html
同时修复所有内部链接为绝对路径。
"""

import re
import shutil
from pathlib import Path

BASE = Path("d:/网站开发-json")

# ─── 路径替换规则 ──────────────────────────────────────────────
# 文章在 pages/blog/ 层级时，相对路径规则：
#   ../../xxx  →  /xxx   (css/styles.css, js/app.js, images/xxx)
#   index.html →  /blog
#   对方文章.html → /blog/对方文章

def fix_blog_article(slug: str, content: str) -> str:
    """修复 blog 文章中的相对链接"""

    # 1. canonical / og:url：更新到新地址
    content = re.sub(
        r'(href|content)="https://www\.aijsons\.com/pages/blog/' + re.escape(slug) + r'\.html"',
        lambda m: f'{m.group(1)}="https://www.aijsons.com/blog/{slug}"',
        content
    )

    # 2. ../../css/ ../../js/ ../../images/ => 绝对路径
    content = re.sub(r'(\.\./){2}(css|js|images)/', r'/\2/', content)

    # 3. ../../pages/format.html => /tools/json-formatter  等工具页
    TOOL_MAP = {
        "format.html": "json-formatter",
        "escape.html": "json-escape",
        "extract.html": "json-extract",
        "sort.html": "json-sort",
        "clean.html": "json-clean",
        "xml.html": "json-to-xml",
        "yaml.html": "json-to-yaml",
        "viewer.html": "json-viewer",
        "json2csv.html": "json-to-csv",
        "compare.html": "json-compare",
    }
    for old, new in TOOL_MAP.items():
        content = content.replace(f'../../pages/{old}', f'/tools/{new}')

    # 4. ../../privacy.html  ../../terms.html  => 绝对路径
    content = re.sub(r'\.\./\.\./(\w[\w-]*)\.html', r'/\1', content)

    # 5. index.html（博客列表）=> /blog
    content = re.sub(r'href="index\.html"', 'href="/blog"', content)

    # 6. 同级文章链接 xxx.html => /blog/xxx
    #    排除已经是绝对路径或外链的情况
    def replace_same_level_blog(m):
        attr = m.group(1)  # href 或 src
        fname = m.group(2)  # xxx.html
        slug_name = fname[:-5]  # 去掉 .html
        return f'{attr}="/blog/{slug_name}"'

    content = re.sub(
        r'(href)="([a-z][a-z0-9-]+\.html)"',
        replace_same_level_blog,
        content
    )

    return content


def fix_news_article(slug: str, content: str) -> str:
    """修复 news 文章中的相对链接"""

    # 1. canonical / og:url
    content = re.sub(
        r'(href|content)="https://www\.aijsons\.com/pages/news/' + re.escape(slug) + r'\.html"',
        lambda m: f'{m.group(1)}="https://www.aijsons.com/news/{slug}"',
        content
    )

    # 2. ../../css/ ../../js/ ../../images/
    content = re.sub(r'(\.\./){2}(css|js|images)/', r'/\2/', content)

    # 3. ../../pages/工具 => /tools/slug
    TOOL_MAP = {
        "format.html": "json-formatter",
        "escape.html": "json-escape",
        "extract.html": "json-extract",
        "sort.html": "json-sort",
        "clean.html": "json-clean",
        "xml.html": "json-to-xml",
        "yaml.html": "json-to-yaml",
        "viewer.html": "json-viewer",
        "json2csv.html": "json-to-csv",
        "compare.html": "json-compare",
    }
    for old, new in TOOL_MAP.items():
        content = content.replace(f'../../pages/{old}', f'/tools/{new}')

    # 4. ../../privacy.html 等 => /privacy
    content = re.sub(r'\.\./\.\./(\w[\w-]*)\.html', r'/\1', content)

    # 5. index.html（新闻列表）=> /news
    content = re.sub(r'href="index\.html"', 'href="/news"', content)

    # 6. 同级新闻文章 xxx.html => /news/xxx
    def replace_same_level_news(m):
        fname = m.group(2)
        slug_name = fname[:-5]
        return f'href="/news/{slug_name}"'

    content = re.sub(
        r'(href)="([a-z][a-z0-9-]+\.html)"',
        replace_same_level_news,
        content
    )

    return content


def migrate_articles(src_dir: Path, target_dir: Path, fix_fn, label: str):
    """把 src_dir 下所有 .html（除 index.html）迁移到 target_dir/<slug>/index.html"""
    migrated = []
    for src_file in sorted(src_dir.glob("*.html")):
        if src_file.stem == "index":
            continue  # 跳过列表页本身

        slug = src_file.stem
        content = src_file.read_text(encoding="utf-8")
        content = fix_fn(slug, content)

        dest_dir = target_dir / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / "index.html").write_text(content, encoding="utf-8")
        migrated.append(slug)
        print(f"  OK: {label}/{slug}/index.html")

    return migrated


# ─── 执行迁移 ──────────────────────────────────────────────────
print("=== Migrating blog articles ===")
blog_slugs = migrate_articles(
    BASE / "pages" / "blog",
    BASE / "blog",
    fix_blog_article,
    "blog"
)

print(f"\n=== Migrating news articles ===")
news_slugs = migrate_articles(
    BASE / "pages" / "news",
    BASE / "news",
    fix_news_article,
    "news"
)

# ─── 更新 _redirects ──────────────────────────────────────────
redirects_path = BASE / "_redirects"
redirects = redirects_path.read_text(encoding="utf-8")

# 重建 blog 文章重定向块
blog_block = "# Blog articles\n"
for slug in blog_slugs:
    blog_block += f"/pages/blog/{slug}.html     /blog/{slug}\n"

news_block = "# News articles\n"
for slug in news_slugs:
    news_block += f"/pages/news/{slug}.html      /news/{slug}\n"

# 替换旧的 blog articles 块
redirects = re.sub(
    r"# Blog articles\n.*?(?=\n# |\Z)",
    blog_block.rstrip(),
    redirects,
    flags=re.DOTALL
)

# 替换旧的 news articles 块
redirects = re.sub(
    r"# News articles\n.*?(?=\n# |\Z)",
    news_block.rstrip(),
    redirects,
    flags=re.DOTALL
)

redirects_path.write_text(redirects, encoding="utf-8")
print(f"\n=== Updated _redirects ===")

print(f"\nDone! Migrated {len(blog_slugs)} blog articles + {len(news_slugs)} news articles.")
print("Blog URLs:  /blog/<slug>  =>  blog/<slug>/index.html")
print("News URLs:  /news/<slug>  =>  news/<slug>/index.html")
