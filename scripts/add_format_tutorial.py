#!/usr/bin/env python3
"""Add tutorial section to format.html"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read the file
with open(r'd:\网站开发-json\pages\format.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tutorial HTML to insert before </main>
tutorial_html = '''
        <!-- Tutorial Section - SEO Content -->
        <div class="tutorial-section" style="max-width:1200px;margin:0 auto;padding:2rem;padding-top:0;">
            <h2 style="font-size:1.5rem;margin-bottom:1rem;color:var(--primary);">JSON Formatter: Complete Guide for Developers</h2>
            <div style="display:grid;gap:1.5rem;">
                <div>
                    <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">What is JSON and Why Format It?</h3>
                    <p style="color:var(--text-secondary);line-height:1.7;">JSON (JavaScript Object Notation) is the most common data format for web APIs. When you copy JSON from an API response, it is often minified (single line). Our JSON formatter beautifies it with proper indentation, making it readable.</p>
                </div>
                <div>
                    <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">How to Use This JSON Formatter</h3>
                    <ol style="color:var(--text-secondary);line-height:1.8;padding-left:1.5rem;">
                        <li><strong>Paste your JSON</strong> into the input area on the left</li>
                        <li><strong>Click Format</strong> to beautify with 2-space indentation</li>
                        <li><strong>Use Validate</strong> to check for syntax errors</li>
                        <li><strong>Use Compress</strong> to remove all whitespace</li>
                        <li><strong>Copy or download</strong> the result</li>
                    </ol>
                </div>
                <div>
                    <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Common JSON Syntax Errors</h3>
                    <div style="background:var(--bg-card);padding:1rem;border-radius:8px;overflow-x:auto;">
                        <table style="width:100%;border-collapse:collapse;font-size:0.875rem;">
                            <tr style="border-bottom:1px solid var(--bg-secondary);">
                                <th style="text-align:left;padding:0.5rem;color:var(--primary);">Error</th>
                                <th style="text-align:left;padding:0.5rem;color:var(--primary);">Fix</th>
                            </tr>
                            <tr>
                                <td style="padding:0.5rem;color:#EF4444;">Unexpected token</td>
                                <td style="padding:0.5rem;color:var(--text-secondary);">Check for missing commas</td>
                            </tr>
                            <tr>
                                <td style="padding:0.5rem;color:#EF4444;">Unexpected string</td>
                                <td style="padding:0.5rem;color:var(--text-secondary);">Use double quotes, not single</td>
                            </tr>
                            <tr>
                                <td style="padding:0.5rem;color:#EF4444;">Unexpected end</td>
                                <td style="padding:0.5rem;color:var(--text-secondary);">Check matching brackets</td>
                            </tr>
                        </table>
                    </div>
                </div>
                <div>
                    <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Code Examples</h3>
                    <div style="background:var(--bg-card);padding:1rem;border-radius:8px;overflow-x:auto;">
                        <div style="margin-bottom:1rem;">
                            <div style="font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.25rem;">JavaScript</div>
                            <code style="font-family:monospace;font-size:0.8rem;color:#A5D6FF;">const formatted = JSON.stringify(JSON.parse(json), null, 2);</code>
                        </div>
                        <div>
                            <div style="font-size:0.75rem;color:var(--text-secondary);margin-bottom:0.25rem;">Python</div>
                            <code style="font-family:monospace;font-size:0.8rem;color:#A5D6FF;">import json formatted = json.dumps(json.loads(json_str), indent=2)</code>
                        </div>
                    </div>
                </div>
                <div>
                    <h3 style="font-size:1.125rem;margin-bottom:0.5rem;">Related Tools</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <a href="json2csv.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON to CSV</a>
                        <a href="compare.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Compare</a>
                        <a href="viewer.html" style="padding:0.5rem 1rem;background:var(--bg-card);border-radius:6px;color:var(--text-secondary);text-decoration:none;font-size:0.875rem;">JSON Viewer</a>
                    </div>
                </div>
            </div>
        </div>
'''

# Find the </main> tag and insert tutorial before it
marker = '</main>'
if marker in content:
    idx = content.find(marker)
    new_content = content[:idx] + tutorial_html + content[idx:]
    
    with open(r'd:\网站开发-json\pages\format.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: Tutorial added to format.html')
else:
    print('ERROR: </main> not found')
    print('Last 500 chars:', content[-500:])
