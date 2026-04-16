#!/usr/bin/env python3
"""修复导航栏 - 添加缺失的 changelog.html 链接"""
import os
import re
from pathlib import Path

FILES_TO_FIX = [
    'd:/网站开发-json/pages/format.html',
    'd:/网站开发-json/pages/escape.html',
    'd:/网站开发-json/pages/extract.html',
    'd:/网站开发-json/pages/sort.html',
    'd:/网站开发-json/pages/clean.html',
    'd:/网站开发-json/pages/xml.html',
    'd:/网站开发-json/pages/yaml.html',
    'd:/网站开发-json/pages/viewer.html',
    'd:/网站开发-json/pages/json2csv.html',
    'd:/网站开发-json/pages/compare.html',
    'd:/网站开发-json/pages/best-practices.html',
]

CHANGELOG_HTML = '''
            <a href="changelog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                Changelog
            </a>
'''

def add_changelog_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'changelog.html' in content:
        print(f"  [SKIP] {file_path} - already has changelog")
        return False
    
    about_pattern = r'(<a href="about\.html" class="nav-link">)'
    changelog_html = CHANGELOG_HTML.strip()
    
    new_content = re.sub(
        about_pattern,
        changelog_html + '\n            \\1',
        content
    )
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  [FIXED] {file_path}")
        return True
    else:
        print(f"  [ERROR] {file_path} - could not find About link")
        return False

def main():
    print("=" * 80)
    print("Fixing Navigation - Adding Changelog Links")
    print("=" * 80)
    
    fixed_count = 0
    for file_path in FILES_TO_FIX:
        if add_changelog_link(file_path):
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files.")

if __name__ == '__main__':
    main()
