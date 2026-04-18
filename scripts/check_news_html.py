import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\news.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if it loads external styles.css
if '../css/styles.css' in content:
    print('news.html loads external styles.css: YES')
else:
    print('news.html loads external styles.css: NO!')

# Check for inline styles vs external
inline_count = content.count('<style>')
print(f'Inline <style> blocks: {inline_count}')

# Extract class names used
classes = set(re.findall(r'class="([^"]+)"', content))
classes = sorted(classes)
print('\nClasses used in news.html:')
for c in classes:
    print(' ', repr(c))

# Check which are missing from styles.css
with open(r'd:\网站开发-json\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('\nMissing from styles.css:')
for c in classes:
    cls_name = c.split()[0]
    pattern = r'\.' + re.escape(cls_name) + r'[^a-zA-Z0-9_-]'
    if not re.search(pattern, css):
        print(' ', cls_name)
