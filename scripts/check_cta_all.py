#!/usr/bin/env python3
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

print('=== Checking CTA Button in all pages ===\n')

for filename in sorted(os.listdir(pages_dir)):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for CTA button
    has_cta = 'Try Formatter' in content
    
    if has_cta:
        print(f'{filename}: YES')
    else:
        print(f'{filename}: NO - Missing CTA')
