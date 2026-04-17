#!/usr/bin/env python3
"""Add CSS preload to pages that are missing it"""
import os
import re

def add_preload(fp):
    """Add CSS preload to a page"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has preload or no CSS
    if 'rel="preload"' in content:
        return False, 'Already has preload'

    if '../css/styles.css' not in content:
        return False, 'No CSS reference'

    # Find the CSS link
    css_pattern = r'<link rel="stylesheet" href="([^"]*css/styles\.css[^"]*)"[^>]*>'

    # Add preload before the stylesheet link
    preload = '<link rel="preload" href="\\1" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">'
    noscript = '<noscript><link rel="stylesheet" href="\\1"></noscript>'

    new_content = re.sub(
        css_pattern,
        preload + '\n    ' + noscript + '\n    \\g<0>',
        content
    )

    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, 'Added preload'
    else:
        return False, 'No change'

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in sorted(os.listdir(pages_dir)):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    fixed = []
    for fp, name in all_pages:
        changed, msg = add_preload(fp)
        if changed:
            fixed.append(name)
            print(f'[FIXED] {name}')
        else:
            print(f'[SKIP] {name}: {msg}')

    print(f'\nFixed {len(fixed)} pages')

if __name__ == '__main__':
    main()
