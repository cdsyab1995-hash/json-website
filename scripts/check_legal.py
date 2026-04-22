#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('navbar-placeholder:', 'id="navbar-placeholder"' in content)
print('navbar.js:', '/js/navbar.js' in content)
print('old nav:', '<nav class="navbar">' in content)
print('css abs path:', 'href="/css/styles.css"' in content)
print('app.js path:', '/js/app.js' in content)
print('css relative:', 'href="css/styles.css"' in content)

# Find app.js
idx = content.find('/js/app.js')
if idx >= 0:
    print('Around app.js:', repr(content[idx-50:idx+50]))
