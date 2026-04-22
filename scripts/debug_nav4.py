#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Debug: find exact nav block boundaries
idx_nav = content.find('<!-- Navigation --> <nav class="navbar">')
idx_end = content.find('</nav> <!-- Main Content -->')
print(f'Nav start: {idx_nav}')
print(f'Nav end: {idx_end}')
print(f'Nav block length: {idx_end - idx_nav}')
print(f'Char at nav_start+120: {repr(content[idx_nav+120:idx_nav+125])}')
print(f'Char before nav_end: {repr(content[idx_end-5:idx_end])}')
print(f'Char at nav_end: {repr(content[idx_end:idx_end+30])}')

# Try different combinations
test1 = '</nav> <!-- Main Content -->'
test2 = '</nav>  <!-- Main Content -->'
print(f'\nTest1 found: {test1 in content}')
print(f'Test2 found: {test2 in content}')
