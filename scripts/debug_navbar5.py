import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} nav-links section ===')
    
    start = content.find('<div class="nav-links">')
    if start >= 0:
        nav_end = content.find('</div>\n        </header>', start)
        if nav_end >= 0:
            navbar = content[start:nav_end + len('</div>')]
            # Show first 2000 chars
            print(navbar[:2000])
            
            # Check what links are in the nav
            links = re.findall(r'href="([^"]*)"[^>]*>([^<]*)</a>', navbar)
            print(f'\nLinks found ({len(links)}):')
            for href, text in links:
                print(f'  {text.strip()}: {href}')
        else:
            print('Could not find nav end')
    else:
        print('No nav-links found')
