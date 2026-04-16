# -*- coding: utf-8 -*-
import os

# 查看 hash-generator.html 的 <nav class="navbar"> 到 </nav> 的内容
fp = r'd:\网站开发-json\pages\hash-generator.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 navbar 的位置
nav_idx = content.find('<nav class="navbar">')
print(f'navbar at: {nav_idx}')

# 看看 navbar 开始到 nav-dropdown-menu 的内容
if nav_idx >= 0:
    nav_end = content.find('</nav>', nav_idx)
    nav_content = content[nav_idx:nav_end]
    print('Navbar content (first 2000 chars):')
    print(nav_content[:2000])
    print('...')
    print(f'Navbar length: {len(nav_content)}')
    
    # 检查是否有问题
    if '</head>' in nav_content:
        print('ERROR: </head> found in navbar!')
    if '<head' in nav_content:
        print('ERROR: <head> found in navbar!')
        
    # 检查是否有多余的 nav-dropdown-menu
    count = nav_content.count('nav-dropdown-menu')
    print(f'nav-dropdown-menu count in navbar: {count}')
