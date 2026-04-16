#!/usr/bin/env python3
"""
修复 jwt-decoder.html 和 uuid-generator.html 的导航栏
"""
import os

BASE_DIR = r'd:\网站开发-json\pages'

# P1 工具链接模板
P1_LINKS = '''                    <a href="regex-tester.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path>
                        </svg>
                        Regex
                    </a>
                    <a href="base64.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="8" y1="12" x2="16" y2="12"></line>
                        </svg>
                        Base64
                    </a>
                    <a href="url-encoder.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                        </svg>
                        URL Encoder
                    </a>
                    <a href="hash-generator.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="4" y1="9" x2="20" y2="9"></line>
                            <line x1="4" y1="15" x2="20" y2="15"></line>
                            <line x1="10" y1="3" x2="8" y2="21"></line>
                            <line x1="16" y1="3" x2="14" y2="21"></line>
                        </svg>
                        Hash Generator
                    </a>
                    <a href="jwt-decoder.html" class="nav-link active">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>
                        JWT
                    </a>
                    <a href="uuid-generator.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>
                        UUID Generator
                    </a>'''

def fix_file(filename, is_uuid_page=False):
    """修复单个文件"""
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f'[WARN] File not found: {filename}')
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有完整的 P1 链接
    if 'href="regex-tester.html"' in content and 'href="hash-generator.html"' in content:
        print(f'[OK] {filename} already has all P1 links')
        return
    
    # 找到 nav-dropdown-menu 的位置
    dropdown_idx = content.find('nav-dropdown-menu')
    if dropdown_idx < 0:
        print(f'[ERROR] No nav-dropdown-menu in {filename}')
        return
    
    # 找到 PDF Split 链接的位置
    pdf_idx = content.find('href="pdf-split.html"')
    if pdf_idx < 0:
        print(f'[ERROR] No pdf-split.html link in {filename}')
        return
    
    # 找到 pdf-split 链接的结束位置
    pdf_end = content.find('</a>', pdf_idx) + 4
    
    # 构建新的链接内容
    if is_uuid_page:
        new_links = P1_LINKS.replace('jwt-decoder.html" class="nav-link active', 'jwt-decoder.html" class="nav-link')
        new_links = new_links.replace('href="uuid-generator.html" class="nav-link', 'href="uuid-generator.html" class="nav-link active')
    else:
        new_links = P1_LINKS
    
    # 替换内容
    new_content = content[:pdf_end] + '\n' + new_links + content[pdf_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'[OK] Fixed {filename}')

def main():
    print('Fixing JWT and UUID page navbars:')
    print('=' * 50)
    
    fix_file('jwt-decoder.html', is_uuid_page=False)
    fix_file('uuid-generator.html', is_uuid_page=True)
    
    print('=' * 50)

if __name__ == '__main__':
    main()
