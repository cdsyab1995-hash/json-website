# -*- coding: utf-8 -*-
"""修复 /pages/ 旧链接"""
import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 修复 JSON-LD 中的 URL
    content = re.sub(
        r'"url":\s*"https://aijsons\.com/pages/([^"]+)\.html"',
        r'"url": "https://aijsons.com/\1"',
        content
    )
    content = re.sub(
        r'"@id":\s*"https://aijsons\.com/pages/([^"]+)\.html"',
        r'"@id": "https://aijsons.com/\1"',
        content
    )
    
    # 修复内部导航链接
    content = re.sub(r'/pages/blog\.html', '/blog', content)
    content = re.sub(r'/pages/news\.html', '/news', content)
    content = re.sub(r'/pages/about\.html', '/about', content)
    content = re.sub(r'/pages/changelog\.html', '/changelog', content)
    content = re.sub(r'/pages/privacy\.html', '/privacy', content)
    content = re.sub(r'/pages/terms\.html', '/terms', content)
    content = re.sub(r'/pages/cookie\.html', '/cookie', content)
    
    # 修复博客文章链接
    content = re.sub(r'/pages/blog/([^"]+)\.html', r'/\1', content)
    
    # 修复工具链接
    content = re.sub(r'/pages/format\.html', '/tools/json-formatter', content)
    content = re.sub(r'/pages/viewer\.html', '/tools/json-viewer', content)
    content = re.sub(r'/pages/escape\.html', '/tools/json-escape', content)
    content = re.sub(r'/pages/extract\.html', '/tools/json-extract', content)
    content = re.sub(r'/pages/sort\.html', '/tools/json-sort', content)
    content = re.sub(r'/pages/clean\.html', '/tools/json-clean', content)
    content = re.sub(r'/pages/xml\.html', '/tools/json-to-xml', content)
    content = re.sub(r'/pages/yaml\.html', '/tools/json-to-yaml', content)
    content = re.sub(r'/pages/json2csv\.html', '/tools/json-to-csv', content)
    content = re.sub(r'/pages/compare\.html', '/tools/json-compare', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base = r'd:\网站开发-json'
    fixed = 0
    
    for root, dirs, filenames in os.walk(base):
        for f in filenames:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                if fix_file(path):
                    print(f'Fixed: {path.replace(base, "")}')
                    fixed += 1
    
    print(f'\nTotal fixed: {fixed} files')

if __name__ == '__main__':
    main()
