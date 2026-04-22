#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Navigation --> <nav class="navbar">'
end_marker = '</nav> <!-- Main Content -->'

print('Start found:', start_marker in content)
print('End found:', end_marker in content)

if start_marker in content:
    idx = content.find(start_marker)
    print('Start pos:', idx)
    print('Around start:', repr(content[idx-5:idx+120]))
else:
    # Try to find partial
    print('Partial nav check:', '<!-- Navigation -->' in content, '<nav class="navbar">' in content)
    idx = content.find('<!-- Navigation -->')
    if idx >= 0:
        print('Nav start at:', idx)
        print(repr(content[idx:idx+200]))
