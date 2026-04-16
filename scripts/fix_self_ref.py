#!/usr/bin/env python3
"""
修复工具页面缺少自己链接的问题
"""
import os

BASE_DIR = r'd:\网站开发-json\pages'

# 每个工具页面的信息
SELF_LINKS = {
    'hash-generator.html': {
        'name': 'Hash Generator',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="4" y1="9" x2="20" y2="9"></line>
                            <line x1="4" y1="15" x2="20" y2="15"></line>
                            <line x1="10" y1="3" x2="8" y2="21"></line>
                            <line x1="16" y1="3" x2="14" y2="21"></line>
                        </svg>''',
        'after': 'url-encoder.html'
    },
    'jwt-decoder.html': {
        'name': 'JWT',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>''',
        'after': 'hash-generator.html'
    },
    'uuid-generator.html': {
        'name': 'UUID Generator',
        'icon': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>''',
        'after': 'jwt-decoder.html'
    }
}

def fix_self_reference(filepath, tool_info):
    """为工具页面添加自己的链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tool_href = os.path.basename(filepath)
    
    # 检查是否已有自己的链接
    if f'href="{tool_href}"' in content:
        print(f'[OK] {tool_href} already has self link')
        return False
    
    # 在指定工具后添加
    after_href = tool_info['after']
    if f'href="{after_href}"' in content:
        idx = content.find(f'href="{after_href}"')
        end_idx = content.find('</a>', idx) + 4
        
        new_link = f'''
                    <a href="{tool_href}" class="nav-link">
                        {tool_info['icon']}
                        {tool_info['name']}
                    </a>'''
        
        content = content[:end_idx] + new_link + content[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'[OK] Added self link to {tool_href}')
        return True
    
    print(f'[WARN] Could not find {after_href} in {tool_href}')
    return False

def main():
    print('Fixing self-references in tool pages:')
    print('=' * 50)
    
    for filename, info in SELF_LINKS.items():
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            fix_self_reference(filepath, info)
        else:
            print(f'[WARN] File not found: {filename}')
    
    print('=' * 50)

if __name__ == '__main__':
    main()
