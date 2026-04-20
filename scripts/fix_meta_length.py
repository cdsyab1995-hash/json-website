# -*- coding: utf-8 -*-
"""Fix meta descriptions that are too long (>160 chars) or too short (<120)"""
import re
from pathlib import Path

PROJECT_ROOT = Path(r'd:\网站开发-json')

# Optimized descriptions (120-160 chars)
FIXES = {
    'index.html': 'Format, validate, and debug JSON instantly. Extract data with dot paths, convert to CSV/Excel, compare versions. Client-side, 100% private.',
    'base64.html': 'Free Base64 encoder and decoder. Encode text to Base64 or decode Base64 to text. Instant, client-side processing. No uploads.',
    'best-practices.html': 'JSON best practices for developers. Learn naming conventions, structure design, validation patterns, and common pitfalls.',
    'clean.html': 'Repair and clean JSON instantly. Remove nulls, fix trailing commas, deduplicate keys. Real-time preview. No signup required.',
    'compare.html': 'Compare JSON documents side-by-side with color-coded diff. Instant visual comparison. Highlight additions, deletions, and changes.',
    'css-minifier.html': 'Free CSS and JavaScript minifier/compressor. Reduce file size by removing whitespace and comments. Instant download.',
    'escape.html': 'Escape and unescape JSON strings instantly. Handle special characters, newlines, and quotes. Real-time preview. No signup.',
    'extract.html': 'Extract JSON data with dot notation paths. Access nested objects, arrays, and properties. Real-time preview. No code required.',
    'format.html': 'Format and validate JSON instantly. Syntax highlighting, error detection, and minify. Real-time preview. No signup required.',
    'html-encoder.html': 'Free HTML encoder and decoder. Convert special characters to HTML entities and back. Instant, client-side processing.',
    'json2csv.html': 'Convert JSON to CSV and Excel instantly. Flatten nested JSON, export arrays. No signup. Client-side only, 100% private.',
    'news.html': 'Developer trending news. Daily API trends, JSON tools updates, and web development insights. Updated regularly.',
    'sort.html': 'Sort JSON keys alphabetically in seconds. Recursive key sorting, ascending/descending order. Real-time preview. No signup.',
    'timestamp-converter.html': 'Free Unix timestamp converter. Convert between Unix timestamp, ISO 8601, and human-readable dates. Instant results.',
    'url-encoder.html': 'Free URL encoder and decoder. Encode special characters for URLs or decode URL-encoded strings. Instant, client-side.',
    'viewer.html': 'Visualize JSON in a tree view. Navigate complex structures, search keys/values. Real-time preview. No signup required.',
    'xml.html': 'Convert JSON to XML and XML to JSON instantly. Bidirectional conversion with syntax validation. Real-time preview. No signup.',
    'yaml.html': 'Convert JSON to YAML and YAML to JSON instantly. Bidirectional conversion with syntax validation. Real-time preview. No signup.',
    'jwt-decoder.html': 'Free JWT decoder. Decode and inspect JSON Web Tokens. View header, payload, and signature. No signup required.',
}

for html_file in sorted(PROJECT_ROOT.rglob('*.html')):
    try:
        content = html_file.read_text(encoding='utf-8')
    except:
        continue

    name = html_file.name
    if name not in FIXES:
        continue

    new_desc = FIXES[name]

    # Replace meta description
    pattern = r'<meta name="description" content="[^"]+">'
    replacement = f'<meta name="description" content="{new_desc}">'

    new_content, count = re.subn(pattern, replacement, content)
    if count > 0:
        html_file.write_text(new_content, encoding='utf-8')
        print(f'[FIX] {name}: {len(new_desc)} chars')
    else:
        print(f'[WARN] {name}: no description found')

print('\nDone!')
