import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check the full navbar content for css-minifier and html-encoder
for fname in ['css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} header content ===')
    
    start = content.find('<header class="navbar">')
    if start >= 0:
        end = content.find('</header>', start)
        header = content[start:end + len('</header>')]
        
        # Find nav-items (each dropdown item)
        nav_items = re.findall(r'<a href="([^"]*)" class="nav-link"', header)
        print(f'Nav items ({len(nav_items)}):')
        for item in nav_items:
            print(f'  - {item}')
        
        # Find all nav text labels
        nav_texts = re.findall(r'class="nav-label">([^<]*)</span>', header)
        print(f'Nav labels: {nav_texts}')
