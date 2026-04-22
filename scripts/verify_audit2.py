#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

# Check btnFormat in format page
fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')

# Find btnClear position
idx = fmt.find('id="btnClear"')
print('btnClear at:', idx)
if idx > 0:
    section = fmt[max(0, idx-800):idx+50]
    print('=== BEFORE btnClear ===')
    print(section[-500:])

# Find btnFormat
idx2 = fmt.find('btnFormat')
print('\nbtnFormat (text) at:', idx2)
if idx2 > 0:
    print(fmt[max(0, idx2-50):idx2+100])

# Check duplicate classes
print('\n=== DUPLICATE CLASS CHECK ===')
dups = re.findall(r'class="[^"]*"[^>]*class="', fmt[:3000])
print(f'Found {len(dups)} duplicate class attr issues')

# Check trailing quote issues
trail = re.findall(r'class="[^"]+">', fmt[:3000])
print(f'Found {len(trail)} trailing quote issues')

# Check Common Use Cases
count = fmt.count('Common Use Cases')
print(f'Common Use Cases: {count}')

# Check the index.html duplicate issues
index_html = (BASE / 'index.html').read_text(encoding='utf-8')
dups2 = re.findall(r'class="[^"]*"[^>]*class="', index_html[:5000])
print(f'\nindex.html duplicate class attr: {len(dups2)}')
