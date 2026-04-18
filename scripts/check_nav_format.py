import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['blog.html', 'hash-generator.html']:
    fpath = os.path.join(pages_dir, fname)
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find nav section
    nav_start = content.find('<nav class="navbar">')
    nav_end = content.find('</nav>')
    
    if nav_start > 0 and nav_end > 0:
        navbar = content[nav_start:nav_end]
        
        # Find best-practices
        pos = navbar.find('best-practices')
        if pos > 0:
            start = max(0, pos - 200)
            print(f'=== {fname} - before best-practices ===')
            print(repr(navbar[start:pos+50]))
