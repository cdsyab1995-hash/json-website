"""
批量更新页面内联 CSS，添加 CLS 优化
- .main-container 添加 min-height
- .feature-card 添加 min-height
"""
import os
import re

pages_dir = r'd:\网站开发-json\pages'
count = 0

for f in os.listdir(pages_dir):
    if not f.endswith('.html'):
        continue
    fp = os.path.join(pages_dir, f)
    
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original = content
    
    # 1. 更新 .main-container 添加 min-height
    # 匹配 .main-container{...} 块
    def replace_main_container(match):
        block = match.group(0)
        # 如果已经有 min-height，跳过
        if 'min-height' in block:
            return block
        # 添加 min-height
        return block.replace(
            'padding:var(--space-xl);width:100%}',
            'padding:var(--space-xl);width:100%;min-height:calc(100vh - 64px - 80px)}'
        )
    
    content = re.sub(r'\.main-container\{[^}]+\}', replace_main_container, content)
    
    # 2. 更新 .feature-card 添加 min-height
    def replace_feature_card(match):
        block = match.group(0)
        # 如果已经有 min-height，跳过
        if 'min-height' in block:
            return block
        # 添加 min-height
        return block.replace(
            'overflow:hidden}',
            'overflow:hidden;min-height:160px}'
        )
    
    content = re.sub(r'\.feature-card\{[^}]+\}', replace_feature_card, content)
    
    if content != original:
        with open(fp, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1
        print(f'Updated: {f}')

print(f'\nTotal pages updated: {count}')
