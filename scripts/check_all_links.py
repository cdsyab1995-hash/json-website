import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'
root_dir = r'd:\网站开发-json'

# Get all existing HTML files
existing_files = set()
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, root_dir).replace('\\', '/')
            existing_files.add(rel)
            # Also add without extension for directory-style URLs
            if rel.endswith('.html'):
                existing_files.add(rel[:-5])

print(f'Existing HTML files: {len(existing_files)}')

# Check all hrefs in all HTML files
issues = []
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            # Find all hrefs
            hrefs = re.findall(r'href="([^"]+)"', content)
            for href in hrefs:
                # Skip external, anchors, javascript
                if href.startswith(('http', '#', 'javascript:', 'mailto:')):
                    continue
                
                # Resolve relative path
                rel_dir = os.path.relpath(root, root_dir).replace('\\', '/')
                if rel_dir == '.':
                    resolved = href
                else:
                    resolved = os.path.normpath(os.path.join(rel_dir, href)).replace('\\', '/')
                
                # Check if exists
                if resolved not in existing_files and resolved + '.html' not in existing_files:
                    # Might be a directory-style URL
                    if not any(resolved.startswith(e.rstrip('.html')) for e in existing_files):
                        issues.append((os.path.relpath(path, root_dir), href, resolved))

print(f'\nBroken links found: {len(issues)}')
for source, href, resolved in issues[:30]:
    print(f'  {source}: {href} -> {resolved} (NOT FOUND)')
