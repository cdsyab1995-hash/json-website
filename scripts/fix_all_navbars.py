import re

def fix_navbar(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Define all 15 tools with their icons
    tools_to_add = {
        'csv-to-excel': {
            'name': 'Excel',
            'svg': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="3" y1="9" x2="21" y2="9"></line>
                            <line x1="9" y1="21" x2="9" y2="9"></line>
                        </svg>'''
        },
        'excel-remove-duplicates': {
            'name': 'Remove Duplicates',
            'svg': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>'''
        },
        'merge-csv': {
            'name': 'Merge CSV',
            'svg': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path>
                            <path d="M8 12v4a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2H10a2 2 0 0 0-2 2"></path>
                        </svg>'''
        },
        'batch-file-renamer': {
            'name': 'Batch Rename',
            'svg': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                        </svg>'''
        },
        'pdf-split': {
            'name': 'PDF Split',
            'svg': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="12" y1="18" x2="12" y2="12"></line>
                            <line x1="9" y1="15" x2="15" y2="15"></line>
                        </svg>'''
        }
    }
    
    # Check which tools are missing
    for tool_key, tool_info in tools_to_add.items():
        href = f'href="{tool_key}.html"' if 'pages' not in filepath else f'href="pages/{tool_key}.html"'
        
        if tool_key not in content:
            # Find a good place to insert - after Compare link
            insert_after = 'pages/compare.html' if 'pages' not in filepath else 'compare.html'
            
            if insert_after in content:
                # Find the Compare link and insert after it
                compare_idx = content.find(insert_after)
                # Find the end of this link's </a> tag
                end_a_idx = content.find('</a>', compare_idx)
                if end_a_idx > 0:
                    insert_point = end_a_idx + 4
                    
                    link_html = f'''
                    <a href="{tool_key}.html" class="nav-link">
                        {tool_info['svg']}
                        {tool_info['name']}
                    </a>'''
                    
                    content = content[:insert_point] + link_html + content[insert_point:]
                    print(f'  Added: {tool_info["name"]}')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[OK] {name} fixed')
    else:
        print(f'[OK] {name} - no changes needed')
    
    # Count tools
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu = content[idx:idx+8000]
        links = re.findall(r'href="[^"]*\.html"', menu)
        print(f'  Total links in dropdown: {len(links)}')

# Fix index.html
print('Fixing index.html...')
fix_navbar(r'd:\网站开发-json\index.html', 'index.html (Home)')

# Fix compare.html
print('\nFixing compare.html...')
fix_navbar(r'd:\网站开发-json\pages\compare.html', 'compare.html')

print('\nDone!')
