import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'
pages_dir = os.path.join(root_dir, 'pages')

def extract_navbar_after_tools(html):
    '''Extract navbar links after Tools dropdown'''
    nav_match = re.search(r'<nav class="navbar">(.*?)</nav>', html, re.DOTALL)
    if not nav_match:
        return None
    nav = nav_match.group(1)
    # Find the Tools dropdown menu end position
    dropdown_end = nav.find('</div>\n            </div>\n            <a')
    if dropdown_end == -1:
        # Try alternate pattern
        dropdown_end = nav.find('</div>\n            </div>\n            <')
    
    if dropdown_end > 0:
        remaining = nav[dropdown_end:]
    else:
        remaining = nav
    
    # Extract links after Tools dropdown
    links = re.findall(r'href="([^"]+)"', remaining)
    # Get texts
    texts = re.findall(r'>([^<]+)<', remaining)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) < 30]
    return links, texts

# Check root index.html
print('=== ROOT index.html Navbar (after Tools) ===')
with open(os.path.join(root_dir, 'index.html'), 'r', encoding='utf-8') as f:
    root_html = f.read()
root_links, root_texts = extract_navbar_after_tools(root_html)
print('Links:', root_links[:10] if root_links else 'None')
print('Texts:', root_texts[:10] if root_texts else 'None')

# Check key pages
key_pages = ['format.html', 'escape.html', 'blog.html', 'news.html', 'about.html', 'changelog.html', 'best-practices.html']
for page in key_pages:
    fpath = os.path.join(pages_dir, page)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        links, texts = extract_navbar_after_tools(html)
        print(f'\n=== pages/{page} (after Tools) ===')
        print('Links:', links[:10] if links else 'None')
        print('Texts:', texts[:10] if texts else 'None')
