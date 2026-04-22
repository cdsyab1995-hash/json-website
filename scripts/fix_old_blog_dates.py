#!/usr/bin/env python3
"""Fix datePublished/dateModified in old pages/blog/ and pages/news/ files"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

# For old blog/news files, we need to find and fix the datePublished/dateModified
# The canonical now points to new URL, but JSON-LD dates are still 2026-01-01
# Strategy: replace datePublished/dateModified in these old files with 2026-04-22 (today)
# or with the actual article date if we can find it in the visible content

TODAY = '2026-04-22'

# Subdirectories to fix
for subdir in ['pages/blog', 'pages/news']:
    base = BASE / subdir
    if not base.exists():
        continue
    
    for f in sorted(base.glob('*.html')):
        try:
            text = f.read_text(encoding='utf-8')
        except:
            continue
        
        original = text
        changes = 0
        
        # Try to find visible date in the content
        # Look for date patterns in visible content (not in JSON-LD)
        # The visible date is usually near the article header
        
        # Strategy: find the first date in the content that's NOT in JSON-LD
        # Then use that for JSON-LD
        
        # Extract JSON-LD section
        ld_match = re.search(r'<script type=.application/ld\+json.>(.*?)</script>', text, re.DOTALL)
        if not ld_match:
            continue
        
        ld_content = ld_match.group(1)
        original_ld = ld_content
        
        # Check if datePublished is 2026-01-01 (bad)
        if '"datePublished": "2026-01-01"' in ld_content:
            # Try to find visible date
            # Remove JSON-LD first to search in visible content
            visible = text[:ld_match.start()] + text[ld_match.end():]
            dates_found = re.findall(r'(\d{4}-\d{2}-\d{2})', visible)
            actual_date = dates_found[0] if dates_found else TODAY
            
            # Replace in JSON-LD
            ld_content = ld_content.replace('"datePublished": "2026-01-01"', f'"datePublished": "{actual_date}"')
            ld_content = ld_content.replace('"dateModified": "2026-01-01"', f'"dateModified": "{actual_date}"')
            
            text = text[:ld_match.start()] + ld_content + text[ld_match.end():]
            changes = 2
            print(f'  FIXED {f.relative_to(BASE)}: dates -> {actual_date}')
        
        if text != original:
            f.write_text(text, encoding='utf-8')

print('\nDone')
