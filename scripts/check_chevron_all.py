import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
has_chevron = []
no_chevron = []

for fname in os.listdir(pages_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(pages_dir, fname)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'chevron-down' in content:
        has_chevron.append(fname)
    else:
        no_chevron.append(fname)

print(f'Pages with chevron-down: {len(has_chevron)}')
print(f'Pages without chevron-down: {len(no_chevron)}')
if no_chevron:
    print('\nNo chevron pages:')
    for p in no_chevron:
        print(f'  {p}')
