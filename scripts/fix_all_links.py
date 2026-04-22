#!/usr/bin/env python3
"""
更新全站所有内部链接为新的干净URL结构

需要替换的链接模式：
pages/xxx.html  → /tools/xxx (或对应页面)
tools/xxx.html  → /tools/xxx
根目录裸文件     → /xxx
../xxx.html     → /xxx (blog/news内的相对路径)
"""

import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# pages/*.html → 新URL
pages_to_url = {
    'format.html': '/tools/json-formatter',
    'escape.html': '/tools/json-escape',
    'extract.html': '/tools/json-extract',
    'sort.html': '/tools/json-sort',
    'clean.html': '/tools/json-clean',
    'xml.html': '/tools/json-to-xml',
    'yaml.html': '/tools/json-to-yaml',
    'viewer.html': '/tools/json-viewer',
    'json2csv.html': '/tools/json-to-csv',
    'compare.html': '/tools/json-compare',
    'batch-file-renamer.html': '/tools/batch-renamer',
    'about.html': '/about',
    'blog.html': '/blog',
    'news.html': '/news',
    'best-practices.html': '/best-practices',
    'changelog.html': '/changelog',
}

# tools/*.html → /tools/xxx
tools_mapping = {}
tools_dir = BASE / 'tools'
if tools_dir.exists():
    for f in tools_dir.glob('*.html'):
        tools_mapping[f'tools/{f.name}'] = f'/tools/{f.stem}'

# 根目录裸文件
root_files = {
    'about.html': '/about',
    'blog.html': '/blog',
    'news.html': '/news',
    'changelog.html': '/changelog',
    'best-practices.html': '/best-practices',
    'privacy.html': '/privacy',
    'terms.html': '/terms',
    'cookie.html': '/cookie',
}

# 相对路径
relative_links = {
    '../about.html': '/about',
    '../blog.html': '/blog',
    '../news.html': '/news',
    '../changelog.html': '/changelog',
    '../best-practices.html': '/best-practices',
    '../privacy.html': '/privacy',
    '../terms.html': '/terms',
    '../cookie.html': '/cookie',
    '../index.html': '/',
    '../pages/format.html': '/tools/json-formatter',
    '../pages/escape.html': '/tools/json-escape',
    '../pages/extract.html': '/tools/json-extract',
    '../pages/sort.html': '/tools/json-sort',
    '../pages/clean.html': '/tools/json-clean',
    '../pages/xml.html': '/tools/json-to-xml',
    '../pages/yaml.html': '/tools/json-to-yaml',
    '../pages/viewer.html': '/tools/json-viewer',
    '../pages/json2csv.html': '/tools/json-to-csv',
    '../pages/compare.html': '/tools/json-compare',
    '../pages/batch-file-renamer.html': '/tools/batch-renamer',
    '../pages/about.html': '/about',
    '../pages/blog.html': '/blog',
    '../pages/news.html': '/news',
    '../pages/best-practices.html': '/best-practices',
    '../pages/changelog.html': '/changelog',
}

def fix_file(filepath):
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return 0, str(e)

    original = text
    changes = 0

    def do_replace(old, new):
        nonlocal changes, text
        count = text.count(f'href="{old}"')
        if count:
            text = text.replace(f'href="{old}"', f'href="{new}"')
            changes += count
        count = text.count(f'src="{old}"')
        if count:
            text = text.replace(f'src="{old}"', f'src="{new}"')
            changes += count

    for old, new in pages_to_url.items():
        do_replace(old, new)

    for old, new in tools_mapping.items():
        do_replace(old, new)

    for old, new in root_files.items():
        do_replace(old, new)

    for old, new in relative_links.items():
        do_replace(old, new)

    if text != original:
        filepath.write_text(text, encoding='utf-8')
    return changes, None

print('开始更新全站内部链接...')
total_changes = 0
files_updated = 0

html_files = list(BASE.glob('**/*.html'))
for f in html_files:
    if any(x in str(f) for x in ['node_modules', '.git', '__pycache__', '.workbuddy']):
        continue
    changes, err = fix_file(f)
    if err:
        print(f'  错误 {f.relative_to(BASE)}: {err}')
    elif changes > 0:
        print(f'  FIXED {f.relative_to(BASE)}: {changes} changes')
        total_changes += changes
        files_updated += 1

print(f'\nDone: {files_updated} files, {total_changes} link updates')
