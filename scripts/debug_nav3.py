#!/usr/bin/env python3
with open(r'd:\网站开发-json\cookie\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find what comes between </nav> and <!-- Main Content -->
import re
m = re.search(r'</nav>(.*?)<!-- Main Content -->', content, re.DOTALL)
if m:
    print('Found between </nav> and <!-- Main Content>:')
    print(repr(m.group(1)[:200]))
else:
    print('No match for </nav>...<!-- Main Content -->')
    # Try find </nav> and what follows
    idx = content.find('</nav>')
    if idx >= 0:
        print('After </nav>:', repr(content[idx:idx+100]))
