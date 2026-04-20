#!/usr/bin/env python3
"""
统一工具页交互框架 - 添加缺失的组件
- 示例模板 (templateSelect)
- FAQ 区域
- Use Cases 区域
"""

import os
import re

PAGES_DIR = r"d:\网站开发-json\pages"

# 工具页列表（核心 JSON 工具）
TOOL_PAGES = [
    "format.html",
    "escape.html",
    "extract.html",
    "sort.html",
    "clean.html",
    "viewer.html",
    "json2csv.html",
    "compare.html",
    "xml.html",
    "yaml.html",
]

# 各工具页的元数据
TOOL_METADATA = {
    "format.html": {
        "title": "JSON Formatter",
        "name": "Format",
        "description": "Format, validate, and compress JSON strings with real-time preview",
        "examples": [
            ("API Response", '{\n  "id": 1,\n  "name": "John Doe",\n  "email": "john@example.com",\n  "skills": ["JavaScript", "Python"]\n}'),
            ("User Config", '{\n  "theme": "dark",\n  "language": "en",\n  "notifications": true\n}'),
            ("Product Data", '{\n  "productId": "SKU-12345",\n  "price": 29.99,\n  "inStock": true\n}'),
            ("package.json", '{\n  "name": "my-project",\n  "version": "1.0.0",\n  "dependencies": {\n    "lodash": "^4.17.21"\n  }\n}'),
        ],
        "usecases": [
            ("API Response Debugging", "Quickly format and validate API responses to spot errors"),
            ("Config File Cleaning", "Clean up messy configuration files for readability"),
            ("Data Compression", "Minify JSON for production deployment"),
        ],
        "faqs": [
            ("How many spaces for indentation?", "Uses 2 spaces, the most common JSON standard"),
            ("Does compression lose data?", "No. Only removes formatting whitespace, data stays intact"),
            ("What errors can be detected?", "Missing quotes, trailing commas, mismatched brackets"),
        ],
    },
    "escape.html": {
        "title": "JSON Escape",
        "name": "Escape",
        "description": "Escape and unescape JSON strings for safe API transmission",
        "examples": [
            ("API Payload", '{"message": "Hello, \\"World\\"!"}'),
            ("Newlines", '{"text": "Line 1\\nLine 2\\nLine 3"}'),
            ("Special Chars", '{"path": "C:\\\\Users\\\\Name\\\\File"}'),
        ],
        "usecases": [
            ("API Payload Preparation", "Safely encode JSON for POST/PUT requests"),
            ("Database Storage", "Escape special characters before storing JSON"),
            ("Config Files", "Handle paths and special characters in JSON configs"),
        ],
        "faqs": [
            ("What characters are escaped?", "Double quotes, backslashes, newlines, tabs, and control characters"),
            ("Why escape for APIs?", "Prevents JSON parsing errors when special characters appear"),
            ("Can I unescape?", "Yes - use the Unescape button to decode escaped strings"),
        ],
    },
    "extract.html": {
        "title": "JSON Extract",
        "name": "Extract",
        "description": "Extract specific fields from JSON using dot notation paths",
        "examples": [
            ("Nested Object", '{\n  "user": {\n    "name": "John",\n    "address": {\n      "city": "NYC"\n    }\n  }\n}', "user.name"),
            ("Array Index", '{\n  "items": [\n    {"id": 1, "name": "A"},\n    {"id": 2, "name": "B"}\n  ]\n}', "items[0].name"),
            ("Deep Path", '{\n  "data": {\n    "results": [\n      {"score": 95}\n    ]\n  }\n}', "data.results[0].score"),
        ],
        "usecases": [
            ("API Data Parsing", "Extract specific fields from large API responses"),
            ("Configuration Access", "Pull config values without parsing the entire file"),
            ("Data Transformation", "Select only needed fields for downstream processing"),
        ],
        "faqs": [
            ("What is dot notation?", "Like 'user.address.city' - dot separates each level of nesting"),
            ("How to access arrays?", "Use index like 'items[0].name' for first item"),
            ("What if path doesn't exist?", "Returns undefined/null, no error thrown"),
        ],
    },
    "sort.html": {
        "title": "JSON Sort",
        "name": "Sort",
        "description": "Sort JSON object keys alphabetically or recursively",
        "examples": [
            ("Simple Object", '{"z":1,"a":2,"m":3}'),
            ("Nested Object", '{"z":{"x":1},"a":{"y":2}}'),
            ("Array of Objects", '[{"b":3},{"a":1},{"c":2}]'),
        ],
        "usecases": [
            ("Consistent Formatting", "Make JSON key order predictable across files"),
            ("Diff-Friendly Output", "Easier to compare sorted JSON in version control"),
            ("API Standardization", "Ensure consistent key ordering in API responses"),
        ],
        "faqs": [
            ("Recursive sort?", "Yes - sorts keys at all nesting levels"),
            ("Array order preserved?", "Yes - only object keys are sorted"),
            ("Ascending vs Descending?", "Ascending (A-Z) is default; descending available"),
        ],
    },
    "clean.html": {
        "title": "JSON Cleaner",
        "name": "Clean",
        "description": "Repair and clean messy JSON - fix quotes, remove nulls, trim whitespace",
        "examples": [
            ("Single Quotes", "{'name': 'John', 'age': 30}"),
            ("Trailing Commas", '{"a": 1, "b": 2, }'),
            ("Extra Whitespace", '  {  "name"  :  "John"  }  '),
        ],
        "usecases": [
            ("API Response Fixes", "Clean up JSON from poorly formatted APIs"),
            ("JavaScript to JSON", "Convert JS objects with single quotes to valid JSON"),
            ("Data Normalization", "Standardize JSON from multiple sources"),
        ],
        "faqs": [
            ("What errors can be fixed?", "Single quotes, trailing commas, extra whitespace"),
            ("Does it modify data?", "Only formatting; data values stay the same"),
            ("Can it fix bracket errors?", "No - bracket mismatches need manual correction"),
        ],
    },
    "viewer.html": {
        "title": "JSON Viewer",
        "name": "Viewer",
        "description": "Visual tree view of JSON with expand/collapse and search",
        "examples": [
            ("API Response", '{\n  "status": "success",\n  "data": {\n    "users": [\n      {"id": 1, "name": "Alice"},\n      {"id": 2, "name": "Bob"}\n    ]\n  }\n}'),
            ("Config File", '{\n  "database": {\n    "host": "localhost",\n    "port": 5432\n  }\n}'),
        ],
        "usecases": [
            ("Large JSON Exploration", "Navigate complex nested structures visually"),
            ("Data Inspection", "Quickly find and focus on specific fields"),
            ("API Debugging", "Understand API response structure at a glance"),
        ],
        "faqs": [
            ("Max nesting depth?", "Unlimited - handles deeply nested JSON"),
            ("Search functionality?", "Yes - filter tree nodes by key or value"),
            ("Copy JSONPath?", "Yes - click any node to copy its JSONPath"),
        ],
    },
    "json2csv.html": {
        "title": "JSON to CSV",
        "name": "JSON to CSV",
        "description": "Convert JSON arrays to CSV format for Excel/spreadsheets",
        "examples": [
            ("Simple Array", '[{"name":"John","age":30},{"name":"Jane","age":25}]'),
            ("Nested Data", '[{"user":{"name":"John"}},{"user":{"name":"Jane"}}]'),
            ("Multiple Types", '[{"id":1,"active":true},{"id":2,"active":false}]'),
        ],
        "usecases": [
            ("Excel Import", "Convert API JSON to CSV for spreadsheet analysis"),
            ("Data Export", "Export JSON data to CSV for external tools"),
            ("Report Generation", "Create CSV reports from JSON data sources"),
        ],
        "faqs": [
            ("Nested JSON handling?", "Flattens nested objects with dot notation (e.g., user.name)"),
            ("Array values?", "Converts to pipe-separated values within cell"),
            ("Header row?", "Yes - first row contains column names"),
        ],
    },
    "compare.html": {
        "title": "JSON Compare",
        "name": "JSON Compare",
        "description": "Compare two JSON documents side-by-side and highlight differences",
        "examples": [
            ("Text Diff", '{\n  "before": "value1",\n  "same": "unchanged"\n}', '{\n  "after": "value2",\n  "same": "unchanged"\n}'),
        ],
        "usecases": [
            ("API Response Comparison", "Compare API responses before and after changes"),
            ("Config Diff", "Spot differences between config versions"),
            ("Data Migration", "Verify data consistency between systems"),
        ],
        "faqs": [
            ("Diff highlighting?", "Yes - added (green), removed (red), changed (yellow)"),
            ("Deep comparison?", "Yes - compares nested objects and arrays recursively"),
            ("Large file support?", "Optimized for files up to 1MB"),
        ],
    },
    "xml.html": {
        "title": "JSON to XML",
        "name": "JSON to XML",
        "description": "Convert JSON to XML format and vice versa",
        "examples": [
            ("Simple Object", '{"root": {"name": "Test", "value": 123}}'),
            ("With Arrays", '{"items": {"item": ["A", "B", "C"]}}'),
        ],
        "usecases": [
            ("Legacy System Integration", "Convert JSON for XML-based APIs"),
            ("Data Transformation", "Transform between JSON and XML formats"),
            ("Enterprise Integration", "Bridge modern JSON with legacy XML systems"),
        ],
        "faqs": [
            ("Attributes support?", "JSON doesn't have attributes; use elements or prefixes"),
            ("Array handling?", "Repeats element names for array items"),
            ("Namespaces?", "Supported in XML output with prefixes"),
        ],
    },
    "yaml.html": {
        "title": "JSON to YAML",
        "name": "JSON to YAML",
        "description": "Convert JSON to YAML format for configuration files",
        "examples": [
            ("Simple Config", '{"app": {"name": "MyApp", "debug": true}}'),
            ("Environment", '{"env": {"prod": {"url": "api.example.com"}}}'),
        ],
        "usecases": [
            ("Config File Creation", "Generate YAML configs from JSON data"),
            ("Kubernetes Manifests", "Create K8s configs from JSON specifications"),
            ("Docker Compose", "Convert JSON to Docker Compose YAML"),
        ],
        "faqs": [
            ("YAML indentation?", "Uses 2-space indentation matching JSON style"),
            ("Preserve data types?", "Yes - numbers, booleans, nulls maintain their types"),
            ("Arrays supported?", "Yes - both inline and multiline formats"),
        ],
    },
}


def generate_template_html(metadata):
    """生成示例模板下拉 HTML"""
    name = metadata["name"]
    examples = metadata.get("examples", [])
    
    if not examples:
        return ""
    
    options = '<option value="">Load Example...</option>\n'
    for i, ex in enumerate(examples):
        if len(ex) == 2:
            label, _ = ex
        else:
            label, _, _ = ex
        options += f'                    <option value="example{i}">{label}</option>\n'
    
    return f'''
            <select id="templateSelect" style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--bg-secondary); background: var(--bg-secondary); cursor: pointer; color: var(--text-primary);">
{options}            </select>'''


def generate_usecases_html(metadata):
    """生成 Use Cases HTML"""
    name = metadata["name"]
    usecases = metadata.get("usecases", [])
    
    if not usecases:
        return ""
    
    cards = ""
    for title, desc in usecases:
        cards += f'''                    <div class="feature-card" style="cursor: default;">
                        <h3 style="font-size: 1rem;">{title}</h3>
                        <p>{desc}</p>
                    </div>
'''
    
    return f'''    <!-- Use Cases -->
    <section class="tool-area">
        <h2 class="section-label text-lg mb-md"">{name} Common Use Cases</h2>
        <div class="feature-grid" style="margin-top: 0;">
{cards}        </div>
    </section>'''


def generate_faq_html(metadata):
    """生成 FAQ HTML"""
    name = metadata["name"]
    faqs = metadata.get("faqs", [])
    
    if not faqs:
        return ""
    
    faq_items = ""
    for q, a in faqs:
        faq_items += f'''            <details class="faq-item">
                <summary class="faq-question">{q}</summary>
                <div class="faq-answer">
                    <p>{a}</p>
                </div>
            </details>
'''
    
    return f'''    <!-- FAQ -->
    <section class="tool-area">
        <h2 class="section-label text-lg mb-md"">{name} FAQ - Common Questions Answered</h2>
        <div class="faq-container">
{faq_items}        </div>
    </section>'''


def needs_template_select(content):
    """检查是否已有 templateSelect"""
    return 'templateSelect' in content or 'Load Example' in content


def needs_usecases(content):
    """检查是否已有 Use Cases"""
    return 'Use Cases' in content or 'Common Use Cases' in content


def needs_faq(content):
    """检查是否已有 FAQ"""
    return 'faq-container' in content or 'faq-item' in content


def add_template_select_to_toolbar(content, metadata):
    """在工具栏中添加示例模板下拉"""
    if needs_template_select(content):
        return content
    
    template_html = generate_template_html(metadata)
    if not template_html:
        return content
    
    # 找到 toolbar 的结束位置，在 Clear 按钮后面添加
    pattern = r'(<button[^>]*id="btnClear"[^>]*>.*?</button>\s*)(</div>)'
    replacement = r'\1' + template_html + r'\n                    \2'
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def add_usecases(content, metadata):
    """添加 Use Cases 区域"""
    if needs_usecases(content):
        return content
    
    usecases_html = generate_usecases_html(metadata)
    if not usecases_html:
        return content
    
    # 在 FAQ 前添加 Use Cases
    if 'faq-container' in content:
        return content.replace('    <!-- FAQ -->', usecases_html + '\n\n    <!-- FAQ -->')
    else:
        # 在 tutorial-section 前添加
        return content.replace(
            '<div class="tutorial-section"',
            usecases_html + '\n\n    <div class="tutorial-section"'
        )


def add_faq(content, metadata):
    """添加 FAQ 区域"""
    if needs_faq(content):
        return content
    
    faq_html = generate_faq_html(metadata)
    if not faq_html:
        return content
    
    # 在 tutorial-section 前添加 FAQ
    if '<div class="tutorial-section"' in content:
        return content.replace(
            '<div class="tutorial-section"',
            faq_html + '\n\n    <div class="tutorial-section"'
        )
    else:
        # 在 footer 前添加
        return content.replace(
            '</main>\n    <!-- Footer -->',
            faq_html + '\n\n</main>\n    <!-- Footer -->'
        )


def process_page(filepath, metadata):
    """处理单个页面"""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 添加示例模板
    content = add_template_select_to_toolbar(content, metadata)
    
    # 添加 Use Cases
    content = add_usecases(content, metadata)
    
    # 添加 FAQ
    content = add_faq(content, metadata)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Updated: {os.path.basename(filepath)}")
        return True
    else:
        print(f"  [--] No changes: {os.path.basename(filepath)}")
        return False


def main():
    """主函数"""
    updated = 0
    
    for page in TOOL_PAGES:
        filepath = os.path.join(PAGES_DIR, page)
        if os.path.exists(filepath):
            metadata = TOOL_METADATA.get(page, {})
            if process_page(filepath, metadata):
                updated += 1
        else:
            print(f"  [X] Not found: {page}")
    
    print(f"\n[OK] Updated {updated} pages")


if __name__ == "__main__":
    main()
