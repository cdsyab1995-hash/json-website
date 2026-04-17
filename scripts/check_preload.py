#!/usr/bin/env python3
"""Check and add preload hints"""
import os
import re

def check_preload(fp):
    """Check preload hints"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # Check if CSS is preloaded
    if 'css/styles.css' in content or '../css/styles.css' in content:
        if 'rel="preload"' not in content or 'as="style"' not in content:
            issues.append('CSS not preloaded')

    # Check if fonts are preconnected
    if 'fonts.googleapis' in content:
        if 'rel="preconnect"' not in content:
            issues.append('Google Fonts not preconnected')
        if 'rel="preload"' in content and 'font' in content.lower():
            issues.append('Fonts preloaded')

    # Check async CSS loading
    if 'media="print"' in content and 'onload=' in content:
        issues.append('CSS already async')

    return issues

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in sorted(os.listdir(pages_dir)):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    print('=== Preload Analysis ===\n')

    for fp, name in all_pages:
        issues = check_preload(fp)
        if issues:
            for issue in issues:
                print(f'{name}: {issue}')
        else:
            print(f'{name}: OK')

if __name__ == '__main__':
    main()
