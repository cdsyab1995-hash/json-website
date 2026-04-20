import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

PAGES_DIR = r"d:\网站开发-json\pages"
PAGES = ['format.html', 'escape.html', 'extract.html', 'sort.html', 'clean.html',
         'viewer.html', 'json2csv.html', 'compare.html', 'xml.html', 'yaml.html']

print('=== Tool Page Final Status ===')
print('Page               Copy    Clear   Download  Template  FAQ    UseCases')
print('-' * 75)

for page in PAGES:
    filepath = os.path.join(PAGES_DIR, page)
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    has_copy = 'btnCopy' in content or 'copyBtn' in content
    has_clear = 'btnClear' in content or 'clearBtn' in content
    has_download = 'btnDownload' in content or 'downloadBtn' in content
    has_template = 'templateSelect' in content
    has_faq = 'faq-item' in content or 'faq-container' in content
    has_usecases = 'Common Use Cases' in content or 'common-usecases' in content
    
    status = 'OK' if all([has_copy, has_clear, has_download, has_template, has_faq, has_usecases]) else 'PARTIAL'
    print(f'{page:<18} {"OK" if has_copy else "NO":<7} {"OK" if has_clear else "NO":<7} {"OK" if has_download else "NO":<9} {"OK" if has_template else "NO":<9} {"OK" if has_faq else "NO":<6} {"OK" if has_usecases else "NO":<10} {status}')
