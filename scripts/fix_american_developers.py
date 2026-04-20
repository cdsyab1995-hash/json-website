#!/usr/bin/env python3
"""Fix American developers references across all HTML files"""

import os
import re

def fix_american_developers(root_dir):
    """Replace 'American developers' with 'developers worldwide'"""
    
    # Patterns to find and replace
    patterns = [
        (r'for American developers', 'for developers worldwide'),
        (r'American developers', 'developers worldwide'),
        (r'US developer workflow', 'modern developer workflow'),
        (r'US developer', 'developer'),
    ]
    
    html_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith('.html') and not f.endswith('-en.html'):
                html_files.append(os.path.join(dirpath, f))
    
    fixed_count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            print(f"Fixed: {filepath}")
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    fix_american_developers(root)
