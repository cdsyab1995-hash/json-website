import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} ===')
    print(f'Total length: {len(content)} chars')
    
    # Find body tag and show content around it
    body_start = content.find('<body>')
    if body_start >= 0:
        print(f'Body starts at: {body_start}')
        # Show next 1500 chars
        print(content[body_start:body_start+1500])
