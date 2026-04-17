#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject PWA support into all HTML pages:
1. Add manifest link tag to <head>
2. Add theme-color meta tag
3. Add Apple touch icon
4. Add SW registration script
"""

import os
import re
from pathlib import Path

BASE_DIR = r'd:\网站开发-json'

# Pages in /pages/ directory - use relative paths
PAGES_SUBDIR_MANIFEST = '../manifest.json'
PAGES_SUBDIR_ICON = '../images/icon-192.png'

# Pages in root - use relative paths
ROOT_MANIFEST = '/manifest.json'
ROOT_ICON = '/images/icon-192.png'

# Service worker registration script
SW_SCRIPT = '''
    <!-- PWA Service Worker -->
    <script>
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js').then(function(reg) {
                console.log('[PWA] SW registered:', reg.scope);
            }).catch(function(err) {
                console.warn('[PWA] SW registration failed:', err);
            });
        });
    }
    </script>'''

def inject_pwa_to_file(file_path, manifest_path, icon_path):
    """Inject PWA tags into a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f'  ERROR reading {file_path}: {e}')
            return False

    # Skip if already has manifest
    if 'rel="manifest"' in content:
        print(f'  SKIP (already has manifest): {os.path.basename(file_path)}')
        return False

    # Build PWA head tags
    pwa_head_tags = f'''    <!-- PWA Manifest -->
    <link rel="manifest" href="{manifest_path}">
    <meta name="theme-color" content="#22C55E">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="JSON Tools">
    <link rel="apple-touch-icon" href="{icon_path}">'''

    # Insert before </head>
    if '</head>' in content:
        content = content.replace('</head>', pwa_head_tags + '\n</head>', 1)
    else:
        print(f'  WARN: No </head> in {os.path.basename(file_path)}')
        return False

    # Insert SW registration before </body>
    if SW_SCRIPT not in content and '</body>' in content:
        content = content.replace('</body>', SW_SCRIPT + '\n</body>', 1)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK: {os.path.basename(file_path)}')
        return True
    except Exception as e:
        print(f'  ERROR writing {file_path}: {e}')
        return False


def main():
    updated = 0
    skipped = 0
    
    # Process root HTML files
    root_files = ['index.html']
    print('\n=== Root HTML files ===')
    for filename in root_files:
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.exists(file_path):
            if inject_pwa_to_file(file_path, ROOT_MANIFEST, ROOT_ICON):
                updated += 1
            else:
                skipped += 1
    
    # Process pages/ directory
    pages_dir = os.path.join(BASE_DIR, 'pages')
    print('\n=== pages/ HTML files ===')
    if os.path.exists(pages_dir):
        for filename in sorted(os.listdir(pages_dir)):
            if filename.endswith('.html'):
                file_path = os.path.join(pages_dir, filename)
                if inject_pwa_to_file(file_path, PAGES_SUBDIR_MANIFEST, PAGES_SUBDIR_ICON):
                    updated += 1
                else:
                    skipped += 1
    
    # Process other root HTML files
    other_root_files = ['privacy.html', 'terms.html', 'cookie.html']
    print('\n=== Other root HTML files ===')
    for filename in other_root_files:
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.exists(file_path):
            if inject_pwa_to_file(file_path, ROOT_MANIFEST, ROOT_ICON):
                updated += 1
            else:
                skipped += 1
    
    print(f'\n=== Summary ===')
    print(f'Updated: {updated} files')
    print(f'Skipped: {skipped} files')

if __name__ == '__main__':
    main()
