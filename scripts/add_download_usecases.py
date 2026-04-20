#!/usr/bin/env python3
"""
批量添加 download 按钮和 use cases 到所有工具页
"""
import os
import re

PAGES_DIR = r"d:\网站开发-json\pages"
PAGES = [
    'format.html', 'escape.html', 'extract.html', 'sort.html', 'clean.html',
    'viewer.html', 'json2csv.html', 'compare.html', 'xml.html', 'yaml.html'
]

# 每个工具的 use cases 配置
USECASES = {
    'format.html': [
        ('Format messy JSON', 'Clean up inconsistent indentation and spacing'),
        ('Validate API responses', 'Check if JSON is valid before processing'),
        ('Prettify for debugging', 'Make JSON readable during development'),
    ],
    'escape.html': [
        ('Escape JSON strings', 'Prepare text for use in JSON payloads'),
        ('Handle user input', 'Safely embed user content in JSON'),
        ('API request preparation', 'Escape special characters for APIs'),
    ],
    'extract.html': [
        ('Extract nested data', 'Pull out values from deep JSON structures'),
        ('Get array items', 'Access specific elements by index'),
        ('Query JSON paths', 'Use JSONPath for complex data extraction'),
    ],
    'sort.html': [
        ('Sort API responses', 'Alphabetically sort JSON keys'),
        ('Organize configurations', 'Consistent key ordering for config files'),
        ('Data normalization', 'Standardize JSON structure order'),
    ],
    'clean.html': [
        ('Remove empty values', 'Strip null, empty strings from JSON'),
        ('Compact data', 'Reduce JSON size by removing whitespace'),
        ('Data sanitization', 'Remove sensitive fields before sharing'),
    ],
    'viewer.html': [
        ('Visualize JSON', 'Tree view for complex nested structures'),
        ('Explore API data', 'Interactive navigation of JSON responses'),
        ('Debug JSON', 'Easy inspection during development'),
    ],
    'json2csv.html': [
        ('Export to Excel', 'Convert JSON arrays to CSV for spreadsheets'),
        ('Data migration', 'Transform JSON data for databases'),
        ('Generate reports', 'Create tabular data from JSON records'),
    ],
    'compare.html': [
        ('Diff JSON files', 'Spot differences between two JSON documents'),
        ('Version comparison', 'Compare API response changes'),
        ('Config audits', 'Find changes in configuration files'),
    ],
    'xml.html': [
        ('JSON to XML', 'Convert JSON responses to XML format'),
        ('API integration', 'Transform data for XML-based systems'),
        ('Data interchange', 'Convert between JSON and XML'),
    ],
    'yaml.html': [
        ('JSON to YAML', 'Convert JSON to human-readable YAML'),
        ('Config files', 'Create YAML configs from JSON data'),
        ('Documentation', 'Generate readable config documentation'),
    ],
}

def add_download_button(content, page):
    """添加 download 按钮"""
    # 查找 Copy 按钮，在其后添加 Download
    copy_pattern = r'(<button[^>]*id="btnCopy"[^>]*>.*?</button>)'
    download_btn = '''<button class="btn btn-secondary" id="btnDownload">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
        <polyline points="7 10 12 15 17 10"></polyline>
        <line x1="12" y1="15" x2="12" y2="3"></line>
    </svg>
    Download
</button>'''
    
    match = re.search(copy_pattern, content, re.DOTALL)
    if match:
        # 在 Copy 按钮后添加 Download
        old = match.group(1)
        new = old + '\n' + download_btn
        content = content.replace(old, new, 1)
        return content, True
    return content, False

def add_use_cases(content, page):
    """添加 use cases section"""
    if page not in USECASES:
        return content, False
    
    usecases = USECASES[page]
    usecases_html = '''<!-- Use Cases -->
<div class="section features-section">
    <div class="container">
        <h2><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg> Common Use Cases</h2>
        <div class="features-grid">
'''
    for title, desc in usecases:
        usecases_html += f'''            <div class="feature-card">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
'''
    usecases_html += '''        </div>
    </div>
</div>
'''
    
    # 在 faq-section 前插入 use cases
    faq_pattern = r'(<div class="section[^"]*faq-section[^"]*">)'
    match = re.search(faq_pattern, content)
    if match:
        content = content.replace(match.group(1), usecases_html + match.group(1), 1)
        return content, True
    return content, False

def process_page(page):
    """处理单个页面"""
    filepath = os.path.join(PAGES_DIR, page)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 添加 download 按钮
    content, has_download = add_download_button(content, page)
    
    # 添加 use cases
    content, has_usecases = add_use_cases(content, page)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] {page} (Download={has_download}, UseCases={has_usecases})")
        return True
    else:
        print(f"  [--] {page} (No changes)")
        return False

def main():
    print("=== Adding Download Button & Use Cases ===\n")
    updated = 0
    for page in PAGES:
        if process_page(page):
            updated += 1
    print(f"\n[OK] Updated {updated} pages")

if __name__ == "__main__":
    main()
