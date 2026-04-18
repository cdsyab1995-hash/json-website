#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nuclear fix: for each HTML file, remove ALL styles.css link tags, 
then insert a single clean sync link at the right position.
"""
import sys, re, os, glob
sys.stdout.reconfigure(encoding='utf-8')

# Determine correct href based on file location
def get_css_href(filepath):
    # pages/*.html -> ../css/styles.css
    # index.html (root) -> css/styles.css
    if 'pages' in filepath.replace('\\', '/'):
        return '../css/styles.css'
    return 'css/styles.css'

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    css_href = get_css_href(filepath)
    correct_link = f'<link rel="stylesheet" href="{css_href}">'
    
    # Count all styles.css links before
    before_links = re.findall(r'<link[^>]*styles\.css[^>]*>', content)
    
    # Remove ALL preload hints for styles.css
    content = re.sub(r'<link rel="preload" href="[^"]*styles\.css" as="style">\s*', '', content)
    
    # Remove ALL noscript blocks containing styles.css
    content = re.sub(r'<noscript><link rel="stylesheet" href="[^"]*styles\.css"></noscript>\s*', '', content)
    
    # Remove ALL async CSS links for styles.css (media=print pattern)
    content = re.sub(r'<link rel="stylesheet" href="[^"]*styles\.css" media="print" onload="[^"]*">\s*', '', content)
    
    # Remove ALL existing sync links for styles.css (to avoid duplicates)
    content = re.sub(r'<link rel="stylesheet" href="[^"]*styles\.css">\s*', '', content)
    
    # Now find the right insertion point: after </style> (last inline style block) or before </head>
    # Best position: before </head>
    insert_before = '</head>'
    insert_pos = content.rfind(insert_before)
    if insert_pos > 0:
        content = content[:insert_pos] + correct_link + '\n' + content[insert_pos:]
    else:
        # Fallback: insert after <head>
        insert_after = '<head>'
        pos = content.find(insert_after)
        if pos > 0:
            content = content[:pos + len(insert_after)] + '\n' + correct_link + content[pos + len(insert_after):]
    
    # Verify
    after_links = re.findall(r'<link[^>]*styles\.css[^>]*>', content)
    
    changed = content != open(filepath, 'r', encoding='utf-8').read()
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return {
        'file': os.path.basename(filepath),
        'before': len(before_links),
        'after': len(after_links),
        'after_links': after_links
    }

# Process all HTML files
files = [r'd:\网站开发-json\index.html']
files += glob.glob(r'd:\网站开发-json\pages\*.html')

print(f'Processing {len(files)} files...')
for filepath in sorted(files):
    result = fix_file(filepath)
    status = 'OK' if len(result['after_links']) == 1 else 'WARN'
    print(f'  [{status}] {result["file"]}: {result["before"]} -> {result["after"]} links')
    if status == 'WARN':
        for l in result['after_links']:
            print(f'    {l}')

print('\nDone!')
