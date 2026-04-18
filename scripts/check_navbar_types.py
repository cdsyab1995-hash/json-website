#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查导航栏类型：下拉菜单 vs 平铺"""

import os
import re

root_dir = r'd:\网站开发-json'

# 导航栏模式
navbar_patterns = {
    'dropdown': r'<div class="dropdown">.*?</div>\s*</li>',  # 下拉菜单
    'flat_tools': r'<a href="[^"]*"[^>]*>\s*(?:Format|Escape|Extract|Sort|Clean|XML|YAML|CSV|Compare|Viewer|JSON to CSV)',  # 平铺工具链接
}

results = []

# 检查所有HTML文件
for root, dirs, files in os.walk(root_dir):
    # 跳过不需要的目录
    dirs[:] = [d for d in dirs if d not in ['.git', '.workbuddy', 'scripts', 'docs', 'images', 'css', 'js']]
    
    for file in files:
        if not file.endswith('.html'):
            continue
            
        filepath = os.path.join(root, file)
        rel_path = os.path.relpath(filepath, root_dir)
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # 检查导航栏类型
        has_dropdown = bool(re.search(r'<div class="dropdown">', content, re.DOTALL))
        has_flat = bool(re.search(r'<li><a href="[^"]*format[^"]*"[^>]*>Format</a></li>', content, re.DOTALL | re.IGNORECASE))
        
        nav_type = 'dropdown' if has_dropdown else ('flat' if has_flat else 'unknown')
        
        results.append({
            'file': rel_path,
            'type': nav_type,
            'has_dropdown': has_dropdown,
            'has_flat': has_flat
        })

# 按类型分组
print("=" * 60)
print("Navbar Type Statistics")
print("=" * 60)

dropdown_files = [r for r in results if r['type'] == 'dropdown']
flat_files = [r for r in results if r['type'] == 'flat']
unknown_files = [r for r in results if r['type'] == 'unknown']

print(f"\n[PASS] Dropdown: {len(dropdown_files)} files")
for r in dropdown_files[:10]:
    print(f"  - {r['file']}")
if len(dropdown_files) > 10:
    print(f"  ... 还有 {len(dropdown_files)-10} 个")

print(f"\n[WARN] Flat navigation: {len(flat_files)} files")
for r in flat_files:
    print(f"  - {r['file']}")

print(f"\n[UNKNOWN] Unknown type: {len(unknown_files)} files")
for r in unknown_files:
    print(f"  - {r['file']}")

print("\n" + "=" * 60)
print("Recommendation: Use dropdown menu consistently")
print("=" * 60)
