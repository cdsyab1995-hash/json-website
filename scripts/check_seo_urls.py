#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

# Check actual canonical in migrated pages
for fpath in ['about/index.html', 'blog/index.html', 'news/index.html',
              'best-practices/index.html', 'changelog/index.html',
              'tools/json-formatter/index.html']:
    f = BASE / fpath
    if f.exists():
        text = f.read_text(encoding='utf-8')
        canon = re.search(r'<link[^>]+rel=.canonical.[^>]*content=.[^"]+', text)
        og = re.search(r'<meta[^>]+property=.og:url.[^>]*content=.[^"]+', text)
        tw = re.search(r'<meta[^>]+name=.twitter:url.[^>]*content=.[^"]+', text)
        print(f'=== {fpath} ===')
        print(f'  canonical: {canon.group(0) if canon else "MISSING"}')
        print(f'  og:url:   {og.group(0) if og else "MISSING"}')
        print(f'  twitter:  {tw.group(0) if tw else "MISSING"}')
