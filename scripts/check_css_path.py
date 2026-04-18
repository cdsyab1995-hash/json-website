import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check if styles.css is correctly linked
for fname in ['format.html', 'escape.html']:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find styles.css link
    if '../css/styles.css' in content:
        print(f'{fname}: uses ../css/styles.css')
    elif 'css/styles.css' in content:
        print(f'{fname}: uses css/styles.css')
    else:
        print(f'{fname}: NO styles.css link found!')

# Check root index.html
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if 'css/styles.css' in content:
    print('index.html: uses css/styles.css')
