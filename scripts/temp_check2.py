import re
pages = ['escape.html', 'extract.html']
for p in pages:
    with open('d:/网站开发-json/pages/' + p, encoding='utf-8') as f:
        content = f.read()
    # 找 FAQ 相关内容
    for pattern in ['faq-section', 'faq-container', 'id="faq"', 'faq-item']:
        if pattern in content:
            print(p + ': found "' + pattern + '"')
    # 找常见结构
    if 'article-content' in content:
        print(p + ': has article-content')
    if 'details' in content and 'summary' in content:
        print(p + ': has details/summary')
