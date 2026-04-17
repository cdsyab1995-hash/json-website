import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'd:\网站开发-json\pages\news.html', 'r', encoding='utf-8') as f:
    content = f.read()
start = content.find('<div class="news-content">')
if start > 0:
    print(content[start:start+5000])
