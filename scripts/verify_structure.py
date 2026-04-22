#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

tools_dirs = len(list((BASE/'tools').glob('*/')))
tools_files = len(list((BASE/'tools').glob('*.html')))
blog_dirs = len([d for d in (BASE/'blog').iterdir() if d.is_dir() and d.name != 'index.html'])
news_dirs = len([d for d in (BASE/'news').iterdir() if d.is_dir() and d.name != 'index.html'])
root_html = [f.name for f in BASE.glob('*.html') if f.name != 'index.html']

print(f'tools/ subdirs: {tools_dirs}, .html files (old): {tools_files}')
print(f'blog article dirs: {blog_dirs}, news article dirs: {news_dirs}')
print(f'Root .html files remaining: {root_html}')

checks = [
    'tools/json-formatter/index.html',
    'tools/json-escape/index.html',
    'tools/base64/index.html',
    'about/index.html',
    'blog/index.html',
    'blog/ai-tool-calling-mcp-2026/index.html',
    'news/index.html',
    'news/mcp-10000-servers/index.html',
    'best-practices/index.html',
    'changelog/index.html',
    'privacy/index.html',
    'terms/index.html',
    'cookie/index.html',
]
print()
for c in checks:
    exists = (BASE / c).exists()
    status = 'OK' if exists else 'MISSING'
    print(f'{c}: {status}')
