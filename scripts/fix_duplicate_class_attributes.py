#!/usr/bin/env python3
"""Fix duplicate class attributes: class="x" class="y" -> class="x y" """

import os
import re

pages_dir = r"d:\网站开发-json\pages"
fixed_files = []

for root, dirs, files in os.walk(pages_dir):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        filepath = os.path.join(root, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern: class="..." class="..."
        new_content = re.sub(
            r'class="([^"]+)"\s+class="([^"]+)"',
            r'class="\1 \2"',
            content
        )
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files.append(filename)

print(f"Fixed {len(fixed_files)} files:")
for f in fixed_files:
    print(f"  - {f}")
