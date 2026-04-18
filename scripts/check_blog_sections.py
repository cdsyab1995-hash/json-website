# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count sections
sections = content.count('<section>')
print('Sections:', sections)

# Find section titles
import re
titles = re.findall(r'<h2 class="section-title">(.*?)</h2>', content)
for t in titles:
    print(' -', t)

# Count template cards
templates = content.count('template-card')
print('Template cards:', templates)

# Count dataset cards
datasets = content.count('dataset-card')
print('Dataset cards:', datasets)

# Check no FOUC
print('Async fonts (bad):', 'media="print"' in content)
print('Has sync styles.css:', '<link rel="stylesheet" href="../css/styles.css">' in content)
