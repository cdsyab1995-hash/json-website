#!/usr/bin/env python3
"""Fix double-quote issues in HTML: class="...""> -> class="...">"""
import re
import io
import sys
from pathlib import Path

for stream in [sys.stdout, sys.stderr]:
    if stream.encoding != 'utf-8':
        stream.reconfigure(encoding='utf-8', errors='replace')

BASE = Path('d:/网站开发-json')

total_changes = 0
files_updated = 0

for pattern in ['**/*.html']:
    for f in BASE.glob(pattern):
        if any(x in str(f) for x in ['node_modules', '.git', '__pycache__', '.workbuddy']):
            continue
        try:
            text = f.read_text(encoding='utf-8')
        except:
            continue
        
        original = text
        
        # Fix: class="...""> -> class="...">
        # Pattern: class="VALUE"" followed by > or space+>
        # This is the exact fix for the double-quote issue
        new_text = re.sub(r'(class="[^"]+)"">', r'\1">', text)
        new_text = re.sub(r'(class="[^"]+)""([^">])', r'\1"\2', new_text)
        
        if new_text != text:
            changes = text.count('"">') - new_text.count('"">')
            f.write_text(new_text, encoding='utf-8')
            if changes > 0:
                rel = str(f.relative_to(BASE))
                print(f'  FIXED {rel}: {changes} double-quote fixes')
                files_updated += 1
                total_changes += changes

print(f'\nDone: {files_updated} files, {total_changes} fixes')
