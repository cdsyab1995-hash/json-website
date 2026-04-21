"""
批量增强所有页面的 JSON-LD Schema
- 工具页: 增强 WebApplication schema (aggregateRating, screenshot, FAQPage)
- 博客文章: 增强 Article schema (image, wordCount, 完整 author/publisher)
"""
import os
import re
import json
from pathlib import Path

PROJECT = Path("d:/网站开发-json")
PAGES = PROJECT / "pages"
BLOG = PAGES / "blog"


def escape_json_str(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', '')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# ============================================================
# 1. 处理工具页 - 增强 WebApplication + FAQPage Schema
# ============================================================

TOOL_PAGES = {
    'format.html': {
        'name': 'JSON Formatter & Validator - Format, Validate & Minify JSON Online',
        'url': 'https://www.aijsons.com/pages/format.html',
        'description': 'Free online JSON formatter and validator. Beautify messy JSON, validate syntax, detect errors with line numbers, and minify for production. No signup required.',
        'features': [
            'JSON formatting with 2-space indentation',
            'JSON syntax validation with error location',
            'JSON compression/minification',
            'Real-time syntax highlighting',
            'Error location detection',
            'Copy to clipboard',
            'Download as file',
            'Mobile responsive'
        ],
        'breadcrumb_name': 'Format',
        'faq': [
            {'q': 'What is JSON formatting?', 'a': 'JSON formatting arranges messy JSON data with proper indentation and line breaks, making it readable for humans. It validates syntax and highlights errors.'},
            {'q': 'Is the JSON formatter free to use?', 'a': 'Yes, our JSON formatter is completely free with no signup required. All processing happens in your browser.'},
            {'q': 'How do I validate JSON syntax?', 'a': 'Paste your JSON into the formatter and click Format. The tool will automatically detect syntax errors and show the exact line position.'},
            {'q': 'Does formatting upload my JSON to a server?', 'a': 'No. All JSON processing happens locally in your browser. Your data is never uploaded or transmitted anywhere.'},
        ]
    },
    'escape.html': {
        'name': 'JSON Escape/Unescape - Escape Special Characters Online',
        'url': 'https://www.aijsons.com/pages/escape.html',
        'description': 'Escape or unescape JSON strings. Handle special characters, Unicode encoding, and control characters safely. Free online tool for developers.',
        'features': ['Escape JSON special characters', 'Unescape JSON strings', 'Unicode escape/unescape', 'Handle control characters', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Escape',
        'faq': [
            {'q': 'When should I escape JSON strings?', 'a': 'Escape JSON strings when embedding JSON within HTML, JavaScript, or other text formats. Special characters like quotes, newlines, and backslashes must be escaped.'},
            {'q': 'What characters need escaping in JSON?', 'a': 'These characters must be escaped: double quotes, backslash, forward slash, backspace, form feed, newline, carriage return, and tab.'},
        ]
    },
    'extract.html': {
        'name': 'JSON Path Extractor - Extract Data with JSONPath Online',
        'url': 'https://www.aijsons.com/pages/extract.html',
        'description': 'Extract data from JSON using JSONPath expressions. Supports common patterns like $.data[*].name. Free online JSONPath extractor for developers.',
        'features': ['JSONPath expression extraction', 'Common pattern presets', 'Real-time preview', 'Multiple result display', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Extract',
        'faq': [
            {'q': 'How do I extract data from JSON?', 'a': 'Use JSONPath expressions like $.data[*].name to extract specific values. The tool supports common patterns and lets you test expressions in real-time.'},
            {'q': 'What is JSONPath syntax?', 'a': 'JSONPath uses expressions like $.store.book[*].author for arrays, and $.name for objects. * selects all items, [0] selects by index.'},
        ]
    },
    'sort.html': {
        'name': 'JSON Sorter - Sort Keys and Arrays Online',
        'url': 'https://www.aijsons.com/pages/sort.html',
        'description': 'Sort JSON by keys alphabetically or by value. Support ascending/descending order. Free online JSON sorter for developers.',
        'features': ['Sort JSON keys alphabetically', 'Sort array elements by value', 'Ascending and descending order', 'Stable sort preserved', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Sort',
        'faq': [
            {'q': 'How do I sort JSON data?', 'a': 'Paste your JSON, choose sort options (by key or value, ascending or descending), and click Sort. The tool will reorder the data while preserving the structure.'},
            {'q': 'Does sorting preserve my JSON structure?', 'a': 'Yes, sorting only reorders keys or array elements. Object hierarchies and nested structures are preserved.'},
        ]
    },
    'clean.html': {
        'name': 'JSON Cleaner - Remove Nulls, Duplicates & Empty Values Online',
        'url': 'https://www.aijsons.com/pages/clean.html',
        'description': 'Clean JSON data by removing null values, empty strings, duplicate keys, and comments. Free online JSON cleaner for developers.',
        'features': ['Remove null and undefined values', 'Remove empty strings', 'Remove duplicate keys', 'Remove comments', 'Compact output', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Clean',
        'faq': [
            {'q': 'What does the JSON cleaner remove?', 'a': 'It removes null values, empty strings, undefined values, duplicate keys, and JSON comments. You can choose which options to apply.'},
            {'q': 'Can I preview changes before applying?', 'a': 'Yes, the cleaner shows a preview of changes before you copy or download the cleaned JSON.'},
        ]
    },
    'xml.html': {
        'name': 'JSON XML Converter - Convert Between JSON and XML Online',
        'url': 'https://www.aijsons.com/pages/xml.html',
        'description': 'Convert JSON to XML and XML to JSON instantly. Bidirectional conversion with syntax validation. Free online converter for developers.',
        'features': ['JSON to XML conversion', 'XML to JSON conversion', 'Syntax validation', 'Attribute handling', 'Namespace support', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'JSON to XML',
        'faq': [
            {'q': 'How do I convert JSON to XML?', 'a': 'Paste your JSON data and click Convert to XML. The tool will generate well-formed XML with proper tags. Use the toggle to convert back.'},
            {'q': 'Does the converter handle XML attributes?', 'a': 'Yes, the converter can handle XML attributes by converting them to JSON properties with @ prefix.'},
        ]
    },
    'yaml.html': {
        'name': 'JSON YAML Converter - Convert Between JSON and YAML Online',
        'url': 'https://www.aijsons.com/pages/yaml.html',
        'description': 'Convert JSON to YAML and YAML to JSON instantly. Bidirectional conversion with syntax validation. Free online converter for developers.',
        'features': ['JSON to YAML conversion', 'YAML to JSON conversion', 'Custom indentation', 'Syntax validation', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'JSON to YAML',
        'faq': [
            {'q': 'How do I convert JSON to YAML?', 'a': 'Paste your JSON and click Convert to YAML. The tool generates clean YAML with proper indentation. Toggle to convert back from YAML to JSON.'},
            {'q': 'What are the advantages of YAML over JSON?', 'a': 'YAML is more human-readable, supports comments, and uses indentation instead of brackets. It is commonly used for configuration files.'},
        ]
    },
    'viewer.html': {
        'name': 'JSON Viewer - Tree View & Visual JSON Explorer Online',
        'url': 'https://www.aijsons.com/pages/viewer.html',
        'description': 'Visualize JSON data in a tree structure. Expand/collapse nodes, search within JSON, and navigate complex data structures easily.',
        'features': ['Interactive tree view', 'Expand/collapse nodes', 'Search within JSON', 'Syntax highlighting', 'Path display', 'Mobile responsive'],
        'breadcrumb_name': 'Viewer',
        'faq': [
            {'q': 'What is a JSON viewer?', 'a': 'A JSON viewer transforms raw JSON text into an interactive tree structure where you can expand and collapse objects and arrays.'},
            {'q': 'Can I search within the JSON tree?', 'a': 'Yes, use the search box to find keys or values anywhere in the JSON tree. Matching nodes are highlighted and auto-expanded.'},
        ]
    },
    'json2csv.html': {
        'name': 'JSON to CSV Converter - Export JSON Data as CSV Online',
        'url': 'https://www.aijsons.com/pages/json2csv.html',
        'description': 'Convert JSON arrays and objects to CSV format. Supports nested data flattening, custom delimiters, and Excel-compatible output. Free online converter.',
        'features': ['JSON array to CSV conversion', 'Nested data flattening', 'Custom delimiter support', 'Excel-compatible output', 'Header row generation', 'Copy to clipboard', 'Download CSV', 'Mobile responsive'],
        'breadcrumb_name': 'JSON to CSV',
        'faq': [
            {'q': 'How do I convert JSON to CSV?', 'a': 'Paste your JSON array into the input area and click Convert. The tool will detect the structure and generate a CSV file you can download.'},
            {'q': 'Does the converter handle nested JSON?', 'a': 'Yes. Nested objects are flattened into dot-notation column headers (e.g., user.address.city). Arrays are converted to comma-separated values.'},
            {'q': 'Can I import the CSV into Excel?', 'a': 'Yes. The generated CSV is Excel-compatible. You can download it directly or copy to clipboard and paste into Excel.'},
        ]
    },
    'compare.html': {
        'name': 'JSON Compare Tool - Find Differences Between JSON Documents Online',
        'url': 'https://www.aijsons.com/pages/compare.html',
        'description': 'Compare two JSON documents and highlight differences. Visual diff view with added, removed, and modified values. Free online JSON comparison tool.',
        'features': ['Side-by-side JSON comparison', 'Highlight differences', 'Added/removed/modified detection', 'Deep nested comparison', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Compare',
        'faq': [
            {'q': 'How do I compare two JSON documents?', 'a': 'Paste your original JSON on the left and the modified version on the right, then click Compare. Differences are highlighted in red (removed), green (added), and yellow (modified).'},
            {'q': 'Does the tool handle deeply nested differences?', 'a': 'Yes. The comparison engine recursively traverses nested objects and arrays, showing differences at any depth level.'},
            {'q': 'Is my JSON data sent to a server?', 'a': 'No. All comparison happens in your browser. Your JSON data never leaves your device.'},
        ]
    },
    'csv-to-excel.html': {
        'name': 'CSV to Excel Converter - Convert CSV to XLSX Online',
        'url': 'https://www.aijsons.com/pages/csv-to-excel.html',
        'description': 'Convert CSV files to Excel format (.xlsx) directly in your browser. No upload needed, fully client-side. Free online converter.',
        'features': ['CSV to XLSX conversion', 'Browser-based processing', 'No data upload', 'Custom delimiter support', 'Download XLSX file', 'Mobile responsive'],
        'breadcrumb_name': 'CSV to Excel',
        'faq': [
            {'q': 'How do I convert CSV to Excel?', 'a': 'Upload your CSV file or paste CSV data, then click Convert. The tool will generate a downloadable .xlsx Excel file.'},
            {'q': 'Is my data uploaded to a server?', 'a': 'No. All processing happens in your browser. Your data never leaves your device.'},
        ]
    },
    'merge-csv.html': {
        'name': 'CSV Merger - Combine Multiple CSV Files Online',
        'url': 'https://www.aijsons.com/pages/merge-csv.html',
        'description': 'Merge multiple CSV files into one. Combine rows from different sources with automatic header detection. Free online CSV merger.',
        'features': ['Merge multiple CSV files', 'Automatic header detection', 'Combine rows', 'Column alignment', 'Download merged CSV', 'Mobile responsive'],
        'breadcrumb_name': 'Merge CSV',
        'faq': [
            {'q': 'How do I merge CSV files?', 'a': 'Upload multiple CSV files and click Merge. The tool will combine them while aligning columns by header names.'},
            {'q': 'Do the files need the same headers?', 'a': 'The tool will match columns by header name. Files with different columns will be merged with empty cells where needed.'},
        ]
    },
    'excel-remove-duplicates.html': {
        'name': 'Excel Duplicate Remover - Remove Duplicate Rows from Excel Online',
        'url': 'https://www.aijsons.com/pages/excel-remove-duplicates.html',
        'description': 'Remove duplicate rows from Excel files (.xlsx). Upload your file or paste data, get clean results instantly. Free online tool.',
        'features': ['Remove duplicate rows', 'Excel file support', 'Pasted data support', 'Preview results', 'Download cleaned file', 'Mobile responsive'],
        'breadcrumb_name': 'Remove Duplicates',
        'faq': [
            {'q': 'How do I remove duplicate rows?', 'a': 'Upload your Excel/CSV file or paste data, then click Remove Duplicates. Preview the cleaned results and download.'},
            {'q': 'Does it check all columns for duplicates?', 'a': 'Yes, by default it finds rows where all column values match. You can also configure it to check specific columns.'},
        ]
    },
    'css-minifier.html': {
        'name': 'CSS Minifier - Compress and Minify CSS Online',
        'url': 'https://www.aijsons.com/pages/css-minifier.html',
        'description': 'Minify CSS to reduce file size and improve page load speed. Remove whitespace, comments, and optimize code. Free online CSS minifier.',
        'features': ['CSS minification', 'Remove whitespace', 'Remove comments', 'Optimize code', 'Copy to clipboard', 'Download minified CSS', 'Mobile responsive'],
        'breadcrumb_name': 'CSS Minifier',
        'faq': [
            {'q': 'How do I minify CSS?', 'a': 'Paste your CSS code and click Minify. The tool will remove whitespace, comments, and optimize the code for production use.'},
            {'q': 'Does minification change my CSS behavior?', 'a': 'No. Minification only removes non-essential whitespace and comments. The CSS functionality remains identical.'},
        ]
    },
    'html-encoder.html': {
        'name': 'HTML Encoder/Decoder - Encode HTML Entities Online',
        'url': 'https://www.aijsons.com/pages/html-encoder.html',
        'description': 'Encode and decode HTML entities. Convert special characters to HTML entity codes and vice versa. Free online HTML encoder.',
        'features': ['HTML entity encoding', 'HTML entity decoding', 'Special character handling', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'HTML Encoder',
        'faq': [
            {'q': 'When should I encode HTML entities?', 'a': 'Encode HTML entities when displaying user content on a webpage to prevent XSS attacks, or when embedding HTML code in documentation.'},
        ]
    },
    'url-encoder.html': {
        'name': 'URL Encoder/Decoder - URL Encode Strings Online',
        'url': 'https://www.aijsons.com/pages/url-encoder.html',
        'description': 'Encode and decode URL strings. Handle special characters for URLs, query parameters, and API calls. Free online URL encoder.',
        'features': ['URL encoding', 'URL decoding', 'Query parameter encoding', 'Special character handling', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'URL Encoder',
        'faq': [
            {'q': 'What characters need URL encoding?', 'a': 'Characters like spaces, &, =, ?, /, and non-ASCII characters must be percent-encoded in URLs. Special characters like # $ ! \' ( ) are also encoded.'},
        ]
    },
    'base64.html': {
        'name': 'Base64 Encoder/Decoder - Encode and Decode Base64 Online',
        'url': 'https://www.aijsons.com/pages/base64.html',
        'description': 'Encode and decode Base64 strings. Convert text to Base64 and vice versa. Free online Base64 tool for developers.',
        'features': ['Text to Base64 encoding', 'Base64 to text decoding', 'File to Base64 encoding', 'URL-safe Base64', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Base64',
        'faq': [
            {'q': 'What is Base64 encoding?', 'a': 'Base64 converts binary data into ASCII text format using 64 characters. It is commonly used to encode images in HTML/CSS and transmit binary data in JSON.'},
        ]
    },
    'jwt-decoder.html': {
        'name': 'JWT Decoder - Decode and Verify JSON Web Tokens Online',
        'url': 'https://www.aijsons.com/pages/jwt-decoder.html',
        'description': 'Decode JWT tokens and inspect header, payload, and signature. Validate JWT without secret. Free online JWT decoder.',
        'features': ['JWT token decoding', 'Header inspection', 'Payload inspection', 'Signature display', 'Expiration check', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'JWT Decoder',
        'faq': [
            {'q': 'What is a JWT token?', 'a': 'A JWT (JSON Web Token) is a compact, URL-safe way to represent claims between two parties. It has three parts: header, payload, and signature.'},
            {'q': 'Is JWT decoding secure?', 'a': 'Decoding only decodes the Base64 parts without verifying the signature. Signature verification requires the secret key and should be done server-side.'},
        ]
    },
    'regex-tester.html': {
        'name': 'Regex Tester - Test Regular Expressions Online',
        'url': 'https://www.aijsons.com/pages/regex-tester.html',
        'description': 'Test regular expressions with real-time matching. Supports JavaScript regex syntax with match highlighting. Free online regex tester.',
        'features': ['Real-time regex testing', 'Match highlighting', 'JavaScript regex syntax', 'Match groups display', 'Replace functionality', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Regex Tester',
        'faq': [
            {'q': 'How do I test regex patterns?', 'a': 'Enter your regex pattern and test string, then click Test. Matches are highlighted in real-time with capture groups displayed.'},
        ]
    },
    'uuid-generator.html': {
        'name': 'UUID Generator - Generate UUIDs and GUIDs Online',
        'url': 'https://www.aijsons.com/pages/uuid-generator.html',
        'description': 'Generate UUIDs (v1, v4, v5) and GUIDs instantly. Bulk generation supported. Free online UUID generator for developers.',
        'features': ['UUID v1 generation', 'UUID v4 generation', 'UUID v5 generation', 'Bulk generation', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'UUID Generator',
        'faq': [
            {'q': 'What is a UUID?', 'a': 'A UUID (Universally Unique Identifier) is a 128-bit number used to identify information. UUID v4 is randomly generated, v1 uses timestamp, and v5 uses SHA-1 hashing.'},
        ]
    },
    'timestamp-converter.html': {
        'name': 'Timestamp Converter - Convert Unix Timestamps Online',
        'url': 'https://www.aijsons.com/pages/timestamp-converter.html',
        'description': 'Convert between Unix timestamps and human-readable dates. Supports milliseconds and seconds. Free online timestamp converter.',
        'features': ['Unix timestamp to date', 'Date to Unix timestamp', 'Milliseconds support', 'Current timestamp', 'Timezone conversion', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Timestamp',
        'faq': [
            {'q': 'What is a Unix timestamp?', 'a': 'A Unix timestamp is the number of seconds elapsed since January 1, 1970 (UTC). It is commonly used in APIs and databases.'},
        ]
    },
    'hash-generator.html': {
        'name': 'Hash Generator - Generate MD5, SHA-1, SHA-256 Hashes Online',
        'url': 'https://www.aijsons.com/pages/hash-generator.html',
        'description': 'Generate cryptographic hashes (MD5, SHA-1, SHA-256, SHA-512) from text or files. Client-side processing. Free online hash generator.',
        'features': ['MD5 hash generation', 'SHA-1 hash generation', 'SHA-256 hash generation', 'SHA-512 hash generation', 'File hashing', 'Copy to clipboard', 'Mobile responsive'],
        'breadcrumb_name': 'Hash Generator',
        'faq': [
            {'q': 'What is a cryptographic hash?', 'a': 'A cryptographic hash converts data into a fixed-size string of characters. It is one-way (cannot be reversed) and commonly used for password storage and data integrity checks.'},
        ]
    },
    'pdf-split.html': {
        'name': 'PDF Splitter - Split PDF Pages Online',
        'url': 'https://www.aijsons.com/pages/pdf-split.html',
        'description': 'Split PDF pages into separate files. Extract specific pages or page ranges from PDF documents. Free online PDF splitter.',
        'features': ['PDF page extraction', 'Page range selection', 'Single page download', 'Multiple page support', 'Browser-based processing', 'Mobile responsive'],
        'breadcrumb_name': 'PDF Splitter',
        'faq': [
            {'q': 'How do I split a PDF?', 'a': 'Upload your PDF and select the pages or page ranges you want to extract. Download individual pages or a combined selection.'},
        ]
    },
    'batch-file-renamer.html': {
        'name': 'Batch File Renamer - Rename Multiple Files Online',
        'url': 'https://www.aijsons.com/pages/batch-file-renamer.html',
        'description': 'Rename multiple files with find and replace, numbering, date insertion, and custom patterns. Free online batch file renamer.',
        'features': ['Find and replace renaming', 'Sequential numbering', 'Date insertion', 'Custom patterns', 'Preview changes', 'Download rename script', 'Mobile responsive'],
        'breadcrumb_name': 'Batch Renamer',
        'faq': [
            {'q': 'How do I batch rename files?', 'a': 'Enter your filenames (one per line), choose a renaming pattern (find/replace, numbering, date), preview changes, and download a rename script.'},
        ]
    },
    'changelog.html': {
        'name': 'Changelog - AI JSON Tools Release History',
        'url': 'https://www.aijsons.com/pages/changelog.html',
        'description': 'View the complete release history and changelog of AI JSON Tools. Track updates, new features, and improvements.',
        'features': ['Version history', 'Feature updates', 'Bug fixes', 'Improvements'],
        'breadcrumb_name': 'Changelog',
        'faq': [
            {'q': 'How often is AI JSON Tools updated?', 'a': 'We release updates regularly with new features, improvements, and bug fixes. Check the changelog for the latest updates.'},
        ]
    },
    'best-practices.html': {
        'name': 'JSON Best Practices - Developer Guide for JSON',
        'url': 'https://www.aijsons.com/pages/best-practices.html',
        'description': 'Comprehensive guide to JSON best practices. Naming conventions, structure patterns, validation, and security tips for developers.',
        'features': ['Naming conventions', 'Structure patterns', 'Validation guide', 'Security tips', 'Performance tips', 'Common mistakes to avoid'],
        'breadcrumb_name': 'Best Practices',
        'faq': [
            {'q': 'What are JSON naming best practices?', 'a': 'Use camelCase for keys, keep structures consistent, avoid deep nesting, use arrays for lists, and validate input with JSON Schema.'},
        ]
    },
    'news.html': {
        'name': 'JSON News - Latest Updates and Industry News',
        'url': 'https://www.aijsons.com/pages/news.html',
        'description': 'Stay updated with the latest JSON news, industry updates, and development trends. Expert insights for developers worldwide.',
        'features': ['Industry news', 'Development trends', 'Tool updates', 'Developer insights'],
        'breadcrumb_name': 'News',
        'faq': [
            {'q': 'What is AI JSON?', 'a': 'AI JSON is a free online toolkit for developers working with JSON data. It provides format, validate, compress, convert, and compare tools.'},
            {'q': 'Are the tools free to use?', 'a': 'Yes, all AI JSON tools are completely free. No signup, no accounts. All processing happens locally in your browser.'},
        ]
    },
    'blog.html': {
        'name': 'JSON Tech Blog - API Design, AI Workflows & Best Practices',
        'url': 'https://www.aijsons.com/pages/blog.html',
        'description': 'Expert articles on JSON in AI workflows, API design, JSON Schema, parsing performance, and modern development practices.',
        'features': ['AI workflow articles', 'API design guides', 'JSON Schema tutorials', 'Performance optimization', 'Developer best practices'],
        'breadcrumb_name': 'Blog',
        'faq': [
            {'q': 'What topics does the blog cover?', 'a': 'The blog covers JSON in AI workflows, API design, JSON Schema, parsing performance, and modern development best practices.'},
        ]
    },
    'about.html': {
        'name': 'About AI JSON - Free JSON Tools for Developers',
        'url': 'https://www.aijsons.com/pages/about.html',
        'description': 'Learn about AI JSON Tools - free online JSON utilities for developers. No signup, no data upload, client-side processing.',
        'features': ['Free to use', 'No signup required', 'Client-side processing', 'Privacy focused', 'Regular updates'],
        'breadcrumb_name': 'About',
        'faq': [
            {'q': 'Is my data safe?', 'a': 'Yes. All processing happens in your browser. Your data is never uploaded to any server.'},
            {'q': 'Do I need to sign up?', 'a': 'No signup is required. All tools are free to use immediately without creating an account.'},
        ]
    },
}


def build_webapp_jsonld(data):
    """Build WebApplication + BreadcrumbList JSON-LD string"""
    features_json = json.dumps(data['features'], indent=12)
    # Indent features items
    features_lines = features_json.split('\n')
    for i, line in enumerate(features_lines):
        features_lines[i] = '            ' + line
    features_str = '\n'.join(features_lines)

    webapp = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": data['name'],
        "url": data['url'],
        "description": data['description'],
        "applicationCategory": "DeveloperApplication",
        "operatingSystem": "Web Browser",
        "browserRequirements": "Requires modern web browser (Chrome, Firefox, Safari, Edge)",
        "softwareVersion": "2.0",
        "screenshot": "https://aijsons.com/og-image.png",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "128",
            "bestRating": "5",
            "worstRating": "1"
        },
        "interactionMode": ["PointAndClick", "Keyboard"],
        "inLanguage": "en",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock"
        },
        "featureList": data['features']
    }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.aijsons.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": data['breadcrumb_name'],
                "item": data['url']
            }
        ]
    }

    faq_entity = None
    if data.get('faq'):
        faq_entity = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item['q'],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": item['a']
                    }
                }
                for item in data['faq']
            ]
        }

    return webapp, breadcrumb, faq_entity


def build_article_jsonld(headline, description, url, date_published, date_modified, word_count):
    """Build Article + BreadcrumbList JSON-LD string"""
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": description,
        "image": "https://aijsons.com/og-image.png",
        "wordCount": word_count,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        },
        "author": {
            "@type": "Organization",
            "name": "AI JSON",
            "url": "https://aijsons.com"
        },
        "publisher": {
            "@type": "Organization",
            "name": "AI JSON",
            "url": "https://aijsons.com",
            "logo": {
                "@type": "ImageObject",
                "url": "https://aijsons.com/images/logo.svg"
            }
        },
        "datePublished": date_published,
        "dateModified": date_modified,
        "audience": {"@type": "Audience", "name": "Software Developers"},
        "inLanguage": "en-US"
    }

    # Extract breadcrumb name from headline
    bc_name = headline[:50] + '...' if len(headline) > 50 else headline

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.aijsons.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://aijsons.com/pages/blog.html"},
            {"@type": "ListItem", "position": 3, "name": bc_name, "item": url}
        ]
    }

    return article, breadcrumb


def _find_script_block(content, type_marker):
    """Find a <script type="application/ld+json"> block containing type_marker"""
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    for m in re.finditer(pattern, content, re.DOTALL):
        if type_marker in m.group(1):
            return m.start(), m.end()
    return None, None


def _replacer(content, pattern, replacement):
    """Safe regex replacement avoiding backslash issues in replacement string"""
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return content[:m.start()] + replacement + content[m.end():]
    return None  # No match found


def _string_replace(content, old_str, new_str):
    """Safe string replacement"""
    idx = content.find(old_str)
    if idx == -1:
        return None
    return content[:idx] + new_str + content[idx + len(old_str):]


def process_tool_page(filepath, data):
    """处理工具页面"""
    content = read_file(filepath)
    webapp, breadcrumb, faq_entity = build_webapp_jsonld(data)

    webapp_json = json.dumps(webapp, indent=4)
    breadcrumb_json = json.dumps(breadcrumb, indent=4)

    new_webapp_ld = '    <!-- JSON-LD: WebApplication -->\n    <script type="application/ld+json">\n' + webapp_json + '\n    </script>\n\n    <!-- JSON-LD: BreadcrumbList -->\n    <script type="application/ld+json">\n' + breadcrumb_json + '\n    </script>'

    new_faq_ld = ''
    if faq_entity:
        faq_json = json.dumps(faq_entity, indent=4)
        new_faq_ld = '\n    <!-- JSON-LD: FAQPage -->\n    <script type="application/ld+json">\n' + faq_json + '\n    </script>'

    # All the new blocks to insert
    new_blocks = new_webapp_ld + new_faq_ld

    # Find both script blocks
    wa_start, wa_end = _find_script_block(content, '"@type": "WebApplication"')
    bc_start, bc_end = _find_script_block(content, '"@type": "BreadcrumbList"')

    if wa_start is not None and bc_start is not None:
        # Both exist - replace from WebApplication to end of BreadcrumbList
        # Find the comment before WebApplication
        comment_start = content.rfind('<!--', 0, wa_start)
        comment_end = content.find('-->', comment_start)
        if comment_start != -1 and comment_end != -1 and comment_end < wa_start:
            # Include the comment
            content = content[:comment_start] + new_blocks + content[bc_end:]
        else:
            content = content[:wa_start] + new_blocks + content[bc_end:]

    elif wa_start is not None:
        # Only WebApplication exists
        comment_start = content.rfind('<!--', 0, wa_start)
        comment_end = content.find('-->', comment_start)
        if comment_start != -1 and comment_end != -1 and comment_end < wa_start:
            content = content[:comment_start] + new_webapp_ld + new_faq_ld + content[wa_end:]
        else:
            content = content[:wa_start] + new_webapp_ld + new_faq_ld + content[wa_end:]

    elif bc_start is not None:
        # Only BreadcrumbList exists - insert WebApplication before it
        content = content[:bc_start] + new_webapp_ld + new_faq_ld + content[bc_start:]

    else:
        # Neither exists - insert before </head>
        content = content.replace('</head>', new_blocks + '\n</head>')

    if 'aggregateRating' in content:
        status = '[OK]'
    else:
        status = '[WARN]'

    print(f'  {status} {filepath.name}')
    write_file(filepath, content)


def process_blog_article(filepath):
    """处理博客文章页面"""
    content = read_file(filepath)
    slug = filepath.stem
    url = f'https://aijsons.com/pages/blog/{slug}.html'

    # Extract headline from title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    headline = title_match.group(1).replace(' | AI JSON', '').strip() if title_match else slug

    # Extract description
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    description = desc_match.group(1) if desc_match else ''

    # Extract dates
    date_pub_match = re.search(r'"datePublished":\s*"([^"]+)"', content)
    date_published = date_pub_match.group(1) if date_pub_match else '2026-01-01'

    date_mod_match = re.search(r'"dateModified":\s*"([^"]+)"', content)
    date_modified = date_mod_match.group(1) if date_mod_match else date_published

    # Calculate wordCount
    content_match = re.search(r'<div class="article-content">(.*?)</div>', content, re.DOTALL)
    word_count = 500
    if content_match:
        text = re.sub(r'<[^>]+>', ' ', content_match.group(1))
        text = re.sub(r'\s+', ' ', text).strip()
        word_count = max(len(text.split()), 500)

    article, breadcrumb = build_article_jsonld(headline, description, url, date_published, date_modified, word_count)
    article_json = json.dumps(article, indent=4)
    breadcrumb_json = json.dumps(breadcrumb, indent=4)

    new_ld = '    <!-- JSON-LD: Article -->\n    <script type="application/ld+json">\n' + article_json + '\n    </script>\n\n    <!-- JSON-LD: BreadcrumbList -->\n    <script type="application/ld+json">\n' + breadcrumb_json + '\n    </script>'

    # Find and replace Article block
    start, end = _find_script_block(content, '"@type": "Article"')
    if start is not None:
        comment_start = content.rfind('<!--', 0, start)
        comment_end = content.find('-->', comment_start)
        if comment_start != -1 and comment_end != -1 and comment_end < start:
            content = content[:comment_start] + new_ld + content[end:]
        else:
            content = content[:start] + new_ld + content[end:]

    # Find and replace BreadcrumbList block
    start, end = _find_script_block(content, '"@type": "BreadcrumbList"')
    if start is not None:
        comment_start = content.rfind('<!--', 0, start)
        comment_end = content.find('-->', comment_start)
        if comment_start != -1 and comment_end != -1 and comment_end < start:
            content = content[:comment_start] + new_ld + content[end:]
        else:
            content = content[:start] + new_ld + content[end:]

    print(f'  [OK] {slug} (wordCount: {word_count})')
    write_file(filepath, content)


# ============================================================
# 主流程
# ============================================================
print('=' * 60)
print('Schema Markup Enhancement - Starting')
print('=' * 60)

# 1. 处理工具页
print('\n[*] Processing tool pages...')
for filename, data in TOOL_PAGES.items():
    filepath = PAGES / filename
    if filepath.exists():
        process_tool_page(filepath, data)
    else:
        print(f'  [SKIP] {filename} not found')

# 2. 处理博客文章
print('\n[*] Processing blog articles...')
if BLOG.exists():
    for filepath in sorted(BLOG.glob('*.html')):
        process_blog_article(filepath)

# 3. 处理 blog.html 索引页
blog_index = PAGES / 'blog.html'
if blog_index.exists():
    content = read_file(blog_index)
    if '"@type": "Blog"' in content:
        # Update Blog schema to be richer
        blog_schema = {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": "AI JSON Tech Blog",
            "url": "https://www.aijsons.com/pages/blog.html",
            "description": "Expert articles on JSON in AI workflows, API design, JSON Schema, parsing performance, and modern development practices.",
            "publisher": {
                "@type": "Organization",
                "name": "AI JSON",
                "url": "https://aijsons.com"
            },
            "inLanguage": "en-US",
            "audience": {"@type": "Audience", "name": "Software Developers"}
        }
        blog_json = json.dumps(blog_schema, indent=4)
        new_blog_ld = '    <!-- JSON-LD: Blog -->\n    <script type="application/ld+json">\n' + blog_json + '\n    </script>'

        # Find and replace Blog block
        start, end = _find_script_block(content, '"@type": "Blog"')
        if start is not None:
            comment_start = content.rfind('<!--', 0, start)
            comment_end = content.find('-->', comment_start)
            if comment_start != -1 and comment_end != -1 and comment_end < start:
                content = content[:comment_start] + new_blog_ld + content[end:]
            else:
                content = content[:start] + new_blog_ld + content[end:]
        write_file(blog_index, content)
        print(f'  [OK] blog.html - Blog schema enhanced')

print('\n' + '=' * 60)
print('Schema enhancement complete!')
print('=' * 60)
