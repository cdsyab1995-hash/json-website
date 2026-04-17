import re
import os

# Read blog.html
blog_path = r'd:\网站开发-json\pages\blog.html'
with open(blog_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find article patterns
articles = re.findall(r'<article id="(ai-daily-\d+[a-z]?)"', content)
print("Existing articles:", articles[:10])

# Find the Latest Articles section in index.html
index_path = r'd:\网站开发-json\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find articles in index
index_articles = re.findall(r'<article[^>]*>\s*<span[^>]*>(\d{4}-\d{2}-\d{2})</span>\s*<h3[^>]*>(.*?)</h3>', index_content)
print("\nIndex articles:")
for date, title in index_articles[:5]:
    print(f"  {date}: {title[:60]}...")
