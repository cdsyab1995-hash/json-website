# -*- coding: utf-8 -*-
import re

# 检查 index.html 中所有 blog/news 相关的链接
with open(r'd:\网站开发-json\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 搜索所有 blog.html 和 news.html 的引用
print('=== index.html 中所有 blog.html 引用 ===')
for match in re.finditer(r'blog\.html', content):
    start = max(0, match.start() - 50)
    end = min(len(content), match.end() + 50)
    print(f'位置 {match.start()}: ...{content[start:end]}...')
    print()

print()
print('=== index.html 中所有 news.html 引用 ===')
for match in re.finditer(r'news\.html', content):
    start = max(0, match.start() - 50)
    end = min(len(content), match.end() + 50)
    print(f'位置 {match.start()}: ...{content[start:end]}...')
    print()

# 检查是否有 "Recent Blog" 或 "Blog Posts" 这样的标题
print()
print('=== 检查文章标题 ===')
if 'Recent Blog' in content or 'Blog Posts' in content:
    print('找到 "Recent Blog" 或 "Blog Posts" 标题')
else:
    print('未找到 "Recent Blog" 或 "Blog Posts" 标题')

if 'Recent News' in content or 'Latest News' in content:
    print('找到 "Recent News" 或 "Latest News" 标题')
else:
    print('未找到 "Recent News" 或 "Latest News" 标题')
