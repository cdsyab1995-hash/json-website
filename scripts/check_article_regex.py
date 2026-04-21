import re, os
from pathlib import Path

# Test json-schema-complete-guide specifically
p = Path(r'd:\网站开发-json\pages\blog\json-schema-complete-guide-2026.html')
with open(p, 'r', encoding='utf-8') as fp:
    c = fp.read()

# Where does article-content div start and end?
start_m = c.find('<div class="article-content">')
print(f'article-content starts at char: {start_m}')

# Find the first </div> after start
first_div = c.find('</div>', start_m)
print(f'First </div> after start at char: {first_div}')

# Find the second </div> after start
second_div = c.find('</div>', first_div + 1)
print(f'Second </div> after start at char: {second_div}')

# Extract using the regex (non-greedy)
m = re.search(r'<div class="article-content">(.*?)</div>', c, re.DOTALL)
if m:
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    text = re.sub(r'\s+', ' ', text).strip()
    wc = len(text.split())
    print(f'Regex matched: {wc} words')
    print(f'First 200 chars: {text[:200]}')
else:
    print('No match!')

# Now try a different approach - find the article tag
article_m = re.search(r'<article>(.*?)</article>', c, re.DOTALL)
if article_m:
    inner = article_m.group(1)
    text = re.sub(r'<[^>]+>', ' ', inner)
    text = re.sub(r'\s+', ' ', text).strip()
    wc = len(text.split())
    print(f'\nArticle tag match: {wc} words')
    print(f'First 200 chars: {text[:200]}')
