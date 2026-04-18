#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统一所有页面使用下拉菜单导航"""

import os
import re

# 下拉菜单模板
DROPDOWN_TEMPLATE = '''<div class="nav-dropdown">
                    <a href="#" class="nav-link nav-dropdown-toggle">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="7" height="7"></rect>
                            <rect x="14" y="3" width="7" height="7"></rect>
                            <rect x="14" y="14" width="7" height="7"></rect>
                            <rect x="3" y="14" width="7" height="7"></rect>
                        </svg>
                        Tools
                        <svg class="chevron-down" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu wide">
                        <div class="nav-dropdown-menu-box">
                            <a href="format.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="4 7 4 4 20 4 20 7"></polyline>
                                    <line x1="9" y1="20" x2="15" y2="20"></line>
                                    <line x1="12" y1="4" x2="12" y2="20"></line>
                                </svg>
                                Format
                            </a>
                            <a href="escape.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="16 18 22 12 16 6"></polyline>
                                    <polyline points="8 6 2 12 8 18"></polyline>
                                </svg>
                                Escape
                            </a>
                            <a href="extract.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="11" cy="11" r="8"></circle>
                                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                                </svg>
                                Extract
                            </a>
                            <a href="sort.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <line x1="12" y1="5" x2="12" y2="19"></line>
                                    <polyline points="19 12 12 19 5 12"></polyline>
                                </svg>
                                Sort
                            </a>
                            <a href="clean.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                                </svg>
                                Clean
                            </a>
                            <a href="xml.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
                                </svg>
                                XML
                            </a>
                            <a href="yaml.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M4 4l4 16 4-16"></path>
                                    <path d="M12 4l4 16"></path>
                                </svg>
                                YAML
                            </a>
                            <a href="viewer.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                    <circle cx="12" cy="12" r="3"></circle>
                                </svg>
                                Viewer
                            </a>
                            <a href="json2csv.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                    <polyline points="14 2 14 8 20 8"></polyline>
                                    <line x1="8" y1="13" x2="16" y2="13"></line>
                                    <line x1="8" y1="17" x2="16" y2="17"></line>
                                </svg>
                                CSV
                            </a>
                            <a href="compare.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M16 3h5v5"></path>
                                    <path d="M8 3H3v5"></path>
                                    <path d="M21 3l-7 7"></path>
                                    <path d="M3 3l7 7"></path>
                                    <path d="M16 21h5v-5"></path>
                                    <path d="M8 21H3v-5"></path>
                                    <path d="M21 21l-7-7"></path>
                                    <path d="M3 21l7-7"></path>
                                </svg>
                                Compare
                            </a>
                        </div>
                    </div>
                </div>'''

def get_navbar_template(is_root=True):
    """根据页面位置返回导航栏模板"""
    prefix = '' if is_root else '../'
    
    tools_html = DROPDOWN_TEMPLATE.replace('href="', f'href="{prefix}')
    
    return f'''<a href="{prefix}index.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                            <polyline points="9 22 9 12 15 12 15 22"></polyline>
                        </svg>
                        Home
                    </a>
                    {tools_html}
                    <a href="{prefix}pages/blog.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                        </svg>
                        Tutorial
                    </a>
                    <a href="{prefix}pages/best-practices.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        Practices
                    </a>
                    <a href="{prefix}pages/news.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                        </svg>
                        News
                    </a>
                    <a href="{prefix}pages/about.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <line x1="12" y1="16" x2="12" y2="12"></line>
                            <line x1="12" y1="8" x2="12.01" y2="8"></line>
                        </svg>
                        About
                    </a>
                    <a href="{prefix}pages/changelog.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        Changelog
                    </a>
                    <a href="{prefix}pages/format.html" class="nav-link cta">Try Formatter</a>'''

def fix_flat_navbar(filepath):
    """修复平铺导航栏为下拉菜单"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经是下拉菜单
    if 'nav-dropdown-menu wide' in content:
        return False
    
    # 确定路径前缀（根目录 vs pages/ 子目录）
    is_root = '\\pages\\' not in filepath
    prefix = '' if is_root else '../'
    
    # 生成新的导航栏
    new_navbar = get_navbar_template(is_root)
    
    # 匹配旧的平铺导航栏
    # 找到 <div class="navbar-links"> 后面的所有 <a href="... class="nav-link"> 直到 </div>
    pattern = r'<div class="navbar-links">.*?</div>\s*</nav>'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_navbar = match.group(0)
        # 保留 Theme Toggle 按钮
        theme_toggle = ''
        theme_match = re.search(r'<button class="theme-toggle".*?</button>', content, re.DOTALL)
        if theme_match:
            theme_toggle = '\n' + theme_match.group(0)
        
        # 构建新的导航栏
        new_content = content.replace(old_navbar, '<div class="navbar-links">\n' + new_navbar + theme_toggle + '\n</div>\n</nav>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    return False

def main():
    root_dir = r'd:\网站开发-json'
    
    # 需要修复的文件
    files_to_fix = [
        r'd:\网站开发-json\cookie.html',
        r'd:\网站开发-json\privacy.html',
        r'd:\网站开发-json\terms.html',
        r'd:\网站开发-json\pages\news\api-transformations-2026.html',
        r'd:\网站开发-json\pages\news\json-schema-w3c-recommendation.html',
    ]
    
    fixed = []
    for filepath in files_to_fix:
        if os.path.exists(filepath):
            if fix_flat_navbar(filepath):
                fixed.append(os.path.relpath(filepath, root_dir))
    
    print('=' * 50)
    print('Navbar Uniformity Fix Complete')
    print('=' * 50)
    print(f'Fixed: {len(fixed)} files')
    for f in fixed:
        print(f'  - {f}')

if __name__ == '__main__':
    main()
