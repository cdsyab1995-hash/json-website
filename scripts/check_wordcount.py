import re, os
from pathlib import Path

blog_dir = Path(r'd:\网站开发-json\pages\blog')
articles = list(blog_dir.glob('*.html'))

for ap in sorted(articles):
    if ap.name == 'index.html':
        continue
    with open(ap, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Extract wordCount from schema
    m_wc = re.search(r'"wordCount":\s*(\d+)', c)
    wc_in_schema = int(m_wc.group(1)) if m_wc else 0
    
    # Extract article content and count words
    content_m = re.search(r'<div class="article-content">(.*?)</div>', c, re.DOTALL)
    if content_m:
        text = re.sub(r'<[^>]+>', ' ', content_m.group(1))
        text = re.sub(r'\s+', ' ', text).strip()
        actual_wc = len(text.split())
        match_ratio = wc_in_schema / actual_wc if actual_wc > 0 else 0
        flag = '!!' if match_ratio > 1.5 or match_ratio < 0.5 else 'OK'
        print(f'{flag} {ap.name}: schema={wc_in_schema}, actual={actual_wc}, ratio={match_ratio:.2f}')
    else:
        print(f'?? {ap.name}: No article-content div found, schema wc={wc_in_schema}')
