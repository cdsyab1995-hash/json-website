import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

# Check sitemap first
with open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Check which sitemap URLs have issues
sitemap_urls = re.findall(r'<loc>([^<]+)</loc>', sitemap)
print('=== SITEMAP URL CHECK ===')
issues = []
for url in sitemap_urls:
    # Extract the file path part
    path = url.replace('https://www.aijsons.com', '')
    if path.startswith('/pages/'):
        file_path = os.path.join(r'd:\网站开发-json', path.lstrip('/'))
    elif path == '/':
        file_path = r'd:\网站开发-json\index.html'
    else:
        file_path = os.path.join(r'd:\网站开发-json', path.lstrip('/'))
    
    exists = os.path.exists(file_path)
    if not exists:
        issues.append(f'  404: {url} -> {file_path}')
        print(f'  404: {url}')
    else:
        print(f'  OK:   {url}')

print(f'\nTotal: {len(sitemap_urls)} URLs, {len(issues)} issues')

# Now check Practices links in all pages
print('\n=== PRACTICES LINKS CHECK ===')
for fname in sorted(html_files):
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    practices_match = re.search(r'href="([^"]*best-practices[^"]*)"', content)
    if practices_match:
        link = practices_match.group(1)
        # Determine correct path based on file location
        if fname == 'index.html':
            # pages/index.html -> ../best-practices.html
            expected = '../best-practices.html'
        else:
            # pages/*.html -> best-practices.html
            expected = 'best-practices.html'
        
        if link == expected:
            print(f'  {fname}: OK ({link})')
        else:
            print(f'  {fname}: WRONG ({link}) - should be {expected}')
    else:
        # Check if Practices is in dropdown
        if 'best-practices' in content:
            print(f'  {fname}: Has best-practices but no href found!')
        else:
            print(f'  {fname}: No Practices link')

# Check News links
print('\n=== NEWS LINKS CHECK ===')
for fname in sorted(html_files):
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    news_match = re.search(r'href="([^"]*news[^"]*)"', content)
    if news_match:
        link = news_match.group(1)
        if fname == 'index.html':
            expected = '../news.html'
        else:
            expected = 'news.html'
        
        if link == expected:
            print(f'  {fname}: OK ({link})')
        else:
            print(f'  {fname}: WRONG ({link}) - should be {expected}')
    else:
        if 'news' in content.lower():
            print(f'  {fname}: Has news but no href')
