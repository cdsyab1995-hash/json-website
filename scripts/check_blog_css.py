import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

classes = set(re.findall(r'class="([^"]+)"', content))
classes = sorted(classes)
print('Classes used in blog.html:')
for c in classes:
    print(' ', repr(c))

# Check which ones exist in styles.css
with open(r'd:\网站开发-json\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('\nMissing from styles.css:')
for c in classes:
    cls_name = c.split()[0]  # first class name
    # Check if .class_name { exists in CSS
    pattern = r'\.' + re.escape(cls_name) + r'[^a-zA-Z0-9_-]'
    if not re.search(pattern, css):
        print(' ', cls_name)
