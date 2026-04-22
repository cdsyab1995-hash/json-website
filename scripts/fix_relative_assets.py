#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复所有工具页的 ../manifest.json 和 ../images 相对路径"""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# 在 tools/*/index.html 中，深度=2，所以 ../manifest.json 应该改为 /manifest.json
fixes = [
    ('href="../manifest.json"', 'href="/manifest.json"'),
    ('content="../images/', 'content="/images/'),
    ('src="../images/', 'src="/images/'),
]

count = 0
for d in (BASE / 'tools').glob('*'):
    if not d.is_dir():
        continue
    f = d / 'index.html'
    if not f.exists():
        continue
    text = f.read_text(encoding='utf-8')
    original = text
    for old, new in fixes:
        if old in text:
            text = text.replace(old, new)
            count += 1
    if text != original:
        f.write_text(text, encoding='utf-8')
        print(f'Fixed {f.relative_to(BASE)}')

print(f'Total fixes: {count}')
print('Done.')
