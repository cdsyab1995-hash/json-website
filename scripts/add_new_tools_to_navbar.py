#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add CSS Minifier and HTML Encoder links to all existing pages' nav dropdown
Strategy: Find the Timestamp link and insert after it
"""
import os
import re

BASE_DIR = r'd:\网站开发-json'

# New nav items to add after timestamp link
NEW_TOOLS_AFTER_TIMESTAMP = '''                        <a href="css-minifier.html" class="nav-link">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                            CSS Minifier
                        </a>
                        <a href="html-encoder.html" class="nav-link">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                            HTML Encoder
                        </a>'''

# For index.html (different relative paths)
NEW_TOOLS_ROOT_AFTER_TIMESTAMP = '''                    <a href="pages/css-minifier.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                        CSS Minifier
                    </a>
                    <a href="pages/html-encoder.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                        HTML Encoder
                    </a>'''

def add_to_pages_dir():
    pages_dir = os.path.join(BASE_DIR, 'pages')
    updated = 0
    skipped = 0
    
    for filename in sorted(os.listdir(pages_dir)):
        if not filename.endswith('.html'):
            continue
        if filename in ('css-minifier.html', 'html-encoder.html'):
            continue  # Already have the links
            
        filepath = os.path.join(pages_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        
        # Check if already updated
        if 'css-minifier.html' in content:
            print(f'  SKIP (already updated): {filename}')
            skipped += 1
            continue
        
        # Find the timestamp link and insert after it
        # Pattern: Timestamp nav link followed by divider or closing tag
        timestamp_pattern = r'(<a href="timestamp-converter\.html"[^<]*(?:<[^/][^>]*>[^<]*</[^>]+>\s*)*Timestamp\s*</a>)'
        
        if re.search(timestamp_pattern, content, re.DOTALL):
            new_content = re.sub(
                timestamp_pattern,
                r'\1\n' + NEW_TOOLS_AFTER_TIMESTAMP,
                content,
                count=1,
                flags=re.DOTALL
            )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'  OK: {filename}')
                updated += 1
            else:
                print(f'  WARN (no change): {filename}')
                skipped += 1
        else:
            # Try simpler pattern
            simple_ts = 'timestamp-converter.html'
            if simple_ts in content:
                # Find the Timestamp link block
                ts_idx = content.rfind(simple_ts)
                # Find the closing </a> after timestamp link
                close_a = content.find('</a>', ts_idx)
                if close_a > -1:
                    insert_after = close_a + 4
                    new_content = content[:insert_after] + '\n' + NEW_TOOLS_AFTER_TIMESTAMP + content[insert_after:]
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'  OK (simple): {filename}')
                    updated += 1
                else:
                    print(f'  WARN (no </a>): {filename}')
                    skipped += 1
            else:
                print(f'  WARN (no timestamp): {filename}')
                skipped += 1
    
    return updated, skipped

def add_to_index():
    filepath = os.path.join(BASE_DIR, 'index.html')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
    
    if 'css-minifier.html' in content:
        print('  SKIP index.html (already updated)')
        return 0
    
    # Find timestamp link in index.html
    ts_search = 'pages/timestamp-converter.html'
    if ts_search in content:
        ts_idx = content.rfind(ts_search)
        close_a = content.find('</a>', ts_idx)
        if close_a > -1:
            insert_after = close_a + 4
            new_content = content[:insert_after] + '\n' + NEW_TOOLS_ROOT_AFTER_TIMESTAMP + content[insert_after:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('  OK: index.html')
            return 1
    
    print('  WARN: Could not update index.html')
    return 0

print('=== Updating pages/ directory ===')
updated_pages, skipped_pages = add_to_pages_dir()

print('\n=== Updating root index.html ===')
updated_root = add_to_index()

print(f'\n=== Summary ===')
print(f'Updated: {updated_pages + updated_root} files')
print(f'Skipped: {skipped_pages} files')
