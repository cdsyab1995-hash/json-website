#!/usr/bin/env python3
from pathlib import Path
import re

BASE = Path('d:/网站开发-json')
fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')

# Extract toolbar section
start = fmt.find('class="toolbar')
end = fmt.find('</div>', start) + 6
toolbar = fmt[start:end]
print('=== TOOLBAR ===')
print(toolbar[:600])

# Find all buttons
btns = re.findall(r'<button[^>]*>', toolbar)
print('\n=== BUTTONS ===')
for b in btns:
    print(b)

# Check for duplicate classes
print('\n=== DUPLICATE CLASS CHECK (index.html) ===')
dups = re.findall(r'class="[^"]*"[^">]*class="[^"]*"', fmt[:5000])
if dups:
    for d in dups[:5]:
        print('DUPLICATE CLASS:', d[:200])
else:
    print('No duplicate classes in visible area')

# Check setLoading in app.js
app_js = (BASE / 'js/app.js').read_text(encoding='utf-8')
idx = app_js.find('setLoading')
if idx >= 0:
    print('\n=== setLoading context ===')
    print(app_js[max(0,idx-50):idx+300])

# Check for Common Use Cases duplicate
count = fmt.count('Common Use Cases')
print(f'\n=== Common Use Cases occurrences: {count} ===')
if count > 1:
    print('DUPLICATE: Common Use Cases appears multiple times!')
