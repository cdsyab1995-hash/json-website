import os

files = [
    'pages/format.html',
    'pages/json2csv.html',
    'pages/compare.html',
    'pages/blog/ai-tool-calling-mcp-2026.html',
]
for f in files:
    path = os.path.join(r'd:\网站开发-json', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        ar = content.count('aggregateRating')
        faq = content.count('FAQPage')
        wc = content.count('wordCount')
        print(f'{f}: aggregateRating={ar}, FAQPage={faq}, wordCount={wc}')
