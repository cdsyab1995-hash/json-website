#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复损坏的 canonical 标签（双重嵌套问题）"""
import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# slug -> correct canonical URL
canonicals = {
    'base64': 'https://www.aijsons.com/tools/base64',
    'batch-renamer': 'https://www.aijsons.com/tools/batch-renamer',
    'css-minifier': 'https://www.aijsons.com/tools/css-minifier',
    'csv-to-excel': 'https://www.aijsons.com/tools/csv-to-excel',
    'excel-remove-duplicates': 'https://www.aijsons.com/tools/excel-remove-duplicates',
    'hash-generator': 'https://www.aijsons.com/tools/hash-generator',
    'html-encoder': 'https://www.aijsons.com/tools/html-encoder',
    'json-clean': 'https://www.aijsons.com/tools/json-clean',
    'json-compare': 'https://www.aijsons.com/tools/json-compare',
    'json-escape': 'https://www.aijsons.com/tools/json-escape',
    'json-extract': 'https://www.aijsons.com/tools/json-extract',
    'json-formatter': 'https://www.aijsons.com/tools/json-formatter',
    'json-sort': 'https://www.aijsons.com/tools/json-sort',
    'json-to-csv': 'https://www.aijsons.com/tools/json-to-csv',
    'json-to-xml': 'https://www.aijsons.com/tools/json-to-xml',
    'json-to-yaml': 'https://www.aijsons.com/tools/json-to-yaml',
    'json-viewer': 'https://www.aijsons.com/tools/json-viewer',
    'jwt-decoder': 'https://www.aijsons.com/tools/jwt-decoder',
    'merge-csv': 'https://www.aijsons.com/tools/merge-csv',
    'pdf-split': 'https://www.aijsons.com/tools/pdf-split',
    'regex-tester': 'https://www.aijsons.com/tools/regex-tester',
    'timestamp-converter': 'https://www.aijsons.com/tools/timestamp-converter',
    'url-encoder': 'https://www.aijsons.com/tools/url-encoder',
    'uuid-generator': 'https://www.aijsons.com/tools/uuid-generator',
}

count = 0
for slug, canonical_url in canonicals.items():
    f = BASE / 'tools' / slug / 'index.html'
    if not f.exists():
        print(f'MISSING: tools/{slug}/index.html')
        continue
    text = f.read_text(encoding='utf-8')

    # 匹配双重嵌套的 canonical: <link rel="canonical" href="<link rel="canonical" href="URL"> <!-- Open Graph -->
    # 匹配直到下一个标签
    bad_pattern = r'<link rel="canonical" href="<link rel="canonical" href="([^"]+)">[^<]*'
    replacement = f'<link rel="canonical" href="{canonical_url}">'

    if re.search(bad_pattern, text):
        text = re.sub(bad_pattern, replacement, text)
        f.write_text(text, encoding='utf-8')
        count += 1
        print(f'Fixed: tools/{slug}/index.html')
    else:
        # 检查是否已正确
        if f'<link rel="canonical" href="{canonical_url}">' in text:
            print(f'OK: tools/{slug}/index.html')
        else:
            print(f'STILL BROKEN: tools/{slug}/index.html - needs manual check')

print(f'\nTotal fixed: {count}')
print('Done.')
