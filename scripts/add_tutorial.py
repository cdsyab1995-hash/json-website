#!/usr/bin/env python3
"""Add tutorial to format.html"""
content = open('d:/网站开发-json/pages/format.html', 'r', encoding='utf-8').read()
tutorial = '''<div class="tutorial-section" style="max-width:1200px;margin:0 auto;padding:2rem;padding-top:0;">
    <h2 style="font-size:1.5rem;margin-bottom:1rem;color:var(--primary);">JSON Formatter: Complete Guide for Developers</h2>
    <p style="color:var(--text-secondary);line-height:1.7;">Learn how to format, validate, and compress JSON data with our free online tool.</p>
</div>'''
idx = content.find('</main>')
if idx > 0:
    new_content = content[:idx] + tutorial + content[idx:]
    open('d:/网站开发-json/pages/format.html', 'w', encoding='utf-8').write(new_content)
    print('SUCCESS')
else:
    print('ERROR: </main> not found')
