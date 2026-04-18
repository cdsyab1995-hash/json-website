import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if file has nav-dropdown-toggle
print('Has nav-dropdown-toggle:', 'nav-dropdown-toggle' in content)
print('Has nav-dropdown:', 'nav-dropdown' in content)

# Find position of nav-dropdown-toggle
pos = content.find('nav-dropdown-toggle')
print(f'nav-dropdown-toggle position: {pos}')

if pos > 0:
    # Get 300 chars after it
    print('\nContent after nav-dropdown-toggle:')
    print(repr(content[pos:pos+300]))
