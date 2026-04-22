#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')

# Find double-quote issues: class="...""> where there's an extra quote
# Pattern: class="..." followed by " then >
bad = re.findall(r'class="[^"]+""[^>]*>', fmt)
print(f'Bad patterns: {len(bad)}')
for b in bad[:10]:
    print(f'  {repr(b[:100])}')

# Also find: any class attribute that ends with ""
class_dups = re.findall(r'class="[^"]+""', fmt)
print(f'\nclass ending with double quote: {len(class_dups)}')
for c in class_dups[:10]:
    print(f'  {repr(c[:100])}')
