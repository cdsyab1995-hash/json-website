import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['jwt-decoder.html', 'css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    
    # Find navbar
    start = content.find('<div class="navbar-links">')
    end = content.find('</div>', content.find('<div class="navbar-links">'))
    print(f'navbar-links start: {start}, end: {end}')
    
    # Check for the end pattern
    nav_end = content.find('</div>\n    </nav>', start)
    nav_end2 = content.find('</div>\n\n    </nav>', start)
    nav_end3 = content.find('</div>\n\n\n    </nav>', start)
    print(f'nav end patterns: {nav_end}, {nav_end2}, {nav_end3}')
    
    # Show first 500 chars of navbar
    if start > 0:
        navbar = content[start:start+500]
        print(navbar)
