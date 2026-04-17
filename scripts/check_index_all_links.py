# -*- coding: utf-8 -*-
import re

# 检查 index.html 的所有链接
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 navbar 部分
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>', nav_start) + 6
nav_content = content[nav_start:nav_end]

print('=== index.html 导航栏所有链接 ===')
print()

# 提取所有链接（包括带 SVG 的）
links = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', nav_content, re.DOTALL)
for href, text in links:
    # 清理文本
    text_clean = ' '.join(text.split())
    text_clean = text_clean.replace('\n', ' ').strip()
    # 移除 SVG
    text_clean = re.sub(r'<svg[^>]*>.*?</svg>', '', text_clean)
    text_clean = text_clean.strip()
    if text_clean:
        print(f'{text_clean} -> {href}')

print()
print('=== 检查是否有 Blog/News ===')
if 'blog' in nav_content.lower():
    print('包含 blog 链接')
else:
    print('不包含 blog 链接')

if 'news' in nav_content.lower():
    print('包含 news 链接')
else:
    print('不包含 news 链接')
