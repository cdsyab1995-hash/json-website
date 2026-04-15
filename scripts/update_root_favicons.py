import os, re

# Update root pages (cookie, privacy, terms)
ROOT_DIR = r'd:\网站开发-json'
root_files = ['cookie.html', 'privacy.html', 'terms.html']

FAVICON_BLOCK_ROOT = '''    <!-- Favicon & App Icons -->
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
    <link rel="icon" type="image/svg+xml" href="/images/logo.svg">
    <meta name="msapplication-TileImage" content="/images/logo-192.png">
    <meta name="msapplication-TileColor" content="#131c2e">
'''

updated = 0
for fname in root_files:
    path = os.path.join(ROOT_DIR, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'favicon.ico' in content or 'favicon-32x32' in content:
        print('  Already has favicon: ' + fname)
        continue
    
    insert_markers = [
        '    <!-- Preconnect to Google Fonts -->',
        '    <link rel="preconnect"',
        '    <link rel="stylesheet"',
        '</head>',
    ]
    
    inserted = False
    for marker in insert_markers:
        if marker in content:
            content = content.replace(marker, FAVICON_BLOCK_ROOT + marker, 1)
            inserted = True
            break
    
    if not inserted:
        # Try <title> tag
        if '<title>' in content:
            content = content.replace('<title>', FAVICON_BLOCK_ROOT + '    <title>', 1)
            inserted = True
    
    if inserted:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print('  Updated: ' + fname)
    else:
        print('  Could not update: ' + fname)

print('Root pages updated: ' + str(updated))
