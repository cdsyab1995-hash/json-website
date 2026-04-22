#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check what's at the boundary
idx_nav_start = content.find('<!-- Navigation --> <nav class="navbar">')
idx_nav_end = content.find('\n</nav> <!-- Main Content -->')
print(f'Nav start: {idx_nav_start}')
print(f'Nav end (LF): {idx_nav_end}')

if idx_nav_end >= 0:
    # Check what character is between </nav> and <!--
    segment = content[idx_nav_end:idx_nav_end+30]
    print(f'Segment: {repr(segment)}')
    # Count spaces
    after_nav = content[idx_nav_end+1:idx_nav_end+30]
    print(f'After LF: {repr(after_nav)}')

# The exact combined pattern
start = '<!-- Navigation --> <nav class="navbar">'
end = '\n</nav> <!-- Main Content -->'
combined = start + end
print(f'\nCombined repr: {repr(combined)}')
print(f'Combined in content: {combined in content}')

# Maybe it's \r\n not \n
end2 = '\r\n</nav> <!-- Main Content -->'
combined2 = start + end2
print(f'Combined2 (CRLF) in content: {combined2 in content}')

# Maybe there are extra spaces
end3 = ' </nav> <!-- Main Content -->'
combined3 = start + end3
print(f'Combined3 (space before nav) in content: {combined3 in content}')

# Try to find manually - where does the nav block END
# Find all </nav> positions
import re
all_closes = [m.start() for m in re.finditer('</nav>', content)]
print(f'\nAll </nav> positions: {all_closes}')
for pos in all_closes:
    print(f'  At {pos}: {repr(content[pos-5:pos+40])}')
