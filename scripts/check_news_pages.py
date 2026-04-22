#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

# Check pages/news for 2026-01-01
base = BASE / 'pages/news'
if base.exists():
    for f in sorted(base.glob('*.html')):
        text = f.read_text(encoding='utf-8')
        ld = re.search(r'<script type=.application/ld\+json.>(.*?)</script>', text, re.DOTALL)
        if ld and '2026-01-01' in ld.group(1):
            print(f'OLD BAD: {f.name}')
        elif ld:
            dp = re.search(r'datePublished.*?([0-9-]+)', ld.group(1))
            pub = dp.group(1) if dp else 'N/A'
            print(f'OK: {f.name} -> {pub}')
        else:
            print(f'NO JSON-LD: {f.name}')
print('Done')
