# -*- coding: utf-8 -*-
"""Audit meta descriptions across all HTML pages"""
import re
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(r'd:\网站开发-json')

# Generic/weak descriptions to flag
WEAK_PATTERNS = [
    'json tool',
    'free json',
    'online json',
    'browser-based',
    'no signup',
    'no upload',
    'privacy-first',
    'client-side',
]

results = []
descriptions = []

for html_file in sorted(PROJECT_ROOT.rglob('*.html')):
    # Skip blog article pages (they have their own content)
    if '/blog/' in str(html_file):
        desc = re.search(r'<meta name="description" content="([^"]+)"', html_file.read_text('utf-8', errors='ignore'))
        if desc:
            descriptions.append((html_file.name, desc.group(1)))
        continue

    try:
        content = html_file.read_text(encoding='utf-8')
    except:
        continue

    # Extract meta description
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if not desc_match:
        results.append((html_file.name, 'MISSING', '', 'No meta description'))
        continue

    desc = desc_match.group(1)
    desc_len = len(desc)

    issues = []
    if desc_len < 120:
        issues.append(f'SHORT ({desc_len})')
    elif desc_len > 160:
        issues.append(f'LONG ({desc_len})')

    # Check for generic patterns
    desc_lower = desc.lower()
    generic_count = sum(1 for p in WEAK_PATTERNS if p in desc_lower)
    if generic_count >= 2:
        issues.append(f'GENERIC ({generic_count} patterns)')

    status = 'ISSUE' if issues else 'OK'
    results.append((html_file.name, status, desc[:80] + ('...' if len(desc) > 80 else ''), ', '.join(issues)))
    descriptions.append((html_file.name, desc))

# Check for duplicates
desc_texts = [d for _, d in descriptions]
duplicates = [name for name, d in descriptions if descriptions.count((name, d)) > 1]
seen = {}
for name, desc in descriptions:
    if desc in seen:
        if name not in seen[desc]:
            seen[desc].append(name)
    else:
        seen[desc] = [name]

dupes = {d: names for d, names in seen.items() if len(names) > 1}

# Print results
print('=' * 80)
print('META DESCRIPTION AUDIT')
print('=' * 80)

print('\n### Pages with Issues ###')
for name, status, desc, issues in results:
    if status != 'OK':
        print(f'\n[{status}] {name}')
        print(f'  Preview: {desc}')
        if issues:
            print(f'  Issues: {issues}')

print('\n### Duplicate Descriptions ###')
if dupes:
    for desc, names in dupes.items():
        print(f'\n  "{desc[:60]}..."')
        print(f'  Pages: {", ".join(names)}')
else:
    print('  None found')

print('\n### Summary ###')
ok_count = sum(1 for _, s, _, _ in results if s == 'OK')
issue_count = sum(1 for _, s, _, _ in results if s != 'OK')
print(f'  Total pages: {len(results)}')
print(f'  OK: {ok_count}')
print(f'  Issues: {issue_count}')
print('=' * 80)
