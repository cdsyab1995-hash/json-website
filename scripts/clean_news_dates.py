# -*- coding: utf-8 -*-
"""
清理 news 文章中的日期格式问题
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

NEWS_DIR = r'd:\网站开发-json\news'

def clean_article(filepath):
    """清理文章中的日期格式问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有需要清理的问题
    if '</span></span>' in content or '</span>",' in content or '</span>",\n' in content:
        print(f'  [CLEAN] {os.path.basename(os.path.dirname(filepath))}')
        
        # 修复双重 </span></span>
        content = content.replace('</span></span>', '</span>')
        
        # 修复 JSON-LD 中的 </span>
        content = re.sub(
            r'"datePublished":\s*"([^"]*)</span>"',
            lambda m: f'"datePublished": "{m.group(1)}"',
            content
        )
        
        # 修复 article-meta 中的双重 </span>
        content = re.sub(
            r'(<span>Published:\s*[^<]+)</span></span>',
            r'\1</span>',
            content
        )
        
        # 清理 article-body 开头的空白和重复 meta
        content = re.sub(
            r'<div class="article-body">\s*<div class="article-meta">.*?</div>\s*',
            '<div class="article-body">\n                ',
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print('=' * 50)
    print('Cleaning News Article Date Formats')
    print('=' * 50)
    
    cleaned = 0
    for root, dirs, files in os.walk(NEWS_DIR):
        for file in files:
            if file == 'index.html':
                filepath = os.path.join(root, file)
                if filepath != os.path.join(NEWS_DIR, 'index.html'):
                    if clean_article(filepath):
                        cleaned += 1
    
    print(f'\nCleaned {cleaned} articles!')

if __name__ == '__main__':
    main()
