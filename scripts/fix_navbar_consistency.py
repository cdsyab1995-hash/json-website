#!/usr/bin/env python3
"""
统一所有页面的导航栏 - 添加 Best Practices 链接
"""
import os
import re

# 目标目录
BASE_DIR = r'd:\网站开发-json'

# 标准导航栏 HTML (从 index.html 获取)
NAVBAR_TEMPLATE = '''
        <div class="navbar-links">
            <a href="../index.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Home
            </a>
            <!-- Tools Dropdown -->
            <div class="nav-dropdown">
                <a href="#" class="nav-link nav-dropdown-toggle">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"></rect>
                        <rect x="14" y="3" width="7" height="7"></rect>
                        <rect x="14" y="14" width="7" height="7"></rect>
                        <rect x="3" y="14" width="7" height="7"></rect>
                    </svg>
                    Tools
                </a>
                <div class="nav-dropdown-menu">
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
            <a href="blog.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Tutorial
            </a>
            <a href="best-practices.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Best Practices
            </a>
            <a href="news.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                News
            </a>
            <a href="about.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
                About
            </a>
            <!-- CTA Button -->
            <a href="format.html" class="nav-link navbar-cta">
                Try Formatter
            </a>
        </div>
'''

# pages/ 子目录中的页面列表
TOOL_PAGES = [
    'format.html', 'escape.html', 'extract.html', 'sort.html', 'clean.html',
    'xml.html', 'yaml.html', 'viewer.html', 'json2csv.html', 'compare.html',
    'best-practices.html', 'blog.html', 'news.html', 'about.html', 'changelog.html'
]

def get_navbar_html(page_name, is_tool_page=True):
    """根据页面名称生成正确的导航栏 HTML"""
    
    # Home 链接
    home_link = '../index.html' if page_name else 'index.html'
    
    # 工具页面使用相对路径
    tools_prefix = '' if page_name else ''
    
    return NAVBAR_TEMPLATE

def update_page_navbar(file_path, page_category):
    """更新单个页面的导航栏"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 Best Practices 链接
    if 'best-practices.html' in content:
        print(f"  [OK] {os.path.basename(file_path)} already has Best Practices")
        return False
    
    # 查找导航栏位置
    nav_match = re.search(r'<div class="navbar-links">(.*?)</div>\s*</nav>', content, re.DOTALL)
    if not nav_match:
        print(f"  [X] {os.path.basename(file_path)} - No navbar-links found")
        return False
    
    # 检查页面是否有下拉菜单
    if 'nav-dropdown' in content:
        # 有下拉菜单 - 只需要在适当位置添加 Best Practices
        # 找到 Tutorial 和 News 之间添加
        pattern = r'(<a href="blog\.html"[^>]*>.*?Tutorial.*?</a>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            tutorial_link = match.group(1)
            best_practices_link = '''
            <a href="best-practices.html" class="nav-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Best Practices
            </a>'''
            new_content = content.replace(tutorial_link, tutorial_link + best_practices_link)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  [OK] {os.path.basename(file_path)} - Added Best Practices after Tutorial")
            return True
    
    print(f"  - {os.path.basename(file_path)} - Skipped (different structure)")
    return False

def main():
    print("[FIX] Fix navbar consistency - add Best Practices link\n")
    
    pages_dir = os.path.join(BASE_DIR, 'pages')
    updated_count = 0
    
    # 更新 pages/ 目录下的所有 HTML 文件
    print("检查 pages/ 目录下的页面...")
    for filename in os.listdir(pages_dir):
        if filename.endswith('.html') and os.path.isfile(os.path.join(pages_dir, filename)):
            file_path = os.path.join(pages_dir, filename)
            if update_page_navbar(file_path, 'pages'):
                updated_count += 1
    
    # 更新根目录下的页面
    print("\n检查根目录下的页面...")
    root_pages = ['index.html', 'cookie.html', 'privacy.html', 'terms.html']
    for filename in root_pages:
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.exists(file_path):
            if filename == 'index.html':
                # index.html 已有完整导航栏
                print(f"  [OK] {filename} already has complete navbar")
            elif 'best-practices.html' in open(file_path, 'r', encoding='utf-8').read():
                print(f"  ✓ {filename} already has Best Practices")
            else:
                print(f"  - {filename} - External pages, needs manual check")
    
    # 更新子目录中的页面
    print("\n检查子目录页面 (blog/, news/)...")
    for subdir in ['blog', 'news']:
        subdir_path = os.path.join(pages_dir, subdir)
        if os.path.exists(subdir_path):
            for filename in os.listdir(subdir_path):
                if filename.endswith('.html'):
                    file_path = os.path.join(subdir_path, filename)
                    if update_page_navbar(file_path, subdir):
                        updated_count += 1
    
    print(f"\n[DONE] Updated {updated_count} pages")

if __name__ == '__main__':
    main()
