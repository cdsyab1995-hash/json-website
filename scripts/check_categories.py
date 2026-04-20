# -*- coding: utf-8 -*-
import re

# Check daily_tool_blog.py
with open(r'd:\网站开发-json\scripts\daily_tool_blog.py', 'r', encoding='utf-8') as f:
    content = f.read()
cats = re.findall(r'"cat_class":\s*"([^"]+)"', content)
print('Categories in daily_tool_blog.py:', sorted(set(cats)))

# Check daily_blog.py
with open(r'd:\网站开发-json\scripts\daily_blog.py', 'r', encoding='utf-8') as f:
    content = f.read()
cats = re.findall(r'"cat_class":\s*"([^"]+)"', content)
print('Categories in daily_blog.py:', sorted(set(cats)))

# Check CSS definitions
with open(r'd:\网站开发-json\css\styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
css_cats = re.findall(r'\.(cat-[a-z-]+)\s*\{', css)
print('CSS category classes:', sorted(set(css_cats)))
