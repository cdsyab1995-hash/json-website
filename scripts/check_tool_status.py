import re
pages = ['format.html', 'escape.html', 'extract.html', 'sort.html', 'clean.html', 'viewer.html', 'json2csv.html', 'compare.html', 'xml.html', 'yaml.html']
print('=== Tool Page Status ===')
for page in pages:
    with open('d:/网站开发-json/pages/' + page, 'r', encoding='utf-8') as f:
        content = f.read()
    has_copy = 'btnCopy' in content or 'copyBtn' in content
    has_clear = 'btnClear' in content or 'clearBtn' in content
    has_template = 'templateSelect' in content
    has_faq = 'faq-container' in content or 'faq-item' in content
    status = 'OK' if (has_copy and has_clear and has_template and has_faq) else 'INCOMPLETE'
    print(f'{page:<20} Copy={has_copy} Clear={has_clear} Template={has_template} FAQ={has_faq} -> {status}')
