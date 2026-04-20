# -*- coding: utf-8 -*-
"""Audit JSON-LD structured data across all HTML pages"""
import re
import json
from pathlib import Path

PROJECT_ROOT = Path(r'd:\网站开发-json')

# Required fields by type
REQUIRED_FIELDS = {
    'WebApplication': ['@type', '@context', 'name', 'url'],
    'Article': ['@type', '@context', 'headline', 'datePublished'],
    'WebSite': ['@type', '@context', 'name', 'url'],
    'FAQPage': ['@type', '@context'],
}

results = []

for html_file in sorted(PROJECT_ROOT.rglob('*.html')):
    try:
        content = html_file.read_text(encoding='utf-8')
    except:
        continue

    # Find all JSON-LD blocks
    ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)

    if not ld_blocks:
        # JSON-LD is optional, but tool pages should have it
        if 'pages/' in str(html_file) and not html_file.name.startswith('blog/'):
            results.append((html_file.name, 'MISSING', '', 'No JSON-LD found'))
        continue

    for block in ld_blocks:
        try:
            data = json.loads(block.strip())

            # Handle array of types
            types = data.get('@type', [])
            if isinstance(types, str):
                types = [types]

            for ld_type in types:
                if ld_type in REQUIRED_FIELDS:
                    missing = []
                    for field in REQUIRED_FIELDS[ld_type]:
                        if field not in data:
                            missing.append(field)

                    if missing:
                        results.append((html_file.name, 'MISSING_FIELDS', ld_type, f'Missing: {", ".join(missing)}'))
                    else:
                        results.append((html_file.name, 'OK', ld_type, ''))
                    break  # Only report first matching type
        except json.JSONDecodeError as e:
            results.append((html_file.name, 'INVALID_JSON', '', f'JSON parse error: {e}'))

# Print results
print('=' * 80)
print('JSON-LD STRUCTURED DATA AUDIT')
print('=' * 80)

missing_count = sum(1 for _, s, _, _ in results if s == 'MISSING')
missing_fields_count = sum(1 for _, s, _, _ in results if s == 'MISSING_FIELDS')
invalid_count = sum(1 for _, s, _, _ in results if s == 'INVALID_JSON')
ok_count = sum(1 for _, s, _, _ in results if s == 'OK')

print(f'\n### Issues ###')
for name, status, ld_type, detail in results:
    if status != 'OK':
        print(f'\n[{status}] {name}')
        if ld_type:
            print(f'  Type: {ld_type}')
        print(f'  Detail: {detail}')

print(f'\n### Summary ###')
print(f'  Missing JSON-LD: {missing_count}')
print(f'  Missing fields: {missing_fields_count}')
print(f'  Invalid JSON: {invalid_count}')
print(f'  OK: {ok_count}')
print('=' * 80)
