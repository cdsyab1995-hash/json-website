import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
fpath = os.path.join(pages_dir, 'format.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find nav-dropdown-toggle section
nav_start = content.find('<nav class="navbar">')
nav_end = content.find('</nav>')

if nav_start > 0 and nav_end > 0:
    navbar = content[nav_start:nav_end]
    
    # Find the Tools dropdown toggle
    toggle_start = navbar.find('nav-dropdown-toggle')
    toggle_end = navbar.find('</a>', toggle_start) + 4
    
    if toggle_start > 0 and toggle_end > 0:
        toggle_html = navbar[toggle_start:toggle_end]
        print('Tools toggle HTML:')
        print(toggle_html)
        
        if 'chevron-down' in toggle_html:
            print('\n✅ chevron-down found in toggle!')
        else:
            print('\n❌ chevron-down NOT found in toggle!')
