# -*- coding: utf-8 -*-
"""
修复首页所有旧链接
"""
import os
import re

HOME = r'd:\网站开发-json\index.html'

# 工具链接映射
TOOLS_MAP = {
    'pages/format.html': '/tools/json-formatter',
    'pages/escape.html': '/tools/json-escape',
    'pages/extract.html': '/tools/json-extract',
    'pages/sort.html': '/tools/json-sort',
    'pages/clean.html': '/tools/json-clean',
    'pages/xml.html': '/tools/json-to-xml',
    'pages/yaml.html': '/tools/json-to-yaml',
    'pages/viewer.html': '/tools/json-viewer',
    'pages/json2csv.html': '/tools/json-to-csv',
    'pages/compare.html': '/tools/json-compare',
    'pages/csv-to-excel.html': '/tools/csv-to-excel',
    'pages/excel-remove-duplicates.html': '/tools/excel-remove-duplicates',
}

# Footer 链接映射
FOOTER_MAP = {
    'pages/about.html': '/about',
    'pages/changelog.html': '/changelog',
}

# 旧文章锚点到实际文章映射
# ai-daily-20260420 = json-edge-computing-cloudflare-workers
# ai-daily-20260418 = json-patch-vs-merge-patch
# ai-daily-20260417 = (无对应文章，跳过)
# ai-daily-20260416b = zod-json-schema-validation-ai
ANCHOR_MAP = {
    'pages/blog.html#ai-daily-20260420': '/blog/json-edge-computing-cloudflare-workers',
    'pages/blog.html#ai-daily-20260418': '/blog/json-patch-vs-merge-patch',
    'pages/blog.html#ai-daily-20260417': None,  # 无对应文章
    'pages/blog.html#ai-daily-20260416b': '/blog/zod-json-schema-validation-ai',
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. 修复工具链接
    for old, new in TOOLS_MAP.items():
        content = content.replace(f'href="{old}"', f'href="{new}"')
        content = content.replace(f"href='{old}'", f"href='{new}'")
    
    # 2. 修复 footer 链接
    for old, new in FOOTER_MAP.items():
        content = content.replace(f'href="{old}"', f'href="{new}"')
        content = content.replace(f"href='{old}'", f"href='{new}'")
    
    # 3. 修复文章锚点
    for old, new in ANCHOR_MAP.items():
        if new:
            content = content.replace(f'href="{old}"', f'href="{new}"')
            content = content.replace(f"href='{old}'", f"href='{new}'")
        else:
            # 删除无效链接的整个元素
            content = re.sub(
                r'<article[^>]*>[\s\S]*?href="' + re.escape(old) + r'"[\s\S]*?</article>',
                '',
                content
            )
    
    # 4. 修复 href 属性缺失的文章链接 (如: <a /blog/xxx>)
    # 匹配 <a /blog/xxx 或 <a href=/blog/xxx 格式
    content = re.sub(
        r'<a\s+(/blog/[^>"]+)>',
        r'<a href="\1">',
        content
    )
    # 修复引号问题
    content = re.sub(
        r'<a\s+href=(/blog/[^>\s]+)\s+class=',
        r'<a href="\1" class=',
        content
    )
    
    # 5. 删除预取旧链接的 JS
    content = re.sub(
        r"var\s+prefetchLinks\s*=\s*document\.querySelectorAll\('\^\?pages/'\)[\s\S]*?\}\);",
        '',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == '__main__':
    if fix_file(HOME):
        print('Fixed: index.html')
    else:
        print('No changes needed: index.html')
