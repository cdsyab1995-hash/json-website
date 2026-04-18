import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'
pages_dir = os.path.join(root_dir, 'pages')

def extract_navbar(html):
    '''Extract navbar links from HTML'''
    nav_match = re.search(r'<nav class="navbar">(.*?)</nav>', html, re.DOTALL)
    if not nav_match:
        return None, None
    nav = nav_match.group(1)
    # Extract all href links
    links = re.findall(r'href="([^"]+)"', nav)
    # Get text content between tags
    texts = re.findall(r'>([^<]+)<', nav)
    texts = [t.strip() for t in texts if t.strip() and len(t.strip()) < 30]
    return links, texts

# Check root index.html
print('=== ROOT index.html Navbar ===')
with open(os.path.join(root_dir, 'index.html'), 'r', encoding='utf-8') as f:
    root_html = f.read()
root_links, root_texts = extract_navbar(root_html)
print('Links:', root_links[:20] if root_links else 'None')
print('Texts:', root_texts[:20] if root_texts else 'None')

# Check key pages
key_pages = ['format.html', 'escape.html', 'blog.html', 'news.html', 'about.html', 'changelog.html', 'best-practices.html']
for page in key_pages:
    fpath = os.path.join(pages_dir, page)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        links, texts = extract_navbar(html)
        print(f'\n=== pages/{page} ===')
        print('Links:', links[:20] if links else 'None')
        print('Texts:', texts[:20] if texts else 'None')
