import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check format.html for Tools section
fpath = os.path.join(pages_dir, 'format.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Tools in navbar
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>')

if nav_start > 0 and nav_end > 0:
    navbar = content[nav_start:nav_end]
    pos = navbar.find('Tools')
    if pos > 0:
        start = max(0, pos - 20)
        end = min(len(navbar), pos + 400)
        print('Tools section in format.html (400 chars):')
        print(repr(navbar[start:end]))
