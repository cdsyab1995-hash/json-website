#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

# Check what the trailing quote issue count actually means
fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')

# This is what the audit's check does - count class="..."> patterns
valid_count = len(re.findall(r'class="[^"]+">', fmt))
print(f'class="..."> patterns (normal HTML): {valid_count}')

# Check for actual double-quote issues (the real bug)
bad = re.findall(r'class="[^"]+""[^>]*>', fmt)
print(f'Actual double-quote bug patterns: {len(bad)}')
for b in bad[:5]:
    print(f'  {repr(b)}')

# Now verify the Load Example issue
app_js = (BASE / 'js/app.js').read_text(encoding='utf-8')
# Find template key
tpl_start = app_js.find('const templates=')
if tpl_start < 0:
    tpl_start = app_js.find('templates=')
print()
print('Template keys in app.js:')
for m in re.finditer(r'(\w+):\s*[{\'"]', app_js[tpl_start:tpl_start+500]):
    print(f'  key: {m.group(1)}')

# HTML option values
print('\nHTML option values:')
for m in re.finditer(r'<option\s+value="([^"]+)"', fmt):
    print(f'  option: {m.group(1)}')
