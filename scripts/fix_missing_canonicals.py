#!/usr/bin/env python3
"""Check which pages are missing canonical tags"""
import re
from pathlib import Path
BASE = Path('d:/网站开发-json')

missing = []
has_canonical = []

# Check all HTML files
for pattern in ['**/*.html']:
    for f in BASE.glob(pattern):
        if any(x in str(f) for x in ['node_modules', '.git', '__pycache__', '.workbuddy']):
            continue
        try:
            text = f.read_text(encoding='utf-8')
        except:
            continue
        
        rel = str(f.relative_to(BASE)).replace('\\', '/')
        
        # Check for canonical tag
        has_canon = bool(re.search(r'<link[^>]+rel=["\']canonical["\']', text))
        
        if has_canon:
            has_canonical.append(rel)
        else:
            missing.append(rel)

print(f'=== PAGES MISSING CANONICAL: {len(missing)} ===')
for m in sorted(missing)[:40]:
    print(f'  MISSING: {m}')

print(f'\n=== PAGES WITH CANONICAL: {len(has_canonical)} ===')
# Show samples
for h in sorted(has_canonical)[:10]:
    print(f'  OK: {h}')
