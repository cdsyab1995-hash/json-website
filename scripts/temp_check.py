import re
pages = ['viewer.html', 'json2csv.html', 'compare.html']
for p in pages:
    with open('d:/网站开发-json/pages/' + p, encoding='utf-8') as f:
        content = f.read()
    buttons = re.findall(r'id="([^"]+)"', content)
    print(p + ': ' + str([b for b in buttons if 'btn' in b.lower() or 'copy' in b.lower() or 'clear' in b.lower()]))
