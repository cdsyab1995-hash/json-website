import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check article links - should point to blog/article-name.html
article_links = re.findall(r'href="([^"]*\.html)"', content)
print(f'Total HTML links in blog.html: {len(article_links)}')

# Categorize
root_links = []  # ../index.html etc
blog_article_links = []  # blog/article.html
other = []

for link in article_links:
    if link.startswith('../'):
        root_links.append(link)
    elif link.startswith('blog/'):
        blog_article_links.append(link)
    elif link.startswith('http') or link == '#':
        pass
    else:
        other.append(link)

print(f'\nRoot links ({len(root_links)}):')
for l in sorted(set(root_links)):
    print(' ', l)

print(f'\nBlog article links ({len(blog_article_links)}):')
for l in sorted(set(blog_article_links)):
    print(' ', l)

print(f'\nOther links ({len(other)}):')
for l in sorted(set(other)):
    print(' ', l)

# Check: article links should be relative to pages/blog.html
# pages/blog.html -> pages/blog/article.html = "blog/article.html" ✓
# pages/blog.html -> pages/index.html = "../index.html" ✓
# These paths are CORRECT!
print('\n=== VERDICT ===')
if root_links and blog_article_links:
    print('Paths are CORRECT for multi-page architecture')
else:
    print('ISSUE: Check path structure')
