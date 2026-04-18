#!/usr/bin/env python3
"""Add tutorial to uuid-generator.html"""
content = open('d:/网站开发-json/pages/uuid-generator.html', 'r', encoding='utf-8').read()

tutorial = '''<div class="tutorial-section" style="max-width:1200px;margin:0 auto;padding:2rem;padding-top:0;">
    <h2 style="font-size:1.5rem;margin-bottom:1rem;color:var(--primary);">UUID Generator: Complete Guide</h2>
    <div style="display:grid;gap:1.5rem;">
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">What is UUID?</h3>
            <p style="color:var(--text-secondary);line-height:1.7;">UUID (Universally Unique Identifier) is a 128-bit label used to identify information. The most common format is UUID v4, which is randomly generated.</p>
            <p style="color:var(--text-secondary);line-height:1.7;margin-top:0.5rem;">Example: <code style="background:var(--bg-secondary);padding:0.125rem 0.375rem;border-radius:4px;">550e8400-e29b-41d4-a716-446655440000</code></p>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">UUID Versions Explained</h3>
            <div style="display:grid;gap:0.75rem;">
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;">
                    <div style="font-weight:600;">UUID v4 (Random)</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Uses cryptographically random numbers. Best for most use cases.</div>
                </div>
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;">
                    <div style="font-weight:600;">UUID v7 (Time-ordered)</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Contains timestamp, sortable by creation time. Great for databases.</div>
                </div>
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;">
                    <div style="font-weight:600;">UUID v1 (Timestamp)</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Contains MAC address and timestamp. Not recommended for privacy.</div>
                </div>
            </div>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Common Use Cases</h3>
            <ul style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;">
                <li><strong>Database primary keys</strong> - Unique identifiers for records</li>
                <li><strong>API endpoints</strong> - Unique resource identifiers</li>
                <li><strong>Session IDs</strong> - Secure session identification</li>
                <li><strong>File naming</strong> - Unique file identifiers</li>
            </ul>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Code Examples</h3>
            <div style="background:var(--bg-card);padding:1rem;border-radius:8px;overflow-x:auto;">
                <div style="margin-bottom:0.75rem;">
                    <div style="font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.25rem;">JavaScript</div>
                    <code style="font-family:monospace;font-size:0.8rem;color:#A5D6FF;">crypto.randomUUID()</code>
                </div>
                <div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.25rem;">Python</div>
                    <code style="font-family:monospace;font-size:0.8rem;color:#A5D6FF;">import uuid; uuid.uuid4()</code>
                </div>
            </div>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Related Tools</h3>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                <a href="hash-generator.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">Hash Generator</a>
                <a href="timestamp-converter.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">Timestamp Converter</a>
            </div>
        </div>
    </div>
</div>'''

idx = content.find('</main>')
if idx > 0:
    new_content = content[:idx] + tutorial + content[idx:]
    open('d:/网站开发-json/pages/uuid-generator.html', 'w', encoding='utf-8').write(new_content)
    print('SUCCESS: Tutorial added to uuid-generator.html')
else:
    print('ERROR: </main> not found')
