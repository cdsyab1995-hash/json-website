#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Navigation --> <nav class="navbar">'
end_marker = '</nav> <!-- Main Content -->'
combined = start_marker + end_marker

print('Combined found:', combined in content)

new_nav = '<!-- Navigation -->\n<div id="navbar-placeholder"></div>\n'
result = content.replace(combined, new_nav)
print('Result == content:', result == content)
print('Changes made:', content.count(combined), '->', result.count(combined))
