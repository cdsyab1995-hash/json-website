#!/usr/bin/env python3
"""Add tutorial to json2csv.html"""
content = open('d:/网站开发-json/pages/json2csv.html', 'r', encoding='utf-8').read()

tutorial = '''<div class="tutorial-section" style="max-width:1200px;margin:0 auto;padding:2rem;padding-top:0;">
    <h2 style="font-size:1.5rem;margin-bottom:1rem;color:var(--primary);">JSON to CSV: Complete Guide</h2>
    <div style="display:grid;gap:1.5rem;">
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">When to Convert JSON to CSV</h3>
            <p style="color:var(--text-secondary);line-height:1.7;">JSON to CSV conversion is useful when you need to:</p>
            <ul style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;margin-top:0.5rem;">
                <li>Import API data into Excel or Google Sheets</li>
                <li>Analyze JSON data in data visualization tools</li>
                <li>Share structured data with non-technical users</li>
                <li>Create backups of configuration data</li>
            </ul>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">How to Use This Tool</h3>
            <ol style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;">
                <li><strong>Paste JSON array</strong> into the input (must be array of objects)</li>
                <li><strong>Click Convert</strong> to generate CSV</li>
                <li><strong>Download</strong> as .csv file or copy to clipboard</li>
            </ol>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Supported JSON Structure</h3>
            <div style="background:var(--bg-card);padding:1rem;border-radius:8px;overflow-x:auto;">
                <div style="font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.5rem;">Valid JSON (array of objects):</div>
                <code style="font-family:monospace;font-size:0.8rem;color:#A5D6FF;">[{"name":"John","age":30},{"name":"Jane","age":25}]</code>
                <div style="font-size:0.75rem;color:var(--text-secondary);margin:0.5rem 0;">Invalid JSON (nested objects need flattening):</div>
                <code style="font-family:monospace;font-size:0.8rem;color:#EF4444;">{"user":{"name":"John"}}</code>
            </div>
        </div>
        <div>
            <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Related Tools</h3>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                <a href="format.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Formatter</a>
                <a href="compare.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Compare</a>
            </div>
        </div>
    </div>
</div>'''

idx = content.find('</main>')
if idx > 0:
    new_content = content[:idx] + tutorial + content[idx:]
    open('d:/网站开发-json/pages/json2csv.html', 'w', encoding='utf-8').write(new_content)
    print('SUCCESS: Tutorial added to json2csv.html')
else:
    print('ERROR: </main> not found')
