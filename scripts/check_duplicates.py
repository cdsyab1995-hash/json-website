import os

files = [
    'pages/blog/jwt-security-best-practices-2026.html',
    'pages/blog/curl-json-api-guide.html',
    'pages/blog/ai-tool-calling-mcp-2026.html',
    'pages/format.html',
]
for f in files:
    path = os.path.join(r'd:\网站开发-json', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        print(f'{f}:')
        print(f'  aggregateRating: {content.count("aggregateRating")}')
        print(f'  FAQPage: {content.count("FAQPage")}')
        print(f'  wordCount: {content.count("wordCount")}')
        print(f'  "Article": {content.count("\"Article\"")}')
        print(f'  "BreadcrumbList": {content.count("\"BreadcrumbList\"")}')
