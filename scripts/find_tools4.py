import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the navbar section
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>')

print(f'Navbar section: {nav_start} to {nav_end}')

if nav_start > 0 and nav_end > 0:
    navbar = content[nav_start:nav_end]
    # Find Tools in navbar
    pos = navbar.find('Tools')
    print(f'Tools in navbar at: {pos}')
    
    if pos > 0:
        start = max(0, pos - 200)
        end = min(len(navbar), pos + 50)
        print('\nContext around Tools in navbar:')
        print(repr(navbar[start:end]))
