#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查迁移后的页面链接质量"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

samples = [
    'tools/json-formatter/index.html',
    'tools/json-escape/index.html',
    'tools/base64/index.html',
    'cookie/index.html',
    'privacy/index.html',
]

for p in samples:
    f = BASE / p
    if not f.exists():
        print(f'MISSING: {p}')
        continue
    text = f.read_text(encoding='utf-8')
    links = re.findall(r'(?:href|src)="([^"]+)"', text)
    bad = [l for l in links if (l.startswith('../') or '.html' in l) and not l.startswith('http') and not l.startswith('/')]
    old_html = [l for l in links if '.html' in l and not l.startswith('http') and not l.startswith('/')]
    css_ok = 'href="/css/' in text or 'href="../../css/' not in text
    js_ok = 'src="/js/' in text or 'src="../../js/' not in text
    print(f'{p}:')
    print(f'  CSS OK: {css_ok}, JS OK: {js_ok}')
    print(f'  Bad links: {bad[:5]}')
    print(f'  Old .html links: {old_html[:3]}')
