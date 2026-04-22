#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查所有工具页的 canonical URL"""
import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

broken = []
fixed = []

for d in sorted((BASE/'tools').glob('*')):
    if not d.is_dir():
        continue
    f = d / 'index.html'
    if not f.exists():
        continue
    text = f.read_text(encoding='utf-8')
    # 找 canonical
    m = re.search(r'<link rel="canonical" href="([^"]+)"', text)
    if m:
        canonical = m.group(1)
        slug = d.name
        expected = f'https://www.aijsons.com/tools/{slug}'
        if canonical != expected:
            broken.append((f.relative_to(BASE), canonical, expected))
        else:
            fixed.append(f.relative_to(BASE))

print(f'Fixed canonicals: {len(fixed)}')
print(f'Broken canonicals: {len(broken)}')
for fname, got, expected in broken:
    print(f'  {fname}:')
    print(f'    GOT:      {got}')
    print(f'    EXPECTED: {expected}')
