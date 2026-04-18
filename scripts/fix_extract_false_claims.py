#!/usr/bin/env python3
"""
Fix extract.html - remove false JSONPath claims
Reality: it's a simplified path extractor, not full JSONPath
"""
import re

extract_path = "d:/网站开发-json/pages/extract.html"

with open(extract_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Title - remove "JSONPath" false claim
content = content.replace(
    '<title>JSON Data Extractor - Extract Fields from JSON | AI JSON</title>',
    '<title>JSON Data Extractor - Extract Fields with Simple Paths | AI JSON</title>'
)

# Fix 2: meta description - remove JSONPath claim
content = content.replace(
    'Extract JSON data with simple path queries, no code required',
    'Extract JSON data with simple dot notation paths, no code required'
)

# Fix 3: OG title - remove JSONPath
content = content.replace(
    '<meta property="og:title" content="JSONPath Query Tool - Extract Data from API Responses | AI JSON">',
    '<meta property="og:title" content="JSON Data Extractor - Extract Fields from JSON | AI JSON">'
)

content = content.replace(
    '<meta property="og:description" content="Pull specific fields from API responses with JSONPath. Extract nested data without writing code. Instant for US developers.">',
    '<meta property="og:description" content="Extract specific fields from JSON API responses using simple paths. Access nested data without writing code. Instant for US developers.">'
)

# Fix 4: Twitter title
content = content.replace(
    '<meta name="twitter:title" content="JSONPath Query Tool - Extract Data from API Responses | AI JSON">',
    '<meta name="twitter:title" content="JSON Data Extractor - Extract Fields from JSON | AI JSON">'
)

content = content.replace(
    '<meta name="twitter:description" content="Pull specific fields from API responses with JSONPath. Extract nested data without writing code. Instant for US developers.">',
    '<meta name="twitter:description" content="Extract specific fields from JSON API responses using simple paths. Access nested data without writing code. Instant for US developers.">'
)

# Fix 5: JSON-LD - remove "JSONPath" false claims
content = content.replace(
    '"description": "JSONPath extractor for US developers. Extract data from complex JSON structures with ease.."',
    '"description": "Simple path extractor for US developers. Extract data from JSON with dot notation."'
)

content = content.replace(
    '"JSONPath queries"',
    '"Simple path queries"'
)

# Fix 6: FAQ section - remove full JSONPath examples
old_faq = '''<details class="faq-item">
            <summary class="faq-question">Can I extract multiple elements from an array?</summary>
            <div class="faq-answer">
                <p>Yes. Common array operations:</p>
                <ul style="margin: 0.5rem 0 0.5rem 1.5rem;">
                    <li><code>$.items[0]</code> - First element</li>
                    <li><code>$.items[-1]</code> - Last element</li>
                    <li><code>$.items[0:3]</code> - First 3 elements (slice)</li>
                </ul>
            </div>
        </details>'''

new_faq = '''<details class="faq-item">
            <summary class="faq-question">Can I extract array elements?</summary>
            <div class="faq-answer">
                <p>Yes. Basic array operations:</p>
                <ul style="margin: 0.5rem 0 0.5rem 1.5rem;">
                    <li><code>items[0]</code> - First element</li>
                    <li><code>items.0</code> - First element (dot notation)</li>
                </ul>
            </div>
        </details>'''

content = content.replace(old_faq, new_faq)

# Fix 7: FAQ - remove XPath comparison (not relevant for simplified tool)
old_xpath_faq = '''<details class="faq-item">
            <summary class="faq-question">What is the difference between JSONPath and XPath?</summary>
            <div class="faq-answer">
                <p>JSONPath is the JSON version of XPath concept. XPath is for XML documents, JSONPath is for JSON documents.</p>
                <p>Main difference: JSONPath uses <code>$</code> for root (like XPath's <code>/</code>) and <code>.</code> for property access (like XPath's <code>/</code>).</p>
            </div>
        </details>'''

new_xpath_faq = '''<details class="faq-item">
            <summary class="faq-question">How is this different from JSONPath?</summary>
            <div class="faq-answer">
                <p>This tool uses <strong>simplified path notation</strong> (like <code>name</code>, <code>address.city</code>) which is easier to type.</p>
                <p>Full JSONPath supports complex filters like <code>$[?(@.price > 100)]</code> - this tool focuses on common use cases.</p>
            </div>
        </details>'''

content = content.replace(old_xpath_faq, new_xpath_faq)

# Fix 8: Section header
content = content.replace(
    '<h2 class="section-label" style="font-size: 1.125rem; margin-bottom: 1rem;">JSONPath Syntax Guide - How to Extract JSON Data</h2>',
    '<h2 class="section-label" style="font-size: 1.125rem; margin-bottom: 1rem;">Path Syntax Guide - How to Extract JSON Data</h2>'
)

# Fix 9: Placeholder text - remove JSONPath claim
content = content.replace(
    "Enter JSONPath, for example: $.name or $.address.city or $.skills[0]",
    "Enter path, for example: name or address.city or skills[0]"
)

# Fix 10: JSON-LD featureList
content = content.replace(
    '"featureList": ["JSON data extraction", "JSONPath queries", "Nested data access", "Array indexing", "Real-time preview", "Copy results"]',
    '"featureList": ["JSON data extraction", "Simple path queries", "Nested data access", "Array indexing", "Real-time preview", "Copy results"]'
)

with open(extract_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("extract.html fixed - removed false JSONPath claims")
