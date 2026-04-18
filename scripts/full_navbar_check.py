import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'
pages_dir = os.path.join(root_dir, 'pages')

def get_navbar_after_tools(html):
    '''Extract navbar links after Tools dropdown'''
    nav_match = re.search(r'<nav class="navbar">(.*?)</nav>', html, re.DOTALL)
    if not nav_match:
        return None, None
    nav = nav_match.group(1)
    
    # Find end of Tools dropdown section
    # Look for the closing </div> of nav-dropdown-menu and </div> of nav-dropdown
    dropdown_end = nav.find('</div>\n            </div>\n            <a')
    if dropdown_end == -1:
        dropdown_end = nav.find('</div>\n            </div>\n')
    if dropdown_end == -1:
        # Try to find just after nav-dropdown div closes
        idx = nav.find('nav-dropdown')
        if idx > 0:
            # Find the next </div> that closes nav-dropdown
            depth = 0
            for i in range(idx, len(nav)):
                if nav[i:i+5] == '<div ':
                    depth += 1
                elif nav[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        dropdown_end = i + 6
                        break
    
    if dropdown_end > 0:
        remaining = nav[dropdown_end:]
    else:
        remaining = nav
    
    # Extract links
    links = re.findall(r'href="([^"]+)"', remaining)
    # Get text
    texts = re.findall(r'>([^<]+)<', remaining)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) < 30]
    
    return links, texts

def get_tools_chevron(html):
    '''Check if Tools has chevron-down'''
    return 'chevron-down' in html

print('=== Full Navbar Check ===\n')

# Check root index.html
print('ROOT index.html:')
with open(os.path.join(root_dir, 'index.html'), 'r', encoding='utf-8') as f:
    root_html = f.read()
links, texts = get_navbar_after_tools(root_html)
chevron = get_tools_chevron(root_html)
print(f'  Chevron: {"✅" if chevron else "❌"}')
print(f'  Links: {links}')
print(f'  Texts: {texts}')

# Check all pages
pages_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

issues = []
for fname in pages_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    links, texts = get_navbar_after_tools(html)
    chevron = get_tools_chevron(html)
    
    status = "✅" if chevron else "❌"
    print(f'\npages/{fname}:')
    print(f'  Chevron: {status}')
    print(f'  Links: {links}')
    print(f'  Texts: {texts}')
    
    if not chevron:
        issues.append(f'{fname}: missing chevron')

print(f'\n\n=== Summary ===')
if issues:
    print(f'Issues found:')
    for i in issues:
        print(f'  ❌ {i}')
else:
    print('✅ All pages have chevron!')
