import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

for fname in ['css-minifier.html', 'html-encoder.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {fname} (first 2000 chars) ===')
    print(content[:2000])
