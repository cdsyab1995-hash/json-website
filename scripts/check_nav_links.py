import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Root-level HTML files (these are at the domain root)
root_files = {'index.html', 'cookie.html', 'privacy.html', 'terms.html'}

# Pages directory files
pages_files = set()
for f in os.listdir(r'd:\网站开发-json\pages'):
    if f.endswith('.html'):
        pages_files.add(f)
# Also subdirectories
for subdir in ['blog', 'news']:
    subdir_path = os.path.join(r'd:\网站开发-json\pages', subdir)
    if os.path.exists(subdir_path):
        for f in os.listdir(subdir_path):
            if f.endswith('.html'):
                pages_files.add(subdir + '/' + f)

print(f'Root files: {sorted(root_files)}')
print(f'Pages files: {len(pages_files)} files')

# Check nav links in all pages
issues = []
for root, dirs, files in os.walk(r'd:\网站开发-json'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            rel_root = os.path.relpath(root, r'd:\网站开发-json')
            
            # Find all HTML hrefs
            hrefs = re.findall(r'href="([^"#?].*?\.html)"', content)
            for href in hrefs:
                # Skip external
                if href.startswith(('http', '//', '/')):
                    continue
                
                # Resolve path
                if rel_root == '.':
                    resolved = href
                else:
                    resolved = os.path.normpath(os.path.join(rel_root, href)).replace('\\', '/')
                
                # Check if this resolves to an actual file
                if resolved in pages_files or resolved in root_files:
                    continue
                
                # Try with .html extension
                if resolved.endswith('.html'):
                    # Check if it should be in pages/
                    filename = os.path.basename(resolved)
                    subpath = os.path.dirname(resolved)
                    if filename in pages_files and subpath not in ['.', 'blog', 'news']:
                        issues.append((os.path.relpath(path, r'd:\网站开发-json'), href, 'should be: pages/' + filename))
                    elif resolved not in pages_files and resolved not in root_files:
                        issues.append((os.path.relpath(path, r'd:\网站开发-json'), href, 'NOT FOUND: ' + resolved))

# Dedupe
seen = set()
unique_issues = []
for issue in issues:
    key = tuple(issue)
    if key not in seen:
        seen.add(key)
        unique_issues.append(issue)

print(f'\nLink issues found: {len(unique_issues)}')
for source, href, note in unique_issues[:30]:
    print(f'  {source}: {href} -> {note}')

# Also show what the nav bar links look like in each category
print('\n=== Nav link patterns ===')
# Check index.html
index_nav = open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8').read()
nav_tools = re.findall(r'href="([^"]*format[^"]*)"', index_nav)
print(f'index.html -> format: {nav_tools}')

# Check pages/format.html
format_nav = open(r'd:\网站开发-json\pages\format.html', 'r', encoding='utf-8').read()
nav_tools2 = re.findall(r'href="([^"]*format[^"]*)"', format_nav)
print(f'pages/format.html -> format: {nav_tools2}')
