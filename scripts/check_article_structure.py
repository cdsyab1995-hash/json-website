# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open(r'd:\网站开发-json\pages\blog\json-schema-complete-guide-2026.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('Size:', len(content))
print('Has navbar:', '<nav' in content)
print('Has footer:', '<footer' in content)
print('Has styles.css:', 'styles.css' in content)
print('Has JSON-LD:', 'application/ld+json' in content)
# Show head section
m = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
if m:
    print('\nHEAD:')
    print(m.group(1)[:500])
