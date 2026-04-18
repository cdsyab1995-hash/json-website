#!/usr/bin/env python3
"""Add tutorial to compare.html"""
content = open('d:/网站开发-json/pages/compare.html', 'r', encoding='utf-8').read()

tutorial = '''<div class="tutorial-section" style="max-width:1200px;margin:0 auto;padding:2rem;padding-top:0;">
    <h2 style="font-size:1.5rem;margin-bottom:1rem;color:var(--primary);">JSON Compare Tool: Complete Guide</h2>
    <div style="display:grid;gap:1.5rem;">
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Why Compare JSON Documents?</h3>
            <p style="color:var(--text-secondary);line-height:1.7;">JSON comparison is essential for:</p>
            <ul style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;margin-top:0.5rem;">
                <li><strong>API debugging</strong> - Find differences between staging and production</li>
                <li><strong>Config changes</strong> - Track changes in configuration files</li>
                <li><strong>Data migration</strong> - Verify data integrity after transfer</li>
                <li><strong>Code review</strong> - Compare JSON output from different versions</li>
            </ul>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">How to Compare JSON</h3>
            <ol style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;">
                <li><strong>Paste original JSON</strong> in the left panel</li>
                <li><strong>Paste modified JSON</strong> in the right panel</li>
                <li><strong>Click Compare</strong> to see differences</li>
                <li><strong>Review highlighted changes</strong> - green for added, red for removed</li>
            </ol>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Diff Color Legend</h3>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0.75rem;">
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;border-left:3px solid #22C55E;">
                    <div style="font-weight:600;">Added</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Fields in modified only</div>
                </div>
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;border-left:3px solid #EF4444;">
                    <div style="font-weight:600;">Removed</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Fields in original only</div>
                </div>
                <div style="padding:0.75rem;background:var(--bg-card);border-radius:8px;border-left:3px solid #F59E0B;">
                    <div style="font-weight:600;">Changed</div>
                    <div style="font-size:0.75rem;color:var(--text-secondary);">Different values</div>
                </div>
            </div>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Use Cases</h3>
            <div style="background:var(--bg-card);padding:1rem;border-radius:8px;">
                <div style="font-size:0.875rem;color:var(--text-secondary);">
                    <strong>API Response Comparison:</strong> Compare responses from different API versions<br>
                    <strong>Config Diff:</strong> Review changes before deploying new configuration<br>
                    <strong>Test Verification:</strong> Compare expected vs actual JSON output
                </div>
            </div>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Related Tools</h3>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                <a href="format.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Formatter</a>
                <a href="viewer.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Viewer</a>
            </div>
        </div>
    </div>
</div>'''

idx = content.find('</main>')
if idx > 0:
    new_content = content[:idx] + tutorial + content[idx:]
    open('d:/网站开发-json/pages/compare.html', 'w', encoding='utf-8').write(new_content)
    print('SUCCESS: Tutorial added to compare.html')
else:
    print('ERROR: </main> not found')
