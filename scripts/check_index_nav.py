# -*- coding: utf-8 -*-
import re

# 检查 index.html 的导航栏
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 navbar 部分
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>', nav_start) + 6
nav_content = content[nav_start:nav_end]

print('=== index.html 导航栏 ===')
print()

# 提取所有链接
links = re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', nav_content)
for href, text in links:
    text = text.strip()
    if text:
        print(f'{text} -> {href}')
