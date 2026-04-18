import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
html_files = []
for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))
# Also check index.html
html_files.append(r'd:\网站开发-json\index.html')

print('=== Tools Dropdown 类名检查 ===\n')
for path in sorted(html_files):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find nav-dropdown-menu class
    match = re.search(r'<div[^>]*class="([^"]*nav-dropdown-menu[^"]*)"', content)
    if match:
        classes = match.group(1)
        filename = os.path.basename(path)
        has_wide = 'wide' in classes
        print(f'{filename:40s} | classes: {classes}')
        if not has_wide:
            print(f'  ^^^ MISSING "wide" class!')
