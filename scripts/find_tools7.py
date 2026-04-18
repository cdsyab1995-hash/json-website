import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the navbar section
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>')

if nav_start > 0 and nav_end > 0:
    navbar = content[nav_start:nav_end]
    # Find Tools in navbar
    pos = navbar.find('Tools')
    if pos > 0:
        start = max(0, pos - 20)
        end = min(len(navbar), pos + 400)
        print('Tools section (500 chars):')
        print(repr(navbar[start:end]))
