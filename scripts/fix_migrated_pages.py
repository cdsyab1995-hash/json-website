#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复迁移后页面的剩余问题"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# 更多链接映射 (从旧文件到新URL)
extra_mappings = {
    # cookie/privacy/terms 页面里的 index.html 链接
    'href="index.html"': 'href="/"',
    'href="pages/blog.html"': 'href="/blog"',
    'href="pages/best-practices.html"': 'href="/best-practices"',
    'href="pages/news.html"': 'href="/news"',
    'href="pages/about.html"': 'href="/about"',
    'href="pages/changelog.html"': 'href="/changelog"',
    # tools 页面里的 index.html 相对链接
    'href="../index.html"': 'href="/index.html"',
    # manifest.json 相对路径
    'href="../manifest.json"': 'href="/manifest.json"',
}

# 同时添加 pages/xxx -> /xxx 映射
pages_mappings = {}
for p in (BASE / 'pages').glob('*.html'):
    pages_mappings[f'href="pages/{p.name}"'] = f'href="/{p.stem}"'

all_mappings = {**extra_mappings, **pages_mappings}

def fix_file(filepath):
    text = filepath.read_text(encoding='utf-8')
    original = text
    changes = 0
    for old, new in all_mappings.items():
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            changes += count
    if text != original:
        filepath.write_text(text, encoding='utf-8')
    return changes

# 修复 cookie/, privacy/, terms/ 目录
for d in ['cookie', 'privacy', 'terms']:
    f = BASE / d / 'index.html'
    if f.exists():
        c = fix_file(f)
        if c:
            print(f'Fixed {d}/index.html: {c} changes')

# 修复 tools/*/index.html 的 ../manifest.json
tools_index_files = list((BASE / 'tools').glob('*/index.html'))
print(f'Tools pages to check: {len(tools_index_files)}')
for f in tools_index_files:
    c = fix_file(f)
    if c:
        print(f'Fixed {f.relative_to(BASE)}: {c} changes')

print('Done.')
