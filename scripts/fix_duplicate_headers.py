#!/usr/bin/env python3
"""Fix duplicate article headers in blog posts"""

import re
import os

def fix_duplicate_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match duplicate header section
    # Find </div> followed by <header class="article-header"> with h1 inside
    pattern = r'</div>\s*<header class="article-header">\s*<h1[^>]*>.*?</h1>\s*<div class="article-meta">.*?</div>\s*</header>\s*<div class="article-content">'
    
    # Replace with just the article-content div
    replacement = '</div>\n            <div class="article-content">'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

files = [
    r'pages\blog\ai-tool-calling-mcp-2026.html',
    r'pages\blog\json-api-error-handling-2026.html',
]

for f in files:
    if os.path.exists(f):
        if fix_duplicate_header(f):
            print(f"Fixed: {f}")
        else:
            print(f"No change: {f}")
    else:
        print(f"Not found: {f}")
