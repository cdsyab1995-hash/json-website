import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix article links: bare filenames -> blog/filename
articles = [
    'ai-tool-calling-mcp-2026.html',
    'curl-json-api-guide.html',
    'json-api-error-handling-2026.html',
    'json-parsing-performance-comparison.html',
    'json-patch-vs-merge-patch.html',
    'json-schema-complete-guide-2026.html',
    'mcp-json-standardizing-ai-tools.html',
    'zod-json-schema-validation-ai.html',
]

fixed_count = 0
for article in articles:
    # Only fix bare filenames (not already prefixed)
    old = f'href="{article}"'
    new = f'href="blog/{article}"'
    if old in content and new not in content:
        content = content.replace(old, new)
        fixed_count += 1
        print(f'Fixed: {article}')

print(f'\nTotal fixed: {fixed_count}')

# Also fix any href that points to a bare .html in the blog directory context
# Pattern: href="some-article.html" where the article is in blog/
# These appear in article-card contexts
# Let's verify the fix worked
remaining = re.findall(r'href="(?!(http|#|\.\.|/))[^"]+\.html"', content)
print(f'Remaining bare .html links: {remaining}')

with open(r'd:\网站开发-json\pages\blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('blog.html updated')
