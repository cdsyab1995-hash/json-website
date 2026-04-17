# -*- coding: utf-8 -*-
import os
import re

# 修复 pdf-split.html 的 PDF.js 脚本
fp = r'd:\网站开发-json\pages\pdf-split.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# 添加 defer 到 PDF.js 脚本
old = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3'
new = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3'

if new in content:
    # 查找完整标签
    pattern = r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/pdf\.js/3[^"]+"></script>'
    match = re.search(pattern, content)
    if match:
        old_tag = match.group(0)
        new_tag = old_tag.replace('<script ', '<script defer ')
        content = content.replace(old_tag, new_tag)
        
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        print('pdf-split.html: Fixed PDF.js defer')
    else:
        print('pdf-split.html: Script tag not found in expected format')
else:
    print('pdf-split.html: PDF.js script not found')
