import sys, os
sys.stdout.reconfigure(encoding='utf-8')

pages_dir = r'd:\网站开发-json\pages'

# Check format.html for Tools section
fpath = os.path.join(pages_dir, 'format.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Tools
pos = content.find('Tools</a>')
if pos > 0:
    start = max(0, pos - 500)
    print('Tools section in format.html:')
    print(repr(content[start:pos+20]))
