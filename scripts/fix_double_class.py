# -*- coding: utf-8 -*-
"""Fix double class attribute issue: class="class=" -> class="" """
import os
import re
from pathlib import Path

PROJECT_ROOT = Path(r'd:\网站开发-json')

# Pattern: class="class="...  (the double opening, take the outer)
PATTERN = re.compile(r'class="class="([^"]*)"')
REPLACEMENT = r'class="\1"'

# Also fix potential: class="class="text-small...">  ->  class="text-small...">
PATTERN2 = re.compile(r'class="class="([^"]+)"')

fixed_count = 0
file_count = 0

for html_file in PROJECT_ROOT.rglob('*.html'):
    try:
        content = html_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f'[WARN] Cannot read {html_file}: {e}')
        continue

    # Match class="class="text...">  → class="text...">
    new_content, count = PATTERN2.subn(r'class="\1"', content)

    if count > 0:
        html_file.write_text(new_content, encoding='utf-8')
        fixed_count += count
        file_count += 1
        print(f'[FIX] {html_file.name}: {count} occurrence(s)')

print(f'\nTotal: {fixed_count} fixes in {file_count} files')
