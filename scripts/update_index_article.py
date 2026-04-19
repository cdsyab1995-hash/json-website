"""
Update index.html with new JWT article.
- Remove the 04-15 article (MCP)
- Add the 04-19 JWT article at the top
"""
import re

with open('d:/网站开发-json/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The old 04-15 article to remove
old_article = ''' <article class="feature-card" style="text-align: left;">
 <span class="class="text-small text-secondary"">2026-04-15</span>
 <h3 class="class="text-lg text-primary mb-sm"">🤖 AI Tool Calling with JSON: How MCP is Standardizing Agent-Software Communication in 2026</h3>
 <p style="color: var(--text-secondary); font-size: 0.95rem;"> AI agents are no longer just generating text — they're executing actions. The Model Context Protocol (MCP) is becoming the universal standard for AI tool interfaces, using JSON Schema as the contract between human intent and AI execution. Learn how tool calling works, MCP's architecture, and practices for building reliable AI-powered applications with structured JSON payloads. </p>
 <a href="pages/blog.html#ai-daily-20260415" class="class="inline-block mt-sm text-primary" style="font-weight:500">Read more →</a>
 </article></article>'''

# New JWT article to add at the top
new_article = ''' <article class="feature-card" style="text-align: left;">
 <span class="class="text-small text-secondary"">2026-04-19</span>
 <h3 class="class="text-lg text-primary mb-sm"">🔐 JWT Security Best Practices 2026: Protect Your JSON Web Token Implementation</h3>
 <p style="color: var(--text-secondary); font-size: 0.95rem;"> JSON Web Tokens are everywhere — but most implementations have at least one critical security flaw. This guide covers algorithm confusion attacks, weak key vulnerabilities, token expiration pitfalls, and production security checklists for US developers building authentication systems in 2026. </p>
 <a href="pages/blog/jwt-security-best-practices-2026.html" class="class="inline-block mt-sm text-primary" style="font-weight:500">Read more →</a>
 </article>'''

# Pattern: find the section between the last article (04-15) and its closing tag
# The articles are inside <section class="tool-area mt-lg">...<h2 class="section-label" class="class="text-xl mb-md"">Latest Articles</h2>...<div class="feature-grid">...</div></section>

# Find the article block for 04-15 (the last one before the </div></section>)
pattern = r'( <article class="feature-card" style="text-align: left;">\s*<span class="class="text-small text-secondary"">2026-04-15</span>\s*<h3 class="class="text-lg text-primary mb-sm"">🤖 AI Tool Calling with JSON: How MCP is Standardizing Agent-Software Communication in 2026</h3>\s*<p style="color: var\( --text-secondary\); font-size: 0\.95rem;"> AI agents are no longer just generating text — they[\s\S]*?Read more →</a>\s*</article>)'

if '2026-04-15</span>' in content:
    # Remove the 04-15 article
    content_new = re.sub(pattern, '', content, count=1)
    print(f"Removed 04-15 article")

    # Add new article at the start (after <div class="feature-grid">)
    content_new = content_new.replace(
        '<article class="feature-card" style="text-align: left;">\n <span class="class="text-small text-secondary"">2026-04-18</span>',
        new_article + '\n <article class="feature-card" style="text-align: left;">\n <span class="class="text-small text-secondary"">2026-04-18</span>'
    )

    with open('d:/网站开发-json/index.html', 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("Updated index.html successfully")
else:
    print("ERROR: Could not find 04-15 article")
