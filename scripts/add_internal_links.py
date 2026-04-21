"""
为工具页和博客文章添加内部链接
- 工具页: 在 FAQ 后添加 Related Tools 区块
- 博客文章: 在文章末尾添加工具推荐区块
"""
import re
from pathlib import Path

PROJECT = Path("d:/网站开发-json")
PAGES = PROJECT / "pages"
BLOG = PAGES / "blog"

# ============================================================
# Related Tools - 各工具页的相关工具推荐
# ============================================================

RELATED_TOOLS = {
    'format.html': [
        {'name': 'JSON Minifier', 'href': 'clean.html', 'desc': 'Compress JSON by removing whitespace'},
        {'name': 'JSON Escape', 'href': 'escape.html', 'desc': 'Escape special characters in JSON'},
        {'name': 'JSON Viewer', 'href': 'viewer.html', 'desc': 'Visualize JSON in tree view'},
    ],
    'escape.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format and validate JSON'},
        {'name': 'URL Encoder', 'href': 'url-encoder.html', 'desc': 'Encode/decode URL strings'},
        {'name': 'Base64 Encoder', 'href': 'base64.html', 'desc': 'Encode/decode Base64'},
    ],
    'extract.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON for extraction'},
        {'name': 'JSON Viewer', 'href': 'viewer.html', 'desc': 'Explore JSON structure visually'},
        {'name': 'JSON Sort', 'href': 'sort.html', 'desc': 'Sort JSON keys and arrays'},
    ],
    'sort.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON before sorting'},
        {'name': 'JSON Clean', 'href': 'clean.html', 'desc': 'Remove nulls and duplicates'},
        {'name': 'JSON Compare', 'href': 'compare.html', 'desc': 'Compare two JSON documents'},
    ],
    'clean.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Reformat cleaned JSON'},
        {'name': 'JSON Sort', 'href': 'sort.html', 'desc': 'Sort cleaned JSON data'},
        {'name': 'JSON Compare', 'href': 'compare.html', 'desc': 'Find differences in JSON'},
    ],
    'xml.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON after conversion'},
        {'name': 'JSON YAML', 'href': 'yaml.html', 'desc': 'Convert JSON to YAML'},
        {'name': 'JSON Escape', 'href': 'escape.html', 'desc': 'Handle special XML characters'},
    ],
    'yaml.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON after conversion'},
        {'name': 'JSON XML', 'href': 'xml.html', 'desc': 'Convert JSON to XML'},
        {'name': 'JSON to CSV', 'href': 'json2csv.html', 'desc': 'Convert JSON to CSV'},
    ],
    'viewer.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Beautify JSON for viewing'},
        {'name': 'JSON Extract', 'href': 'extract.html', 'desc': 'Extract specific data paths'},
        {'name': 'JSON Compare', 'href': 'compare.html', 'desc': 'Compare JSON documents'},
    ],
    'json2csv.html': [
        {'name': 'CSV to Excel', 'href': 'csv-to-excel.html', 'desc': 'Convert CSV to Excel format'},
        {'name': 'Merge CSV', 'href': 'merge-csv.html', 'desc': 'Combine multiple CSV files'},
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON before export'},
    ],
    'compare.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON before comparing'},
        {'name': 'JSON Clean', 'href': 'clean.html', 'desc': 'Remove differences from nulls'},
        {'name': 'JSON Viewer', 'href': 'viewer.html', 'desc': 'Visualize JSON differences'},
    ],
    'csv-to-excel.html': [
        {'name': 'JSON to CSV', 'href': 'json2csv.html', 'desc': 'Convert JSON to CSV first'},
        {'name': 'Merge CSV', 'href': 'merge-csv.html', 'desc': 'Combine CSV files'},
        {'name': 'Remove Duplicates', 'href': 'excel-remove-duplicates.html', 'desc': 'Clean Excel data'},
    ],
    'merge-csv.html': [
        {'name': 'CSV to Excel', 'href': 'csv-to-excel.html', 'desc': 'Convert merged CSV to Excel'},
        {'name': 'JSON to CSV', 'href': 'json2csv.html', 'desc': 'Convert JSON to CSV before merging'},
        {'name': 'Remove Duplicates', 'href': 'excel-remove-duplicates.html', 'desc': 'Clean merged data'},
    ],
    'excel-remove-duplicates.html': [
        {'name': 'CSV to Excel', 'href': 'csv-to-excel.html', 'desc': 'Convert CSV/XLSX files'},
        {'name': 'Merge CSV', 'href': 'merge-csv.html', 'desc': 'Combine CSV files'},
        {'name': 'JSON to CSV', 'href': 'json2csv.html', 'desc': 'Convert JSON to spreadsheet'},
    ],
    'css-minifier.html': [
        {'name': 'HTML Encoder', 'href': 'html-encoder.html', 'desc': 'Encode HTML entities'},
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JSON config files'},
    ],
    'html-encoder.html': [
        {'name': 'URL Encoder', 'href': 'url-encoder.html', 'desc': 'Encode URL strings'},
        {'name': 'Base64 Encoder', 'href': 'base64.html', 'desc': 'Encode binary data'},
    ],
    'url-encoder.html': [
        {'name': 'Base64 Encoder', 'href': 'base64.html', 'desc': 'Encode binary data as text'},
        {'name': 'HTML Encoder', 'href': 'html-encoder.html', 'desc': 'Encode HTML entities'},
    ],
    'base64.html': [
        {'name': 'URL Encoder', 'href': 'url-encoder.html', 'desc': 'Encode URL strings'},
        {'name': 'Hash Generator', 'href': 'hash-generator.html', 'desc': 'Generate cryptographic hashes'},
    ],
    'jwt-decoder.html': [
        {'name': 'JSON Viewer', 'href': 'viewer.html', 'desc': 'Explore JWT payload'},
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format JWT claims'},
    ],
    'regex-tester.html': [
        {'name': 'JSON Extract', 'href': 'extract.html', 'desc': 'Extract data with JSONPath'},
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Validate JSON with regex'},
    ],
    'uuid-generator.html': [
        {'name': 'Hash Generator', 'href': 'hash-generator.html', 'desc': 'Generate secure hashes'},
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format UUID data'},
    ],
    'timestamp-converter.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Format timestamp data'},
        {'name': 'UUID Generator', 'href': 'uuid-generator.html', 'desc': 'Generate unique IDs'},
    ],
    'hash-generator.html': [
        {'name': 'Base64 Encoder', 'href': 'base64.html', 'desc': 'Encode hash results'},
        {'name': 'UUID Generator', 'href': 'uuid-generator.html', 'desc': 'Generate unique identifiers'},
    ],
    'pdf-split.html': [
        {'name': 'Batch Renamer', 'href': 'batch-file-renamer.html', 'desc': 'Organize PDF files'},
    ],
    'batch-file-renamer.html': [
        {'name': 'CSV to Excel', 'href': 'csv-to-excel.html', 'desc': 'Convert data files'},
        {'name': 'Merge CSV', 'href': 'merge-csv.html', 'desc': 'Combine data files'},
    ],
    # Static pages
    'blog.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Free JSON formatting tool'},
        {'name': 'JSON Compare', 'href': 'compare.html', 'desc': 'Compare JSON documents'},
    ],
    'news.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Free JSON formatting tool'},
        {'name': 'Best Practices', 'href': 'best-practices.html', 'desc': 'JSON development guide'},
    ],
    'best-practices.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Validate your JSON'},
        {'name': 'JSON Schema Guide', 'href': 'blog/json-schema-complete-guide-2026.html', 'desc': 'Learn JSON Schema'},
    ],
    'about.html': [
        {'name': 'JSON Formatter', 'href': 'format.html', 'desc': 'Try our most popular tool'},
        {'name': 'Best Practices', 'href': 'best-practices.html', 'desc': 'JSON development guide'},
    ],
}


def build_related_tools_html(tools, page_name='tool'):
    """Build Related Tools HTML block"""
    cards_html = ''
    for tool in tools:
        # Determine href path
        if tool['href'].startswith('blog/') or tool['href'].startswith('news/'):
            href = f'../{tool["href"]}'
        else:
            href = f'../pages/{tool["href"]}'

        cards_html += f'''        <a href="{href}" class="related-tool-card">
            <strong>{tool['name']}</strong>
            <span>{tool['desc']}</span>
        </a>'''

    return f'''
    <section class="related-tools-section">
        <h2>Related Tools</h2>
        <div class="related-tools-grid">
{cards_html}
        </div>
    </section>'''


def add_related_tools_to_tool_pages():
    """Add Related Tools section to tool pages"""
    count = 0
    for filename, tools in RELATED_TOOLS.items():
        filepath = PAGES / filename
        if not filepath.exists():
            continue

        content = open(filepath, 'r', encoding='utf-8').read()

        # Check if already has Related Tools
        if 'related-tools-section' in content:
            continue

        # Insert before </main>
        related_html = build_related_tools_html(tools)
        if '</main>' in content:
            content = content.replace('</main>', related_html + '\n</main>')
            open(filepath, 'w', encoding='utf-8').write(content)
            print(f'  [OK] {filename} - Related Tools added')
            count += 1
        else:
            print(f'  [WARN] {filename} - No </main> found')

    return count


# ============================================================
# Tool links in blog articles
# ============================================================

TOOL_LINKS_IN_BLOGS = {
    'format.html': '../pages/format.html',
    'json-formatter': '../pages/format.html',
    'json-to-csv': '../pages/json2csv.html',
    'json2csv': '../pages/json2csv.html',
    'compare': '../pages/compare.html',
    'json-compare': '../pages/compare.html',
    'json-viewer': '../pages/viewer.html',
    'viewer': '../pages/viewer.html',
    'escape': '../pages/escape.html',
    'json-escape': '../pages/escape.html',
    'yaml': '../pages/yaml.html',
    'json-to-yaml': '../pages/yaml.html',
    'xml': '../pages/xml.html',
    'json-to-xml': '../pages/xml.html',
    'clean': '../pages/clean.html',
    'json-clean': '../pages/clean.html',
    'sort': '../pages/sort.html',
    'json-sort': '../pages/sort.html',
}


def add_tool_links_to_blog_article(filepath):
    """Add tool links to blog article body"""
    content = open(filepath, 'r', encoding='utf-8').read()

    # Check if already has tool links section
    if 'tool-recommendations' in content:
        return False

    slug = filepath.stem

    # Determine which tools to recommend based on article content
    tools = []
    content_lower = open(filepath, 'r', encoding='utf-8').read().lower()

    if 'schema' in content_lower:
        tools.append({'name': 'JSON Schema Validator', 'href': '../pages/format.html', 'desc': 'Validate JSON Schema online'})
    if 'api' in content_lower or 'rest' in content_lower or 'http' in content_lower:
        tools.append({'name': 'JSON Formatter', 'href': '../pages/format.html', 'desc': 'Format and debug API responses'})
    if 'csv' in content_lower or 'excel' in content_lower or 'spreadsheet' in content_lower:
        tools.append({'name': 'JSON to CSV', 'href': '../pages/json2csv.html', 'desc': 'Convert JSON to CSV'})
    if 'yaml' in content_lower:
        tools.append({'name': 'JSON to YAML', 'href': '../pages/yaml.html', 'desc': 'Convert JSON to YAML'})
    if 'xml' in content_lower:
        tools.append({'name': 'JSON to XML', 'href': '../pages/xml.html', 'desc': 'Convert JSON to XML'})
    if 'jwt' in content_lower or 'token' in content_lower:
        tools.append({'name': 'JWT Decoder', 'href': '../pages/jwt-decoder.html', 'desc': 'Decode JWT tokens'})
    if 'compare' in content_lower or 'diff' in content_lower:
        tools.append({'name': 'JSON Compare', 'href': '../pages/compare.html', 'desc': 'Compare JSON documents'})
    if 'escape' in content_lower or 'special characters' in content_lower:
        tools.append({'name': 'JSON Escape', 'href': '../pages/escape.html', 'desc': 'Escape JSON strings'})

    # Always add formatter as default
    if not tools:
        tools = [{'name': 'JSON Formatter', 'href': '../pages/format.html', 'desc': 'Free JSON formatting tool'}]

    tools_html = build_related_tools_html(tools[:3], 'blog')

    # Insert before </main>
    if '</main>' in content:
        content = content.replace('</main>', tools_html + '\n</main>')
        open(filepath, 'w', encoding='utf-8').write(content)
        return True
    return False


def add_tool_links_to_all_blogs():
    """Add tool links to all blog articles"""
    count = 0
    if not BLOG.exists():
        return count
    for filepath in sorted(BLOG.glob('*.html')):
        if add_tool_links_to_blog_article(filepath):
            print(f'  [OK] {filepath.name} - Tool links added')
            count += 1
    return count


# ============================================================
# Main
# ============================================================
print('=' * 60)
print('Adding Internal Links')
print('=' * 60)

print('\n[*] Adding Related Tools to tool pages...')
count1 = add_related_tools_to_tool_pages()

print(f'\n[*] Adding Tool Links to blog articles...')
count2 = add_tool_links_to_all_blogs()

print(f'\n[*] Summary: {count1} tool pages, {count2} blog articles updated')
print('=' * 60)
