#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""直接修复根目录 cookie/privacy/terms 页面的 pages/ 链接"""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# 完整的 pages/*.html -> 新URL 映射（所有可能出现的）
pages_to_url = {
    'pages/format.html': '/tools/json-formatter',
    'pages/escape.html': '/tools/json-escape',
    'pages/extract.html': '/tools/json-extract',
    'pages/sort.html': '/tools/json-sort',
    'pages/clean.html': '/tools/json-clean',
    'pages/xml.html': '/tools/json-to-xml',
    'pages/yaml.html': '/tools/json-to-yaml',
    'pages/viewer.html': '/tools/json-viewer',
    'pages/json2csv.html': '/tools/json-to-csv',
    'pages/compare.html': '/tools/json-compare',
    'pages/batch-file-renamer.html': '/tools/batch-renamer',
    'pages/about.html': '/about',
    'pages/blog.html': '/blog',
    'pages/news.html': '/news',
    'pages/best-practices.html': '/best-practices',
    'pages/changelog.html': '/changelog',
}

for fname in ['cookie.html', 'privacy.html', 'terms.html']:
    f = BASE / fname
    if not f.exists():
        continue
    text = f.read_text(encoding='utf-8')
    original = text
    changes = 0
    for old, new in pages_to_url.items():
        count = text.count(f'href="{old}"')
        if count:
            text = text.replace(f'href="{old}"', f'href="{new}"')
            changes += count
    if changes:
        f.write_text(text, encoding='utf-8')
        print(f'Fixed {fname}: {changes} changes')
        # 同时 fix the migrated copy
        dname = fname.replace('.html', '')
        mf = BASE / dname / 'index.html'
        if mf.exists():
            mf_text = mf.read_text(encoding='utf-8')
            mf_original = mf_text
            for old, new in pages_to_url.items():
                count2 = mf_text.count(f'href="{old}"')
                if count2:
                    mf_text = mf_text.replace(f'href="{old}"', f'href="{new}"')
                    changes += count2
            if mf_text != mf_original:
                mf.write_text(mf_text, encoding='utf-8')
                print(f'  Also fixed {dname}/index.html')
    else:
        print(f'No changes needed for {fname}')
print('Done.')
