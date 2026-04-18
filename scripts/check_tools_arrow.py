import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Tools dropdown toggle section
match = re.search(r'class="nav-dropdown-toggle"[^>]*>(.*?)</a>', content, re.DOTALL)
if match:
    print('Tools toggle HTML:')
    print(match.group(0))
else:
    print('Not found')

# Also check for chevron-down or arrow-down icons
if 'chevron' in content.lower():
    print('\nChevron found in HTML')
else:
    print('\nNo chevron icon found')

# Check CSS for dropdown arrow
with open(r'd:\网站开发-json\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'chevron' in css.lower():
    print('\nChevron found in CSS')
    # Find the chevron section
    for line in css.split('\n'):
        if 'chevron' in line.lower():
            print(line)
else:
    print('\nNo chevron in CSS')
