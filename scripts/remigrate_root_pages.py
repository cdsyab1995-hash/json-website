#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新迁移根目录页面（用已修复的 .html 文件覆盖 dir/index.html）"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

root_files = {
    'cookie.html': '/cookie',
    'privacy.html': '/privacy',
    'terms.html': '/terms',
}

print('Re-migrating root pages using fixed source files...')

for fname, url in root_files.items():
    old_file = BASE / fname
    target_dir = BASE / fname.replace('.html', '')
    target_file = target_dir / 'index.html'

    if not old_file.exists():
        print(f'SKIP: {fname} not found')
        continue

    # 读取已修复的文件内容
    text = old_file.read_text(encoding='utf-8')

    # 深度=1 (cookie/index.html), root_rel = '..'
    root_rel = '..'
    css_path = f'{root_rel}/css/'
    js_path = f'{root_rel}/js/'

    # 替换 CSS/JS 相对路径
    text = re.sub(r'href="(\.\./)+css/', f'href="{css_path}"', text)
    text = re.sub(r'href="(\.\./)+js/', f'href="{js_path}"', text)
    text = re.sub(r'src="(\.\./)+css/', f'src="{css_path}"', text)
    text = re.sub(r'src="(\.\./)+js/', f'src="{js_path}"', text)

    # 替换 canonical
    old_slug = old_file.stem
    for old_url in [f'https://www.aijsons.com/{old_slug}.html',
                    f'https://aijsons.com/{old_slug}.html']:
        text = text.replace(old_url, f'https://www.aijsons.com{url}')

    # 写入
    target_file.write_text(text, encoding='utf-8')
    print(f'Re-migrated: {fname} -> {target_file.relative_to(BASE)}')

    # 验证
    verify = target_file.read_text(encoding='utf-8')
    has_bad = 'pages/' in verify and 'href="pages/' in verify
    has_html_link = '.html"' in verify and 'href="' in verify and not any(x in verify for x in ['href="/blog"', 'href="/tools/', 'href="/about', 'href="/privacy'])
    print(f'  Verified: has pages/ links = {has_bad}')

print('Done.')
