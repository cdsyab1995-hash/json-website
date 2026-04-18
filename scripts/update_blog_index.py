# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

INDEX_FILE = r'd:\网站开发-json\pages\blog\index.html'

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# New articles to add
new_cards = [
    ('curl-json-api-guide.html', 'Developer Tools', '2026-04-18', '6-8 min', 'Mastering curl with JSON APIs: The Complete Command-Line Guide', 'Complete guide to using curl with JSON APIs. Learn how to send GET, POST, PATCH requests, handle headers, auth, and pretty-print JSON responses.'),
    ('json-patch-vs-merge-patch.html', 'API Design', '2026-04-18', '8-10 min', 'JSON Patch vs Merge Patch: Which API Update Strategy Should You Use?', 'JSON Patch (RFC 6902) vs Merge Patch: Learn the difference between these two partial update strategies for REST APIs. Which one should you use and when?'),
]

for fname, category, date, read_time, headline, desc in new_cards:
    cat_class = category.lower().replace(' ', '-')
    card = f'''
                <article class="article-card">
                    <div class="article-category cat-{cat_class}">{category}</div>
                    <h3><a href="{fname}">{headline}</a></h3>
                    <p class="article-excerpt">{desc[:120]}...</p>
                    <div class="article-meta">
                        <span>{date}</span> |
                        <span>{read_time} read</span>
                    </div>
                    <a href="{fname}" class="read-more">Read article →</a>
                </article>
'''
    # Insert after the last </article> in articles-grid
    content = content.replace('            </div>\n        </section>\n\n        <!-- JSON Templates', 
                               '            ' + card.strip() + '\n            </div>\n        </section>\n\n        <!-- JSON Templates')

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated blog/index.html with new articles')
