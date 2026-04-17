import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check blog.html
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

articles = re.findall(r'<article id="([^"]+)"', blog)
dates = re.findall(r'<strong>Published:</strong>\s*([A-Za-z0-9 ,-]+)', blog)
titles = re.findall(r'<h3[^>]*>([^<]+)</h3>', blog)

print('=== BLOG.HTML Articles ===')
print(f'Found {len(articles)} articles, {len(dates)} dates, {len(titles)} titles')
for i, (a, d, t) in enumerate(zip(articles, dates, titles)):
    print(f'  {i+1}. [{a}] | {d} | {t[:70]}')
print()

# Check news.html
with open(r'd:\网站开发-json\pages\news.html', 'r', encoding='utf-8') as f:
    news = f.read()

news_articles = re.findall(r'<article id="([^"]+)"', news)
news_dates = re.findall(r'<strong>Published:</strong>\s*([A-Za-z0-9 ,-]+)', news)
news_titles = re.findall(r'<h3[^>]*>([^<]+)</h3>', news)

print('=== NEWS.HTML Articles ===')
print(f'Found {len(news_articles)} articles, {len(news_dates)} dates, {len(news_titles)} titles')
for i, (a, d, t) in enumerate(zip(news_articles, news_dates, news_titles)):
    print(f'  {i+1}. [{a}] | {d} | {t[:70]}')

# Check if 2026-04-17 content exists
print()
print('=== Today 2026-04-17 content ===')
has_blog_today = '2026-04-17' in blog or 'April 17, 2026' in blog
has_news_today = '2026-04-17' in news or 'April 17, 2026' in news
print(f'Blog has 2026-04-17 content: {has_blog_today}')
print(f'News has 2026-04-17 content: {has_news_today}')
