#!/usr/bin/env python3
"""
修复工具页面的导航栏链接
"""
import os

BASE_DIR = r'd:\网站开发-json\pages'

# 需要修复的工具页面及其导航栏链接
TOOL_NAVBAR_FIXES = {
    'hash-generator.html': [
        ('hash-generator.html" class="nav-link active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex',
         'regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex'),
        ('hash-generator.html" class="nav-link active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex',
         'hash-generator.html" class="nav-link active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>Hash Generator'),
    ],
    'jwt-decoder.html': [
        # 需要添加 regex-tester 和其他缺失的链接
    ],
    'uuid-generator.html': [
        # 需要添加 regex-tester 和其他缺失的链接
    ]
}

def fix_navbar(filepath, fixes):
    """修复导航栏"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
            print(f'[OK] Fixed: {os.path.basename(filepath)}')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print('Fixing tool page navbars:')
    print('=' * 50)
    
    # 修复 hash-generator.html
    filepath = os.path.join(BASE_DIR, 'hash-generator.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复 1: 把 "Regex" 链接改为 regex-tester.html
        old_pattern = 'href="hash-generator.html" class="nav-link active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex'
        new_pattern = 'href="regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex'
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            print('[OK] Fixed hash-generator.html: added regex-tester link')
        
        # 修复 2: 添加 hash-generator.html 链接（在 regex-tester 后面）
        regex_link = 'href="regex-tester.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>Regex'
        hash_link = '''href="hash-generator.html" class="nav-link active"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>Hash Generator'''
        
        if regex_link in content and hash_link not in content:
            content = content.replace(regex_link, regex_link + '\n                    ' + hash_link)
            print('[OK] Fixed hash-generator.html: added hash-generator link')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print('=' * 50)

if __name__ == '__main__':
    main()
