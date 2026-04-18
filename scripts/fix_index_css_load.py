#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix index.html: change async CSS loading to sync loading
The "media=print onload" pattern causes FOUC - SVG icons have no constraints during first paint
"""
import re

INDEX_FILE = r'd:\网站开发-json\index.html'

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} bytes")
print(f"Lines: {content.count(chr(10))}")

# Fix 1: Replace async CSS loading with sync loading for styles.css
# Pattern: <link rel="preload" href="css/styles.css" as="style">
#          <link rel="stylesheet" href="css/styles.css" media="print" onload="this.media='all'">
#          <noscript><link rel="stylesheet" href="css/styles.css"></noscript>

old_css = '<link rel="preload" href="css/styles.css" as="style"> <link rel="stylesheet" href="css/styles.css" media="print" onload="this.media=\'all\'"> <noscript><link rel="stylesheet" href="css/styles.css"></noscript>'
new_css = '<link rel="stylesheet" href="css/styles.css">'

# Also handle the version without spaces
old_css2 = '<link rel="preload" href="css/styles.css" as="style">\n<link rel="stylesheet" href="css/styles.css" media="print" onload="this.media=\'all\'">\n<noscript><link rel="stylesheet" href="css/styles.css"></noscript>'

if old_css in content:
    content = content.replace(old_css, new_css)
    print("✅ Fixed: async CSS -> sync CSS (single line variant)")
elif old_css2 in content:
    content = content.replace(old_css2, new_css)
    print("✅ Fixed: async CSS -> sync CSS (multiline variant)")
else:
    # Try regex
    pattern = r'<link rel="preload" href="css/styles\.css" as="style">\s*<link rel="stylesheet" href="css/styles\.css" media="print" onload="this\.media=\'all\'">\s*<noscript><link rel="stylesheet" href="css/styles\.css"></noscript>'
    if re.search(pattern, content):
        content = re.sub(pattern, '<link rel="stylesheet" href="css/styles.css">', content)
        print("✅ Fixed: async CSS -> sync CSS (regex)")
    else:
        # More flexible regex
        pattern2 = r'<link[^>]+preload[^>]+css/styles\.css[^>]*>\s*<link[^>]+css/styles\.css[^>]+media="print"[^>]*>\s*<noscript><link[^>]+css/styles\.css[^>]*></noscript>'
        if re.search(pattern2, content):
            content = re.sub(pattern2, '<link rel="stylesheet" href="css/styles.css">', content)
            print("✅ Fixed: async CSS -> sync CSS (flexible regex)")
        else:
            print("⚠️  Could not find the async CSS pattern, searching for any mention...")
            # Find all stylesheet links
            matches = re.findall(r'<link[^>]*styles\.css[^>]*>', content)
            for m in matches:
                print(f"  Found: {m[:100]}")

# Fix 2: Remove duplicate critical CSS (there are TWO identical <style> blocks)
# Keep only one
style_count = content.count('/* Critical CSS - prevent FOUC and CLS */')
print(f"\nCritical CSS blocks found: {style_count}")

if style_count > 1:
    # Remove the first duplicate (keep the second one which is more complete)
    first = content.find('/* Critical CSS - prevent FOUC and CLS */')
    # Find the </style> after it
    end_first = content.find('</style>', first)
    if end_first > 0:
        # Find the <style> tag before this comment
        start_style = content.rfind('<style>', 0, first)
        if start_style > 0:
            to_remove = content[start_style:end_first + len('</style>')]
            content = content.replace(to_remove, '', 1)
            print(f"✅ Removed duplicate critical CSS block ({len(to_remove)} chars)")

# Write back
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Done! Written {len(content)} bytes")

# Verify
with open(INDEX_FILE, 'rb') as f:
    first4 = f.read(4)
print(f"File BOM/encoding: {first4.hex()}")
