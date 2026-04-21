import re
from pathlib import Path

blog_dir = Path(r'd:\网站开发-json\pages\blog')
articles = sorted([f for f in blog_dir.glob('*.html') if f.name != 'index.html'])

print('=== Article Schema url and wordCount verification ===\n')
issues = []
for ap in articles:
    with open(ap, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # Find Article JSON-LD block
    art_m = re.search(r'"@type":\s*"Article"', c)
    if not art_m:
        issues.append(f'{ap.name}: NO Article schema!')
        print(f'[!!] {ap.name}: NO Article schema!')
        continue

    # Find url field (should be the article's full URL)
    url_fields = re.findall(r'"url":\s*"([^"]+)"', c)
    # The Article url should be the full article URL (not just the root)
    article_url = None
    for u in url_fields:
        if 'pages/blog/' in u:
            article_url = u
            break
    if not article_url:
        article_url = url_fields[0] if url_fields else 'MISSING'
        issues.append(f'{ap.name}: url="{article_url}" may be wrong')

    wc_m = re.search(r'"wordCount":\s*(\d+)', c)
    wc_val = int(wc_m.group(1)) if wc_m else 0

    # Actual article word count
    art_tag = re.search(r'<article[^>]*>(.*?)</article>', c, re.DOTALL)
    if art_tag:
        inner = art_tag.group(1)
        inner = re.sub(r'<nav[^>]*>.*?</nav>', '', inner, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', inner)
        text = re.sub(r'\s+', ' ', text).strip()
        actual_wc = len(text.split())
    else:
        actual_wc = 0

    flag_url = '[OK]' if article_url and 'pages/blog/' in article_url else '[!!]'
    flag_wc = '[OK]' if wc_val >= actual_wc * 0.8 else '[W]'
    print(f'{flag_url} {ap.name}:')
    print(f'       url={article_url}')
    print(f'       schema_wc={wc_val}, actual_wc~{actual_wc} {flag_wc}')
    print()

print('=== Issues ===')
if issues:
    for i in issues:
        print(f'  [!!] {i}')
else:
    print('  None!')
