#!/usr/bin/env python3
"""
修复剩余页面的 P1 工具导航栏
"""
import os
import re

PAGES_DIR = r'd:\网站开发-json\pages'

# 要添加的工具信息
NEW_TOOLS = [
    {
        'name': 'JWT',
        'href': 'jwt-decoder.html',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>'''
    },
    {
        'name': 'Hash Generator',
        'href': 'hash-generator.html',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="4" y1="9" x2="20" y2="9"></line>
                            <line x1="4" y1="15" x2="20" y2="15"></line>
                            <line x1="10" y1="3" x2="8" y2="21"></line>
                            <line x1="16" y1="3" x2="14" y2="21"></line>
                        </svg>'''
    },
    {
        'name': 'UUID Generator',
        'href': 'uuid-generator.html',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>'''
    }
]

def update_navbar(content):
    """在 Compare 链接后添加新工具"""
    for tool in NEW_TOOLS:
        tool_href = tool['href']
        if f'href="{tool_href}"' not in content:
            # 尝试在 compare.html 链接后添加
            pattern = 'href="compare.html"'
            if pattern in content:
                idx = content.find(pattern)
                end_idx = content.find('</a>', idx) + 4
                
                new_link = f'''
                    <a href="{tool_href}" class="nav-link">
                        {tool['icon']}
                        {tool['name']}
                    </a>'''
                
                content = content[:end_idx] + new_link + content[end_idx:]
                print(f'[OK] Added {tool["name"]} after Compare')
            else:
                # 如果也没有 compare，在 PDF Split 后添加
                pattern = 'href="pdf-split.html"'
                if pattern in content:
                    idx = content.find(pattern)
                    end_idx = content.find('</a>', idx) + 4
                    
                    new_link = f'''
                    <a href="{tool_href}" class="nav-link">
                        {tool['icon']}
                        {tool['name']}
                    </a>'''
                    
                    content = content[:end_idx] + new_link + content[end_idx:]
                    print(f'[OK] Added {tool["name"]} after PDF Split')
                else:
                    print(f'[WARN] Could not find anchor for {tool["name"]}')
    return content

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = update_navbar(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    files_to_fix = [
        r'd:\网站开发-json\pages\about.html',
        r'd:\网站开发-json\pages\blog.html',
        r'd:\网站开发-json\pages\news.html'
    ]
    
    print('=' * 50)
    print('Fixing remaining P1 Navigation Bars')
    print('=' * 50)
    
    for fp in files_to_fix:
        print(f'\nProcessing: {os.path.basename(fp)}')
        process_file(fp)
    
    print('=' * 50)

if __name__ == '__main__':
    main()
