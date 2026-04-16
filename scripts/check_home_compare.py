import os
import re

# 检查 index.html 和 compare.html
files = [
    r'd:\网站开发-json\index.html',
    r'd:\网站开发-json\pages\compare.html'
]

standard_tools = [
    'format', 'escape', 'extract', 'sort', 'clean',
    'xml', 'yaml', 'viewer',
    'json2csv', 'csv-to-excel', 'excel-remove-duplicates', 'merge-csv',
    'batch-file-renamer', 'pdf-split', 'compare'
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找 Tools 下拉菜单中的链接数量
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        # 提取菜单内容
        menu = content[idx:idx+8000]
        # 计算链接数
        links = re.findall(r'href="([^"]+)\.html"', menu)
        print(f'{os.path.basename(fp)}: {len(links)} 工具链接')
        for l in links:
            print(f'  - {l}')
        
        # 检查缺失
        missing = [t for t in standard_tools if t not in links]
        if missing:
            print(f'  缺失: {missing}')
    else:
        print(f'{os.path.basename(fp)}: 未找到 nav-dropdown-menu')
    print()
