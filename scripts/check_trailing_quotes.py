#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')
# Find trailing quote issues: class="..." followed by > without space
# More precisely: class="..." with > right after (no space before >)
issues = re.findall(r'class="[^"]{0,50}">', fmt[:5000])
print(f'Found {len(issues)} trailing quote issues:')
for i in issues[:10]:
    print(f'  {i[:80]}')
