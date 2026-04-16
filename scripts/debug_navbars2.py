import re

def check_navbar(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu = content[idx:idx+10000]
        
        # Simple pattern - find text between </svg> and </a>
        pattern = r'</svg>\s*([^<]+)</a>'
        matches = re.findall(pattern, menu)
        
        print(f'\n{name}:')
        print(f'  Total: {len(matches)} items')
        for i, tool_name in enumerate(matches, 1):
            print(f'    {i}. {tool_name.strip()}')
        
        # Check for specific missing tools
        standard = ['Format', 'Escape', 'Extract', 'Sort', 'Clean', 'XML', 'YAML', 'Viewer', 
                    'CSV', 'Excel', 'Remove Duplicates', 'Merge CSV', 'Batch Rename', 'PDF Split', 'Compare']
        
        missing = []
        for tool in standard:
            found = any(tool.lower() == m.strip().lower() for m in matches)
            if not found:
                missing.append(tool)
        
        if missing:
            print(f'  MISSING: {missing}')
        else:
            print(f'  COMPLETE - all 15 tools present')
    else:
        print(f'{name}: No nav-dropdown-menu found')

check_navbar(r'd:\网站开发-json\index.html', 'index.html (Home)')
check_navbar(r'd:\网站开发-json\pages\compare.html', 'compare.html')
