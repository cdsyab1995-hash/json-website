#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check line endings
crlf = content.count('\r\n')
lf = content.count('\n') - crlf
cr = content.count('\r') - crlf
print(f'CRLF: {crlf}, LF: {lf}, CR: {cr}')

# Check around </nav>
idx = content.find('\n</nav>')
if idx >= 0:
    print(f'LF + </nav> at: {idx}')
    print(repr(content[idx:idx+40]))
else:
    print('No LF before </nav>')
    idx2 = content.find('</nav>')
    print(f'</nav> at: {idx2}')
    print(repr(content[idx2-10:idx2+10]))

# Check exact pattern
pattern1 = '<!-- Navigation --> <nav class="navbar">\n</nav> <!-- Main Content -->'
pattern2 = '<!-- Navigation --> <nav class="navbar">\r\n</nav> <!-- Main Content -->'
pattern3 = '<!-- Navigation --> <nav class="navbar"></nav> <!-- Main Content -->'
print(f'\nPattern1 (LF): {pattern1 in content}')
print(f'Pattern2 (CRLF): {pattern2 in content}')
print(f'Pattern3 (no-newline): {pattern3 in content}')
