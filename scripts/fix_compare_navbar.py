#!/usr/bin/env python3
"""修复 compare.html 导航栏 - 添加缺失的工具链接"""
import re

fp = r'd:\网站开发-json\pages\compare.html'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找 json2csv.html 链接的结束位置
pattern = r'(<a href="json2csv\.html"[^>]*>.*?</svg>\s*CSV\s*</a>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    
    # 要插入的内容
    new_links = '''
                    <a href="csv-to-excel.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>
                        Excel
                    </a>
                    <a href="excel-remove-duplicates.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        Remove Duplicates
                    </a>
                    <a href="merge-csv.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path>
                            <path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path>
                        </svg>
                        Merge CSV
                    </a>
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
    
    print('Updated compare.html - added Excel, Remove Duplicates, Merge CSV, Batch Rename, PDF Split')
else:
    print('Could not find json2csv.html link in compare.html')
