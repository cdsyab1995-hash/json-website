#!/usr/bin/env python3
from pathlib import Path
import re
BASE = Path('d:/网站开发-json')

fmt = (BASE / 'tools/json-formatter/index.html').read_text(encoding='utf-8')
# Same as final_audit_check.py
issues = re.findall(r'class="[^"]+">', fmt[:3000])
print(f'Found {len(issues)} matches in first 3000 chars:')
for i in issues[:10]:
    print(f'  REPR: {repr(i[:80])}')
