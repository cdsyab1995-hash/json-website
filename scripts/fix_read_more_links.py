# -*- coding: utf-8 -*-
"""Fix 'Read article' link texts in blog.html to be more descriptive."""
import re
from pathlib import Path

blog_path = Path(r'd:\网站开发-json\pages\blog.html')
content = blog_path.read_text(encoding='utf-8')

replacements = [
    ('compare-json-documents-find-differences', 'Read article', 'Read the JSON diff guide'),
    ('model-context-protocol-json-rpc-ai-tools', 'Read article', 'Read the MCP JSON-RPC guide'),
    ('sort-json-arrays-objects-guide', 'Read article', 'Read the JSON sorting guide'),
    ('postgresql-jsonb-vs-mongodb-document-store', 'Read article', 'Compare JSONB vs MongoDB'),
    ('json-edge-computing-cloudflare-workers', 'Read article', 'Read the edge computing guide'),
    ('jwt-security-best-practices-2026', 'Read article', 'Read the JWT security guide'),
    ('zod-json-schema-validation-ai', 'Read article', 'Read the Zod validation guide'),
    ('ai-tool-calling-mcp-2026', 'Read article', 'Read the AI tool calling guide'),
    ('mcp-json-standardizing-ai-tools', 'Read article', 'Read the MCP standardization guide'),
    ('json-api-error-handling-2026', 'Read article', 'Read the API error handling guide'),
    ('json-schema-complete-guide-2026', 'Read article', 'Read the JSON Schema complete guide'),
]

count = 0
for url_frag, old_text, new_text in replacements:
    pattern = rf'(<a href="blog/{re.escape(url_frag)}\.html" class="read-more">){re.escape(old_text)} .(</a>)'
    replacement = r'\g<1>' + new_text + ' \u2192' + r'\g<2>'
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        count += 1
        content = new_content

blog_path.write_text(content, encoding='utf-8')
print(f'Updated {count} article link texts in blog.html')
