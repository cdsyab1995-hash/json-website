# -*- coding: utf-8 -*-
"""
修复 P1 工具页面的导航栏 - 添加完整工具列表
"""
import os
import re

def get_tools_menu(filename):
    """根据文件名返回完整的工具菜单"""
    
    target_file = os.path.basename(filename)
    
    # 构建菜单
    menu_items = []
    
    # JSON 工具
    json_tools = [
        ('format.html', 'Format', 'Format'),
        ('escape.html', 'Escape', 'Escape'),
        ('extract.html', 'Extract', 'Extract'),
        ('sort.html', 'Sort', 'Sort'),
        ('clean.html', 'Clean', 'Clean'),
        ('viewer.html', 'Viewer', 'Viewer'),
        ('compare.html', 'Compare', 'Compare'),
        ('xml.html', 'XML', 'XML'),
        ('yaml.html', 'YAML', 'YAML'),
    ]
    
    csv_tools = [
        ('json2csv.html', 'CSV', 'CSV'),
        ('csv-to-excel.html', 'Excel', 'Excel'),
        ('excel-remove-duplicates.html', 'Remove Duplicates', 'Remove Duplicates'),
        ('merge-csv.html', 'Merge CSV', 'Merge CSV'),
        ('batch-file-renamer.html', 'Batch Rename', 'Batch Rename'),
    ]
    
    dev_tools = [
        ('regex-tester.html', 'Regex', 'Regex'),
        ('base64.html', 'Base64', 'Base64'),
        ('url-encoder.html', 'URL Encoder', 'URL Encoder'),
        ('jwt-decoder.html', 'JWT', 'JWT'),
        ('hash-generator.html', 'Hash Generator', 'Hash Generator'),
        ('uuid-generator.html', 'UUID Generator', 'UUID Generator'),
    ]
    
    # SVG 图标映射
    icons = {
        'Format': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg>',
        'Escape': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
        'Extract': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
        'Sort': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>',
        'Clean': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>',
        'Viewer': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>',
        'Compare': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>',
        'XML': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>',
        'YAML': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
        'CSV': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>',
        'Excel': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line></svg>',
        'Remove Duplicates': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>',
        'Merge CSV': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>',
        'Batch Rename': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>',
        'Regex': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
        'Base64': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
        'URL Encoder': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
        'JWT': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>',
        'Hash Generator': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>',
        'UUID Generator': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>',
        'PDF Split': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>',
    }
    
    # 添加 JSON 工具
    for href, full_name, short_name in json_tools:
        active = ' class="nav-link active"' if target_file == href else ' class="nav-link"'
        icon = icons.get(short_name, '')
        menu_items.append(f'<a href="{href}"{active}>{icon}{short_name}</a>')
    
    menu_items.append('<div class="nav-dropdown-divider"></div>')
    
    # 添加 CSV/Excel 工具
    for href, full_name, short_name in csv_tools:
        active = ' class="nav-link active"' if target_file == href else ' class="nav-link"'
        icon = icons.get(short_name, '')
        menu_items.append(f'<a href="{href}"{active}>{icon}{short_name}</a>')
    
    menu_items.append('<div class="nav-dropdown-divider"></div>')
    
    # 添加开发者工具
    for href, full_name, short_name in dev_tools:
        active = ' class="nav-link active"' if target_file == href else ' class="nav-link"'
        icon = icons.get(short_name, '')
        menu_items.append(f'<a href="{href}"{active}>{icon}{short_name}</a>')
    
    menu_items.append('<div class="nav-dropdown-divider"></div>')
    
    # 添加 Utilities
    menu_items.append(f'<a href="pdf-split.html" class="nav-link">{icons["PDF Split"]}PDF Split</a>')
    
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
    
    # 正确找到匹配的 </div>
    depth = 1
    pos = menu_start
    while depth > 0 and pos < len(content):
        if content[pos:pos+5] == '<div ':
            depth += 1
            pos += 5
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                break
            pos += 6
        else:
            pos += 1
    
    menu_end = pos
    
    if menu_start <= 0 or menu_end <= menu_start:
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
