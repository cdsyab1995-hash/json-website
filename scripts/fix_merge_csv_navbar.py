#!/usr/bin/env python3
"""修复 merge-csv.html 导航栏 - 添加缺失的工具链接"""
import re

fp = r'd:\网站开发-json\pages\merge-csv.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找 merge-csv.html 链接的结束位置
pattern = r'(<a href="merge-csv\.html"[^>]*>.*?</svg>\s*Merge CSV\s*</a>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    
    # 要插入的内容
    new_links = '''
                    <a href="batch-file-renamer.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>
                        Batch Rename
                    </a>
                    <a href="pdf-split.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="12" y1="18" x2="12" y2="12"></line>
                            <line x1="9" y1="15" x2="15" y2="15"></line>
                        </svg>
                        PDF Split
                    </a>'''
    
    new_content = content[:insert_pos] + new_links + content[insert_pos:]
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Updated merge-csv.html - added Batch Rename, PDF Split')
else:
    print('Could not find merge-csv.html link in merge-csv.html')
