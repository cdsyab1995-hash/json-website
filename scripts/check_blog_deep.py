import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check breadcrumb
bc = re.findall(r'breadcrumb', content)
print(f'breadcrumb occurrences: {len(bc)}')
# Show breadcrumb context
for m in re.finditer(r'breadcrumb', content):
    print('Context:', repr(content[max(0,m.start()-50):m.start()+100]))
    print()

# Check app.js
print('app.js in content:', '../js/app.js' in content)

# Check og:image
print('og:image in content:', '../og-image.png' in content)

# Check JSON-LD
ld_m = re.search(r'"url":\s*"([^"]+)"', content)
if ld_m:
    print('JSON-LD url:', ld_m.group(1))

# Check datasets
print('datasets-list:', 'datasets-list' in content)
print('dataset-card:', 'dataset-card' in content)

# Find all link hrefs with relative paths
hrefs = re.findall(r'href="([^"]+)"', content)
print('\nAll hrefs:')
for h in hrefs[:20]:
    print(' ', h)
