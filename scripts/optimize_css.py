#!/usr/bin/env python3
"""
精简内联样式 - 找出重复的内联样式并建议 CSS 类
"""
import re
import sys
import os
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'

# 找出所有内联样式
all_inline_styles = []

for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join(root, filename)
        rel_path = os.path.relpath(filepath, root_dir)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取内联样式
        styles = re.findall(r'style="([^"]+)"', content)
        for style in styles:
            style_clean = style.strip()
            if style_clean:
                all_inline_styles.append((rel_path, style_clean))

# 统计重复的样式
style_counter = Counter([s[1] for s in all_inline_styles])
duplicates = {k: v for k, v in style_counter.items() if v >= 2 and len(k) > 20}

print('Repeated inline styles (can be extracted to CSS classes):\n')
for style, count in sorted(duplicates.items(), key=lambda x: -x[1])[:20]:
    print(f'Used {count} times:')
    print(f'  {style[:80]}...' if len(style) > 80 else f'  {style}')
    print()

# 找出最常见的样式属性组合
common_patterns = Counter()
for path, style in all_inline_styles:
    # 提取关键属性
    props = re.findall(r'([^:]+):[^;]+;?', style)
    pattern = ', '.join(sorted([p.strip() for p in props if p.strip()]))
    if len(pattern) > 10:
        common_patterns[pattern] += 1

print('\nMost common style property combinations:')
for pattern, count in common_patterns.most_common(10):
    if count >= 5:
        print(f'  {count}x: {pattern[:60]}')
