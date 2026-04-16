import re

# Fix index.html
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Compare link and add the missing tools after it
compare_pattern = r'(<a href="pages/compare\.html" class="nav-link">.*?</svg>\s*Compare\s*</a>\s*)(</div>\s*</div>)'

replacement = r'''\1
                    <a href="pages/csv-to-excel.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>
                        Excel
                    </a>
                    <a href="pages/excel-remove-duplicates.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        Remove Duplicates
                    </a>
                    <a href="pages/merge-csv.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path>
                            <path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path>
                        </svg>
                        Merge CSV
                    </a>
                    <a href="pages/batch-file-renamer.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>
                        Batch Rename
                    </a>
                    <a href="pages/pdf-split.html" class="nav-link">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="12" y1="18" x2="12" y2="12"></line>
                            <line x1="9" y1="15" x2="15" y2="15"></line>
                        </svg>
                        PDF Split
                    </a>
                \2'''

new_content = re.sub(compare_pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    with open(r'd:\网站开发-json\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('[OK] index.html fixed - added 5 missing tools to Tools dropdown')
else:
    print('[WARN] index.html - Compare link pattern not found')

# Verify
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count tool links in dropdown
idx = content.find('nav-dropdown-menu')
if idx >= 0:
    menu = content[idx:idx+8000]
    links = re.findall(r'href="pages/([^"]+)\.html"', menu)
    print(f'index.html Tools dropdown now has {len(links)} tools')
