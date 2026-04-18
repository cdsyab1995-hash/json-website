import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Fix 1: sitemap duplicate
with open(r'd:\网站开发-json\sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Remove duplicate news.html
sitemap_lines = sitemap.split('\n')
seen = {}
new_lines = []
for line in sitemap_lines:
    if '<loc>' in line:
        url = re.search(r'<loc>([^<]+)</loc>', line)
        if url:
            u = url.group(1)
            if u in seen:
                print(f'Removing duplicate: {u}')
                continue
            seen[u] = True
    new_lines.append(line)

sitemap_fixed = '\n'.join(new_lines)
with open(r'd:\网站开发-json\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_fixed)
print('sitemap.xml fixed (duplicate removed)')

# Fix 2: best-practices.html - self-link should be #
with open(r'd:\网站开发-json\pages\best-practices.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix self-referencing link
content = re.sub(
    r'href="https://www\.aijsons\.com/pages/best-practices\.html"',
    'href="#"',
    content
)
# Also fix ../best-practices.html if any (best-practices.html is in pages/, so it should be # for self)
content = re.sub(
    r'href="\.\./best-practices\.html"',
    'href="#"',
    content
)
with open(r'd:\网站开发-json\pages\best-practices.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('best-practices.html fixed')

# Fix 3: news.html - self-link should be #
with open(r'd:\网站开发-json\pages\news.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'href="https://www\.aijsons\.com/pages/news\.html"',
    'href="#"',
    content
)
content = re.sub(
    r'href="\.\./news\.html"',
    'href="#"',
    content
)
with open(r'd:\网站开发-json\pages\news.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('news.html fixed')

# Fix 4: blog.html - fix ../best-practices.html and ../news.html
with open(r'd:\网站开发-json\pages\blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# blog.html is in pages/, so links to best-practices.html should be just "best-practices.html"
content = content.replace('../best-practices.html', 'best-practices.html')
content = content.replace('../news.html', 'news.html')
with open(r'd:\网站开发-json\pages\blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('blog.html fixed')

# Fix 5: jwt-decoder.html - add Practices link
with open(r'd:\网站开发-json\pages\jwt-decoder.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if it has any nav links at all
if 'nav-dropdown' in content and 'best-practices' not in content:
    print('jwt-decoder.html missing Practices link - adding it')
    # Find the Practices link section in another file for reference
    with open(r'd:\网站开发-json\pages\format.html', 'r', encoding='utf-8') as f:
        format_content = f.read()
    practices_link = re.search(r'<a href="best-practices\.html" class="nav-link">[^<]*<svg[^>]+>.*?</svg>\s*Practices[^<]*</a>', format_content, re.DOTALL)
    if practices_link:
        # Insert after News link
        news_pos = content.find('href="news.html"')
        if news_pos > 0:
            insert_pos = content.find('</a>', news_pos) + len('</a>')
            content = content[:insert_pos] + '\n' + practices_link.group() + content[insert_pos:]
            with open(r'd:\网站开发-json\pages\jwt-decoder.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print('jwt-decoder.html Practices link added')
        else:
            print('jwt-decoder.html: could not find News link to insert after')
else:
    print('jwt-decoder.html already has Practices or no nav-dropdown')

print('\nAll fixes applied!')
