import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['jwt-decoder.html', 'css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    
    # Find all nav-related classes
    nav_classes = re.findall(r'<nav[^>]*class="([^"]*)"', content)
    print(f'nav classes: {nav_classes}')
    
    # Find navbar divs
    navbar_divs = re.findall(r'<div[^>]*class="([^"]*navbar[^"]*)"', content, re.IGNORECASE)
    print(f'navbar divs: {navbar_divs}')
    
    # Find the nav structure
    nav_start = content.find('<nav')
    if nav_start >= 0:
        nav_section = content[nav_start:nav_start+2000]
        print(f'nav section (first 1000 chars):\n{nav_section[:1000]}')
