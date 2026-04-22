import re
from pathlib import Path

BASE = Path('d:/网站开发-json')
path = BASE / 'tools' / 'json-formatter.html'
text = path.read_text(encoding='utf-8')

NAV_PATTERN = re.compile(r'<!--\s*Navigation\s*-->\s*<nav class="navbar">.*?</nav>', re.DOTALL)
m = NAV_PATTERN.search(text)
if m:
    print('Found nav block, start:', m.start(), 'end:', m.end())
    print('First 120 chars:', m.group()[:120])
else:
    bare = re.compile(r'<nav class="navbar">.*?</nav>', re.DOTALL)
    m2 = bare.search(text)
    if m2:
        print('Found bare nav, start:', m2.start(), 'end:', m2.end())
        print('First 120 chars:', m2.group()[:120])
    else:
        print('NOT FOUND')
        # Show context around "navbar"
        idx = text.find('navbar')
        print('navbar found at:', idx)
        print('Context:', text[max(0,idx-50):idx+200])
