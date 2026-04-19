# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open('d:/网站开发-json/index.html', encoding='utf-8').read()
print(f"File size: {len(content)} bytes")

# Find the 04-15 article marker
p = content.find('2026-04-15')
print(f"'2026-04-15' at position: {p}")

if p == -1:
    print("04-15 not found in file")
else:
    # Find the <article class="feature-card" that starts this block
    # Search backwards for the opening <article
    marker = '<article class="feature-card"'
    pos = p
    article_start = content.rfind(marker, max(0, pos - 1000), pos)
    print(f"Article start (backward search from {pos}): {article_start}")

    # Find the closing </article> after the 04-15 text
    # The 04-15 article ends with "Read more →</a>\n </article>"
    after_04_15 = content.find('</article>', p)
    print(f"Article end (forward search): {after_04_15}")

    if article_start != -1 and after_04_15 != -1:
        # Extract the full article block
        old_block = content[article_start:after_04_15 + len('</article>')]
        print(f"\nOld block length: {len(old_block)}")
        # Clean for display (remove emojis and long spaces)
        clean = old_block.replace('\n', ' ').replace('  ', ' ')
        # Truncate for display
        print(f"Old block preview: {clean[:200]}...")

        # New article block (on a single line, matching the style)
        new_block = ''' <article class="feature-card" style="text-align: left;">
 <span class="class="text-small text-secondary"">2026-04-19</span>
 <h3 class="class="text-lg text-primary mb-sm"">&#128274; JWT Security Best Practices 2026: Protect Your JSON Web Token Implementation</h3>
 <p style="color: var(--text-secondary); font-size: 0.95rem;"> JSON Web Tokens are everywhere — but most implementations have at least one critical security flaw. This guide covers algorithm confusion attacks, weak key vulnerabilities, token expiration pitfalls, and production security checklists for US developers building authentication systems in 2026. </p>
 <a href="pages/blog/jwt-security-best-practices-2026.html" class="class="inline-block mt-sm text-primary" style="font-weight:500">Read more &#8594;</a>
 </article>'''

        # Actually, let's use the actual HTML entity format instead of emoji
        # and keep it consistent with existing articles
        new_block = ''' <article class="feature-card" style="text-align: left;">
 <span class="class="text-small text-secondary"">2026-04-19</span>
 <h3 class="class="text-lg text-primary mb-sm"">&#128274; JWT Security Best Practices 2026: Protect Your JSON Web Token Implementation</h3>
 <p style="color: var(--text-secondary); font-size: 0.95rem;"> JSON Web Tokens are everywhere — but most implementations have at least one critical security flaw. This guide covers algorithm confusion attacks, weak key vulnerabilities, token expiration pitfalls, and production security checklists for US developers building authentication systems in 2026. </p>
 <a href="pages/blog/jwt-security-best-practices-2026.html" class="class="inline-block mt-sm text-primary" style="font-weight:500">Read more &#8594;</a>
 </article>'''

        # Do the replacement
        new_content = content[:article_start] + new_block + content[after_04_15 + len('</article>'):]
        print(f"\nNew content size: {len(new_content)}")

        # Verify JWT is now in the file
        if '2026-04-19' in new_content:
            print("SUCCESS: 04-19 article is now in the file")
        else:
            print("ERROR: 04-19 not found after replacement")

        if '2026-04-15' in new_content:
            print("WARNING: 04-15 still in file")
        else:
            print("SUCCESS: 04-15 removed from file")

        # Write back
        open('d:/网站开发-json/index.html', 'w', encoding='utf-8').write(new_content)
        print("\nFile written successfully!")
    else:
        print("Could not find article boundaries")
