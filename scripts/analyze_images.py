#!/usr/bin/env python3
"""Analyze images in pages for CLS issues"""
import os
import re

def analyze_images(fp):
    """Analyze images in a page"""
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    images = re.findall(r'<img[^>]+>', content)

    issues = []
    for img in images:
        # Check for width/height attributes
        if 'width="' in img or 'height="' in img:
            issues.append(f'Has width/height attrs: {img[:80]}')

    return images, issues

def main():
    pages_dir = r'd:\网站开发-json\pages'
    root_files = [r'd:\网站开发-json\index.html']

    all_pages = [(fp, os.path.basename(fp)) for fp in root_files]
    for f in os.listdir(pages_dir):
        if f.endswith('.html'):
            all_pages.append((os.path.join(pages_dir, f), f))

    print('=== Image Analysis ===\n')

    for fp, name in sorted(all_pages):
        images, issues = analyze_images(fp)
        if images:
            print(f'{name}: {len(images)} images')
            for issue in issues[:2]:  # Show first 2 issues
                print(f'  - {issue[:100]}')

    print('\n=== Sample images with dimensions ===\n')
    with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    images = re.findall(r'<img[^>]+>', content)
    for img in images[:5]:
        print(img[:150])

if __name__ == '__main__':
    main()
