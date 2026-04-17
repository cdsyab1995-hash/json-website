# -*- coding: utf-8 -*-
import re

# 检查 index.html 的导航栏
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 navbar 部分
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>', nav_start) + 6
nav_content = content[nav_start:nav_end]

print('=== index.html 导航栏完整内容 ===')
print()
print(nav_content[:3000])
print()
print('...' if len(nav_content) > 3000 else '')
