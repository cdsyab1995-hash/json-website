import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if canonical exists
canonical = re.search(r'<link rel="canonical"[^>]+>', content)
print('Current canonical:', canonical.group() if canonical else 'MISSING')

# Check og:url
og = re.search(r'<meta property="og:url"[^>]+>', content)
print('Current og:url:', og.group() if og else 'MISSING')

# Check JSON-LD url
ld = re.search(r'"url":\s*"([^"]+)"', content)
print('Current JSON-LD url:', ld.group(1) if ld else 'MISSING')

# Add canonical if missing
if not canonical:
    # Find a good insertion point - after og:title or before title
    title_end = content.find('</title>')
    if title_end > 0:
        insert_point = title_end + len('</title>')
        canonical_tag = '\n    <link rel="canonical" href="https://www.aijsons.com/pages/blog.html">'
        content = content[:insert_point] + canonical_tag + content[insert_point:]
        print('\nAdded canonical tag')
    else:
        print('Could not find title tag')

# Fix og:url
og_fixed = False
if og:
    content = content.replace(
        og.group(),
        '<meta property="og:url" content="https://www.aijsons.com/pages/blog.html">'
    )
    print('Fixed og:url')
    og_fixed = True
else:
    # Add og:url after og:title
    og_title = re.search(r'<meta property="og:title"[^>]+>', content)
    if og_title:
        insert = og_title.end()
        content = content[:insert] + '\n    <meta property="og:url" content="https://www.aijsons.com/pages/blog.html">' + content[insert:]
        print('Added og:url')

# Fix JSON-LD
if ld:
    content = content.replace(
        f'"url": "{ld.group(1)}"',
        '"url": "https://www.aijsons.com/pages/blog.html"'
    )
    print('Fixed JSON-LD url')

with open(r'd:\网站开发-json\pages\blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    final = f.read()
canonical2 = re.search(r'<link rel="canonical"[^>]+>', final)
og2 = re.search(r'<meta property="og:url"[^>]+>', final)
ld2 = re.search(r'"url":\s*"([^"]+)"', final)
print('\nFinal check:')
print('canonical:', canonical2.group() if canonical2 else 'MISSING')
print('og:url:', og2.group() if og2 else 'MISSING')
print('JSON-LD url:', ld2.group(1) if ld2 else 'MISSING')
