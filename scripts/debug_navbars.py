import re

def check_navbar(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    idx = content.find('nav-dropdown-menu')
    if idx >= 0:
        menu = content[idx:idx+10000]
        
        # Extract all tool names
        # Pattern: href="..." ... >Name</a>
        pattern = r'href="[^"]*\.html"[^>]*>[^<]*<svg[^>]*>[^<]*</svg>\s*([^<]+)'
        matches = re.findall(pattern, menu)
        
        print(f'\n{name}:')
        print(f'  Total: {len(matches)} tools')
        for i, name in enumerate(matches, 1):
            print(f'    {i}. {name.strip()}')
        
        # Check for specific missing tools
        standard = ['Format', 'Escape', 'Extract', 'Sort', 'Clean', 'XML', 'YAML', 'Viewer', 
                    'CSV', 'Excel', 'Remove Duplicates', 'Merge CSV', 'Batch Rename', 'PDF Split', 'Compare']
        
        missing = []
        for tool in standard:
            found = any(tool.lower() in m.lower() for m in matches)
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
