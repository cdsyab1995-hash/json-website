# -*- coding: utf-8 -*-
import os

pages_dir = r'd:\网站开发-json\pages'

# Pattern to add new tools before Compare
old_pattern = '''Remove Duplicates
                </a>
                <a href="compare.html" class="nav-link">'''

new_pattern = '''Remove Duplicates
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
                </a>
                <a href="compare.html" class="nav-link">'''

count = 0

for f in os.listdir(pages_dir):
    if not f.endswith('.html'):
        continue
    if f in ['merge-csv.html', 'batch-file-renamer.html', 'pdf-split.html']:
        continue
    
    fp = os.path.join(pages_dir, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if has Remove Duplicates but not Merge CSV
    if 'excel-remove-duplicates.html' in content and 'merge-csv.html' not in content:
        new_content = content.replace(old_pattern, new_pattern)
        if new_content != content:
            with open(fp, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print(f'Updated: {f}')

print(f'\nTotal pages updated: {count}')
