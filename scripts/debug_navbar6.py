import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    
    # Find header class
    start = content.find('<header class="navbar">')
    if start >= 0:
        # Find the closing of the header (</header>)
        header_end = content.find('</header>', start)
        if header_end >= 0:
            header_content = content[start:header_end + len('</header>')]
            print(f'Header length: {len(header_content)}')
            
            # Find all links in the header
            links = re.findall(r'href="([^"]*)"', header_content)
            texts = re.findall(r'>([^<]{2,30})</[a]', header_content)
            
            print(f'Links in navbar: {links}')
            print(f'Texts in navbar: {texts}')
