# -*- coding: utf-8 -*-
"""
修复 P1 工具页面的导航栏 - 添加自己的链接
"""
import os
import re

def get_tools_menu(filename):
    """根据文件名返回正确的工具菜单"""
    
    # P0 工具（始终不变）
    p0_tools = [
        ('regex-tester.html', 'Regex Tester', 'Regex'),
        ('base64.html', 'Base64 Encoder', 'Base64'),
        ('url-encoder.html', 'URL Encoder', 'URL Encoder'),
    ]
    
    # P1 工具
    p1_tools = [
        ('jwt-decoder.html', 'JWT Decoder', 'JWT'),
        ('hash-generator.html', 'Hash Generator', 'Hash Generator'),
        ('uuid-generator.html', 'UUID Generator', 'UUID Generator'),
    ]
    
    target_file = os.path.basename(filename)
    
    # 构建菜单
    menu_items = []
    
    # JSON 工具
    menu_items.append('<a href="format.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg>Format</a>')
    menu_items.append('<a href="escape.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>Escape</a>')
    menu_items.append('<a href="extract.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>Extract</a>')
    menu_items.append('<a href="sort.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="6" x2="20" y2="6"></line><line x1="4" y1="12" x2="14" y2="12"></line><line x1="4" y1="18" x2="9" y2="18"></line></svg>Sort</a>')
    menu_items.append('<a href="clean.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18"></path><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"></path></svg>Clean</a>')
    menu_items.append('<a href="viewer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>Viewer</a>')
    menu_items.append('<a href="compare.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>Compare</a>')
    menu_items.append('<a href="xml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>XML</a>')
    menu_items.append('<a href="yaml.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>YAML</a>')
    
    # CSV/Excel 工具
    menu_items.append('<a href="json2csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>CSV</a>')
    menu_items.append('<a href="csv-to-excel.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line></svg>Excel</a>')
    menu_items.append('<a href="merge-csv.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>Merge</a>')
    menu_items.append('<a href="excel-remove-duplicates.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>Remove Dup</a>')
    menu_items.append('<a href="batch-file-renamer.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>Batch Rename</a>')
    
    # 分隔线
    menu_items.append('<div class="nav-dropdown-divider"></div>')
    
    # P0 开发者工具
    for href, full_name, short_name in p0_tools:
        active = ' class="nav-link active"' if target_file == href else ' class="nav-link"'
        menu_items.append(f'<a href="{href}"{active}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>{short_name}</a>')
    
    # 分隔线
    menu_items.append('<div class="nav-dropdown-divider"></div>')
    
    # P1 开发者工具
    for href, full_name, short_name in p1_tools:
        active = ' class="nav-link active"' if target_file == href else ' class="nav-link"'
        menu_items.append(f'<a href="{href}"{active}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>{short_name}</a>')
    
    # Utilities
    menu_items.append('<a href="pdf-split.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>PDF Split</a>')
    
    return '\n                    '.join(menu_items)


def fix_navbar(filename):
    """修复单个文件的导航栏"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有 nav-dropdown-menu
    idx = content.find('nav-dropdown-menu')
    if idx < 0:
        print(f'{os.path.basename(filename)}: No nav-dropdown-menu found')
        return False
    
    # 找到 nav-dropdown-menu 的开始和结束
    menu_start = content.find('>', idx) + 1
    menu_end = content.find('</div>', menu_start)
    
    if menu_start <= 0 or menu_end <= 0:
        print(f'{os.path.basename(filename)}: Invalid menu structure')
        return False
    
    # 生成新的菜单内容
    new_menu = get_tools_menu(filename)
    
    # 替换
    new_content = content[:menu_start] + new_menu + content[menu_end:]
    
    # 检查是否有变化
    if new_content == content:
        print(f'{os.path.basename(filename)}: No changes needed')
        return False
    
    # 保存
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'{os.path.basename(filename)}: Fixed')
    return True


# 修复三个工具页面
files = [
    r'd:\网站开发-json\pages\hash-generator.html',
    r'd:\网站开发-json\pages\jwt-decoder.html',
    r'd:\网站开发-json\pages\uuid-generator.html',
]

for fp in files:
    fix_navbar(fp)
