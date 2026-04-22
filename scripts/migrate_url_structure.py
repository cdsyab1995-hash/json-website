#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""URL结构统一迁移脚本 - 将所有 .html 文件转换为 dir/index.html 结构"""

import re
import io
import sys
from pathlib import Path

# Fix stdout encoding
for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# ============================================================
# 1. 定义迁移映射
# ============================================================
migrations = {}

# tools/*.html -> tools/name/index.html
tools_dir = BASE / 'tools'
if tools_dir.exists():
    for f in sorted(tools_dir.glob('*.html')):
        slug = f.stem
        url = f'/tools/{slug}'
        migrations[f] = (slug, url)

# root-level .html -> dir/index.html
for fname in ['cookie', 'privacy', 'terms']:
    f = BASE / f'{fname}.html'
    if f.exists():
        url = f'/{fname}'
        migrations[f] = (fname, url)

print(f'Files to migrate: {len(migrations)}')
for f, (slug, url) in sorted(migrations.items()):
    print(f'  {f.relative_to(BASE)} -> {slug}/index.html  [{url}]')

# ============================================================
# 2. 执行文件迁移
# ============================================================
print('\n--- Migrating files ---')
migrated_count = 0
errors = []

for old_file, (new_dir, url) in sorted(migrations.items()):
    target_dir = old_file.parent / new_dir

    if target_dir.exists():
        print(f'SKIP (exists): {old_file.relative_to(BASE)}')
        continue

    try:
        text = old_file.read_text(encoding='utf-8')
    except Exception as e:
        errors.append(f'{old_file}: {e}')
        continue

    # 计算从新文件位置到根目录的相对路径
    depth = len(target_dir.relative_to(BASE).parts) - 1
    root_rel = '/'.join(['..'] * depth) if depth > 0 else ''
    if root_rel:
        css_path = f'{root_rel}/css/'
        js_path = f'{root_rel}/js/'
    else:
        css_path = '/css/'
        js_path = '/js/'

    # 替换 CSS/JS 链接
    text = re.sub(r'href="(\.\./)+css/', f'href="{css_path}"', text)
    text = re.sub(r'href="(\.\./)+js/', f'href="{js_path}"', text)
    text = re.sub(r'src="(\.\./)+css/', f'src="{css_path}"', text)
    text = re.sub(r'src="(\.\./)+js/', f'src="{js_path}"', text)

    # 替换 canonical / og:url / JSON-LD url
    old_slug = old_file.stem
    for old_url in [f'https://www.aijsons.com/{old_slug}.html',
                    f'https://aijsons.com/{old_slug}.html']:
        text = text.replace(old_url, f'https://www.aijsons.com{url}')
        text = text.replace(f'"url": "{old_url}"', f'"url": "https://www.aijsons.com{url}"')

    # 创建目录并写入
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / 'index.html'
    target_file.write_text(text, encoding='utf-8')

    migrated_count += 1
    print(f'OK: {old_file.relative_to(BASE)} -> {target_dir.relative_to(BASE)}/index.html')

if errors:
    print(f'\nErrors: {errors}')

print(f'\nMigrated {migrated_count} files')

# ============================================================
# 3. 更新 _redirects
# ============================================================
print('\n--- Updating _redirects ---')
redirects_file = BASE / '_redirects'
existing = redirects_file.read_text(encoding='utf-8') if redirects_file.exists() else ''

redirect_entries = []
for old_file, (new_dir, url) in sorted(migrations.items()):
    old_stem = old_file.stem
    if old_file.parent.name == 'tools':
        old_url = f'/tools/{old_stem}.html'
        redirect_url = f'/tools/{old_stem}'
    else:
        old_url = f'/{old_stem}.html'
        redirect_url = f'/{old_stem}'
    redirect_entries.append((old_url, redirect_url))

existing_lines = existing.split('\n')
new_entries = []
for old, new in redirect_entries:
    found = any(old in line and not line.strip().startswith('#') for line in existing_lines)
    if not found:
        new_entries.append(f'{old}\t{new}')
        print(f'ADD redirect: {old} -> {new}')

if new_entries:
    marker = '# URL structure migration (2026-04-22)\n'
    if marker not in existing:
        new_content = existing.rstrip('\n') + '\n\n' + marker + '\n'.join(new_entries) + '\n'
    else:
        new_content = existing
    redirects_file.write_text(new_content, encoding='utf-8')
    print(f'Updated _redirects: added {len(new_entries)} rules')
else:
    print('_redirects: no new rules needed')

print('\nDone.')
