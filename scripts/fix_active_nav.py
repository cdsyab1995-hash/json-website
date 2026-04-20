#!/usr/bin/env python3
"""Fix navigation active class positioning - was added before nav-link class"""

import os
import re

pages_dir = r"d:\网站开发-json\pages"

# Pattern: href="xxx" class="active" class="nav-link" -> href="xxx" class="nav-link active"
# Also handles: href="xxx" class="active"> (if nav-link was missing)

for filename in os.listdir(pages_dir):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(pages_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix: href="xxx" class="active" class="nav-link" -> href="xxx" class="nav-link active"
    content = re.sub(
        r'href="([^"]+)"\s+class="active"\s+class="nav-link"',
        r'href="\1" class="nav-link active"',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")

print("\nDone!")
