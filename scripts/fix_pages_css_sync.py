#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix all pages/*.html: change async CSS loading to sync for ../css/styles.css
"""
import sys, re, os, glob
sys.stdout.reconfigure(encoding='utf-8')

PAGES_DIR = r'd:\网站开发-json\pages'

html_files = glob.glob(os.path.join(PAGES_DIR, '*.html'))
print(f'Found {len(html_files)} HTML files in pages/')

fixed_count = 0
for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern for ../css/styles.css with async loading
    # Find preload + media=print async block
    pattern = r'<link rel="preload" href="\.\./css/styles\.css" as="style">\s*<link rel="stylesheet" href="\.\./css/styles\.css" media="print" onload="this\.media=\'all\'">\s*<noscript><link rel="stylesheet" href="\.\./css/styles\.css"></noscript>'
    replacement = '<link rel="stylesheet" href="../css/styles.css">'
    
    m = re.search(pattern, content)
    if m:
        content = re.sub(pattern, replacement, content)
        print(f'  FIXED (regex): {os.path.basename(filepath)}')
        fixed_count += 1
    else:
        # Try block-based approach
        preload_pattern = r'<link rel="preload" href="\.\./css/styles\.css" as="style">'
        m2 = re.search(preload_pattern, content)
        if m2:
            start = m2.start()
            end_marker = '</noscript>'
            end_pos = content.find(end_marker, start)
            if end_pos > 0 and end_pos - start < 500:  # reasonable range
                block = content[start:end_pos + len(end_marker)]
                if '../css/styles.css' in block:
                    content = content[:start] + replacement + content[end_pos + len(end_marker):]
                    print(f'  FIXED (block): {os.path.basename(filepath)}')
                    fixed_count += 1
            else:
                # Maybe media=print without preload?
                pattern3 = r'<link rel="stylesheet" href="\.\./css/styles\.css" media="print" onload="this\.media=\'all\'">'
                m3 = re.search(pattern3, content)
                if m3:
                    content = re.sub(pattern3, '<link rel="stylesheet" href="../css/styles.css">', content)
                    # Also remove preload hint
                    content = re.sub(r'<link rel="preload" href="\.\./css/styles\.css" as="style">\s*', '', content)
                    # Remove noscript fallback
                    content = re.sub(r'<noscript><link rel="stylesheet" href="\.\./css/styles\.css"></noscript>\s*', '', content)
                    print(f'  FIXED (media=print): {os.path.basename(filepath)}')
                    fixed_count += 1
        else:
            # Check if already sync
            sync_check = re.search(r'<link rel="stylesheet" href="\.\./css/styles\.css"(?! media)', content)
            if sync_check:
                pass  # Already sync, OK
            else:
                links = re.findall(r'<link[^>]*styles\.css[^>]*>', content)
                if links:
                    print(f'  SKIP (unknown pattern): {os.path.basename(filepath)}')
                    for l in links:
                        print(f'    {l[:100]}')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f'\nTotal fixed: {fixed_count} files')

# Verify - count remaining async CSS links across all pages
total_async = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    count = len(re.findall(r'media="print" onload="this\.media=\'all\'"', c))
    if count > 0:
        total_async += count
        print(f'  Still async: {os.path.basename(filepath)} ({count} instances)')

if total_async == 0:
    print('All pages: sync CSS loading confirmed')
else:
    print(f'WARNING: {total_async} async CSS instances remaining')
