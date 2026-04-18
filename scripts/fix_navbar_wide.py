import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

# All HTML files that need fixing
files_to_fix = []

pages_dir = r'd:\网站开发-json\pages'
for root, dirs, filenames in os.walk(pages_dir):
    for f in filenames:
        if f.endswith('.html'):
            files_to_fix.append(os.path.join(root, f))

# Also index.html
files_to_fix.append(r'd:\网站开发-json\index.html')

fixed = 0
errors = []
for path in sorted(files_to_fix):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only fix if it has nav-dropdown-menu but NOT wide
    if 'nav-dropdown-menu' in content and 'nav-dropdown-menu wide' not in content:
        old = 'class="nav-dropdown-menu"'
        new = 'class="nav-dropdown-menu wide"'
        if old in content:
            content = content.replace(old, new, 1)  # Only first occurrence
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
            print(f'Fixed: {os.path.relpath(path, r"d:\\网站开发-json")}')
        else:
            # Try to find what class is actually there
            m = re.search(r'<div[^>]*class="([^"]*nav-dropdown-menu[^"]*)"', content)
            if m:
                errors.append(f'{os.path.basename(path)}: unexpected class = "{m.group(1)}"')

print(f'\nTotal fixed: {fixed}')
if errors:
    print('Errors:')
    for e in errors:
        print(' ', e)
