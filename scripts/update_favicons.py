import os, re

pages_dir = r'd:\网站开发-json\pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

FAVICON_BLOCK = '''    <!-- Favicon & App Icons -->
    <link rel="icon" type="image/x-icon" href="../images/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png">
    <link rel="icon" type="image/svg+xml" href="../images/logo.svg">
    <meta name="msapplication-TileImage" content="../images/logo-192.png">
    <meta name="msapplication-TileColor" content="#131c2e">
'''

updated = 0
for fname in files:
    path = os.path.join(pages_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has proper favicon
    if 'favicon.ico' in content or 'favicon-32x32' in content:
        print('  Already has favicon: ' + fname)
        continue
    
    # Insert before </head> or before first <style> or before <link rel="preconnect"
    # Find a good insertion point
    insert_markers = [
        '    <!-- Preconnect to Google Fonts -->',
        '    <link rel="preconnect"',
        '    <link rel="stylesheet"',
        '</head>',
    ]
    
    inserted = False
    for marker in insert_markers:
        if marker in content:
            content = content.replace(marker, FAVICON_BLOCK + marker, 1)
            inserted = True
            break
    
    if inserted:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print('  Updated: ' + fname)
    else:
        print('  Could not find insertion point: ' + fname)

print('Done: ' + str(updated) + '/' + str(len(files)) + ' files updated')
