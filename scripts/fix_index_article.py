# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open('d:/网站开发-json/index.html', encoding='utf-8').read()
print(f"File size: {len(content)} bytes")

# Find positions
p_04_15 = content.find('2026-04-15')
p_04_18 = content.find('2026-04-18')
p_04_19 = content.find('2026-04-19')

print(f"04-15 found: {p_04_15}")
print(f"04-18 found: {p_04_18}")
print(f"04-19 found: {p_04_19}")

if p_04_15 != -1:
    # The article is likely all on one line
    # Find the start of this article card (look for the opening <article>)
    # Work backwards from 04-15 to find <article class="feature-card"
    search_start = max(0, p_04_15 - 500)
    snippet = content[search_start:p_04_15 + 100]
    print(f"\nSnippet around 04-15 (cleaned):")
    # Remove emojis for display
    clean = ''.join(c for c in snippet if ord(c) < 0x1F000 or c == '\n')
    print(clean[:300])
