import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\网站开发-json'
pages_dir = os.path.join(root_dir, 'pages')

# Find all HTML files in pages directory
fixed_count = 0
for fname in os.listdir(pages_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(pages_dir, fname)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this page has the wrong tutorial link
    if 'href="tutorial.html"' in content:
        # Replace tutorial.html with blog.html
        new_content = content.replace('href="tutorial.html"', 'href="blog.html"')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        fixed_count += 1
        print(f'Fixed: {fname} - changed tutorial.html to blog.html')

print(f'\nTotal fixed: {fixed_count}')
