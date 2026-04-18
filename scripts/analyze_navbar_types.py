import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check the full navbar content for format.html (as reference)
fpath = os.path.join(pages_dir, 'format.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

print('=== format.html navbar analysis ===')
# Find navbar
nav_start = content.find('<div class="navbar-links">')
if nav_start >= 0:
    nav_end = content.find('</div>\n    </nav>', nav_start)
    navbar = content[nav_start:nav_end]
    
    # All links
    links = re.findall(r'href="([^"]*)"', navbar)
    print(f'All links ({len(links)}):')
    for link in links:
        print(f'  - {link}')
