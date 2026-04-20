# -*- coding: utf-8 -*-
"""
Tool-Focused Blog Automation Script
Generates articles that directly serve JSON tool pages.
Each article targets a specific tool and uses SEO-friendly content models:
- Problem keywords (why, fix, common mistakes)
- Comparison keywords (JSON vs YAML, JSON vs XML, etc.)
- Scenario keywords (API testing, debugging, production)
- Tutorial keywords (how to extract, how to clean, how to validate)
"""
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

# ============================================================================
# TOOL MAPPING - Maps article themes to tool pages
# ============================================================================
TOOL_MAPPING = {
    'format': '../format.html',
    'clean': '../clean.html',
    'viewer': '../viewer.html',
    'extract': '../extract.html',
    'sort': '../sort.html',
    'compare': '../compare.html',
    'escape': '../escape.html',
    'json2csv': '../json2csv.html',
    'yaml': '../yaml.html',
    'xml': '../xml.html',
}

# ============================================================================
# BLOG TOPICS - Each serves a specific tool page
# ============================================================================
TOOL_BLOG_TOPICS = [
    # ===== FORMAT TOOL ARTICLES =====
    {
        "tool": "format",
        "slug": "why-is-my-json-invalid-common-errors",
        "category": "Debugging",
        "cat_class": "cat-debugging",
        "read_time": "5-7 min read",
        "title": "Why Is My JSON Invalid? 10 Common Errors and How to Fix Them",
        "excerpt": "JSON parsing errors can crash your app. Learn the 10 most common JSON syntax errors—trailing commas, unquoted keys, comments—and how to fix them instantly.",
        "description": "Why is my JSON invalid? Learn the 10 most common JSON syntax errors including trailing commas, unquoted keys, and single quotes, with instant fix solutions.",
        "keywords": "JSON invalid, JSON syntax error, trailing comma JSON, unquoted keys, fix JSON online",
        "body": """
                <p class="lead">Every developer has hit a "JSON.parse error" at least once. These errors usually come from a handful of predictable mistakes. Learn to spot and fix them instantly.</p>

                <h2>1. Trailing Commas</h2>
                <p>JSON arrays and objects cannot end with a comma:</p>
                <pre class="code-block"><code>// INVALID - trailing comma
{"name": "Alice",}

// VALID
{"name": "Alice"}</code></pre>
                <p><a href="../format.html">Use our JSON formatter</a> to automatically remove trailing commas.</p>

                <h2>2. Single Quotes</h2>
                <p>JSON requires double quotes for strings and keys:</p>
                <pre class="code-block"><code>// INVALID - single quotes
{'name': 'Alice'}

// VALID
{"name": "Alice"}</code></pre>

                <h2>3. Unquoted Keys</h2>
                <p>JavaScript allows unquoted keys, but JSON does not:</p>
                <pre class="code-block"><code>// INVALID - unquoted key
{name: "Alice"}

// VALID
{"name": "Alice"}</code></pre>

                <h2>4. Comments in JSON</h2>
                <p>JSON does not support comments. Use a JSONC parser or preprocess:</p>
                <pre class="code-block"><code>// INVALID - JSON cannot have comments
{
  "name": "Alice" // this is not allowed
}

// VALID - no comments
{
  "name": "Alice"
}</code></pre>

                <h2>5. Trailing Commas in Arrays</h2>
                <pre class="code-block"><code>// INVALID
[1, 2, 3, ]

// VALID
[1, 2, 3]</code></pre>

                <h2>6. Unquoted String Values</h2>
                <pre class="code-block"><code>// INVALID
{"status": active}

// VALID
{"status": "active"}</code></pre>

                <h2>7. Missing Colon or Comma</h2>
                <pre class="code-block"><code>// INVALID - missing colon
{"name" "Alice"}

// INVALID - missing comma
{"name": "Alice" "age": 30}</code></pre>

                <h2>8. Extra Comma Before Closing Bracket</h2>
                <pre class="code-block"><code>// INVALID
{"name": "Alice",}</code></pre>

                <h2>9. BOM Characters</h2>
                <p>Byte Order Marks from UTF-8 encoded files can break JSON parsing:</p>
                <pre class="code-block"><code>// INVALID - starts with BOM character
\uFEFF{"name": "Alice"}

// VALID - plain UTF-8
{"name": "Alice"}</code></pre>

                <h2>10. Newline in String Values</h2>
                <p>Strings must escape newlines:</p>
                <pre class="code-block"><code>// INVALID
{"bio": "Line 1
Line 2"}

// VALID
{"bio": "Line 1\\nLine 2"}</code></pre>

                <h2>Quick Fix: Use a JSON Validator</h2>
                <p>Paste your JSON into our <a href="../format.html">JSON Formatter</a>. It highlights errors and shows exactly where to fix them.</p>
"""
    },
    {
        "tool": "format",
        "slug": "how-to-validate-json-schema-beginners-guide",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "6-8 min read",
        "title": "How to Validate JSON Against a Schema: A Beginner's Guide",
        "excerpt": "JSON Schema lets you define the expected structure of your JSON data. Learn how to validate API responses and catch errors before they reach production.",
        "description": "Learn how to validate JSON against a schema. This beginner's guide covers JSON Schema basics, validation patterns, and how to use validators in your code.",
        "keywords": "JSON Schema validation, validate JSON, JSON Schema tutorial, API validation",
        "body": """
                <p class="lead">API returning unexpected data? JSON Schema validation catches mismatches before they crash your application. Here is how to use it.</p>

                <h2>What Is JSON Schema?</h2>
                <p>JSON Schema is a vocabulary that lets you annotate and validate JSON documents. Think of it as a contract for your JSON data:</p>
                <pre class="code-block"><code>{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer", "minimum": 0 },
    "email": { "type": "string", "format": "email" }
  },
  "required": ["name", "email"]
}</code></pre>

                <h2>Validating in JavaScript (ajv)</h2>
                <pre class="code-block"><code>import Ajv from 'ajv';
const ajv = new Ajv();

const schema = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    age: { type: 'integer', minimum: 0 }
  },
  required: ['name']
};

const validate = ajv.compile(schema);
const data = { name: 'Alice', age: 30 };

if (validate(data)) {
  console.log('Valid!');
} else {
  console.log('Errors:', validate.errors);
}</code></pre>

                <h2>Validating API Responses</h2>
                <p>Validate every API response before processing:</p>
                <pre class="code-block"><code>const response = await fetch('/api/user/123');
const data = await response.json();

if (!validate(data)) {
  throw new Error(`Invalid API response: ${JSON.stringify(validate.errors)}`);
}

// Now safe to use data
console.log(data.name);</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li><strong>API testing</strong> - Ensure test fixtures match production schemas</li>
                    <li><strong>Configuration files</strong> - Validate config.json before startup</li>
                    <li><strong>Data pipelines</strong> - Catch schema drift early</li>
                    <li><strong>LLM outputs</strong> - Validate structured generation</li>
                </ul>

                <h2>Tools</h2>
                <p>Format and preview your JSON with our <a href="../format.html">JSON Formatter</a> before applying schema validation.</p>
"""
    },
    {
        "tool": "clean",
        "slug": "how-to-clean-messy-json-remove-nulls-trailing-commas",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "5-6 min read",
        "title": "How to Clean Messy JSON: Remove Nulls, Fix Trailing Commas, and Normalize Keys",
        "excerpt": "Dirty JSON from APIs, exports, or pasted data often needs cleaning. Learn the common issues and how to fix them automatically.",
        "description": "How to clean messy JSON data. Remove null values, fix trailing commas, normalize keys, and handle common data quality issues with automated tools.",
        "keywords": "clean JSON, remove nulls JSON, JSON data cleaning, fix JSON online",
        "body": """
                <p class="lead">Data from APIs, spreadsheets, and manual exports often arrives messy. Learn to clean JSON automatically without writing parsing code.</p>

                <h2>Common JSON Data Issues</h2>
                <ul>
                    <li><strong>Null values</strong> - Often unnecessary in client code</li>
                    <li><strong>Trailing commas</strong> - Syntax errors waiting to happen</li>
                    <li><strong>Empty keys</strong> - <code>"name": ""</code> instead of omitting</li>
                    <li><strong>Extra whitespace</strong> - Makes files unnecessarily large</li>
                </ul>

                <h2>Fix #1: Remove Null Values</h2>
                <pre class="code-block"><code>// Before
{"name": "Alice", "phone": null, "email": "alice@example.com"}

// After - nulls removed
{"name": "Alice", "email": "alice@example.com"}</code></pre>
                <p>Use our <a href="../clean.html">JSON Cleaner</a> to remove nulls with one click.</p>

                <h2>Fix #2: Remove Empty Strings</h2>
                <pre class="code-block"><code>// Before
{"name": "Alice", "phone": "", "address": ""}

// After
{"name": "Alice"}</code></pre>

                <h2>Fix #3: Normalize Whitespace</h2>
                <pre class="code-block"><code>// Before - messy formatting
{  "name" : "Alice", "age" :30}

// After - clean and consistent
{"name":"Alice","age":30}</code></pre>

                <h2>Fix #4: Remove Trailing Commas</h2>
                <pre class="code-block"><code>// Before
{"name": "Alice",}

// After
{"name": "Alice"}</code></pre>

                <h2>When to Clean JSON</h2>
                <ul>
                    <li><strong>Before storing</strong> - Save clean data to databases</li>
                    <li><strong>Before API requests</strong> - Ensure clean payloads</li>
                    <li><strong>Data migration</strong> - Normalize before importing</li>
                    <li><strong>Testing</strong> - Create clean test fixtures</li>
                </ul>

                <h2>Use Cases</h2>
                <ul>
                    <li>Cleaning API response data for storage</li>
                    <li>Preparing JSON for database insertion</li>
                    <li>Normalizing exported spreadsheet data</li>
                    <li>Removing sensitive null fields before sharing</li>
                </ul>
"""
    },
    {
        "tool": "escape",
        "slug": "json-escape-sequences-special-characters-guide",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "4-5 min read",
        "title": "JSON Escape Sequences: Handling Special Characters in JSON Strings",
        "excerpt": "Newlines, tabs, quotes, and backslashes all need escaping in JSON. Learn the escape rules and how to handle them automatically.",
        "description": "JSON escape sequences guide: how to properly escape newlines, tabs, quotes, and special characters in JSON strings. Includes quick reference and examples.",
        "keywords": "JSON escape, escape JSON string, JSON special characters, newline in JSON",
        "body": """
                <p class="lead">Special characters in JSON strings must be escaped. Learn the rules and stop fighting JSON parsing errors.</p>

                <h2>Required Escape Sequences</h2>
                <table style="width: 100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid var(--border);">
                        <th style="text-align: left; padding: 0.5rem;">Character</th>
                        <th style="text-align: left; padding: 0.5rem;">Escape</th>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>"</code> (double quote)</td>
                        <td style="padding: 0.5rem;"><code>\"</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>\</code> (backslash)</td>
                        <td style="padding: 0.5rem;"><code>\\</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;">Newline</td>
                        <td style="padding: 0.5rem;"><code>\n</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;">Tab</td>
                        <td style="padding: 0.5rem;"><code>\t</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;">Carriage return</td>
                        <td style="padding: 0.5rem;"><code>\r</code></td>
                    </tr>
                </table>

                <h2>Example: Escaping Quotes in JSON</h2>
                <pre class="code-block"><code>// User's bio contains quotes
{"bio": "She said \"hello\" to me"}

// Correctly escaped
{"bio": "She said \\\"hello\\\" to me"}</code></pre>

                <h2>Example: Escaping Newlines</h2>
                <pre class="code-block"><code>// Multi-line text in JSON
{"address": "123 Main St\\nApt 4\\nNew York, NY"}

// Renders as:
// 123 Main St
// Apt 4
// New York, NY</code></pre>

                <h2>Common Mistakes</h2>
                <ul>
                    <li><strong>Unescaped quotes</strong> - Breaks the string: <code>"He said "hi""</code></li>
                    <li><strong>Unescaped backslashes</strong> - Windows paths need doubling: <code>"C:\\Users"</code></li>
                    <li><strong>Literal newlines</strong> - Strings cannot contain actual line breaks</li>
                </ul>

                <h2>Auto-Escape with Tools</h2>
                <p>Use our <a href="../escape.html">JSON Escape Tool</a> to automatically escape or unescape special characters in your JSON.</p>
"""
    },
    {
        "tool": "extract",
        "slug": "json-extraction-dot-notation-vs-jsonpath",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "5-7 min read",
        "title": "JSON Data Extraction: Dot Notation vs Nested Paths",
        "excerpt": "Need to pull specific data from nested JSON? Learn dot notation and path extraction to access deeply nested values without parsing the entire structure.",
        "description": "JSON extraction techniques: dot notation, bracket notation, and nested path access. How to extract data from complex nested JSON structures with examples.",
        "keywords": "JSON extract data, dot notation JSON, JSON nested, extract from JSON, JSON path",
        "body": """
                <p class="lead">Extracting data from nested JSON doesn't have to be painful. Learn dot notation and path-based extraction to pull exactly what you need.</p>

                <h2>The Problem with Nested JSON</h2>
                <pre class="code-block"><code>{
  "users": [
    {
      "id": 1,
      "profile": {
        "name": "Alice",
        "settings": {
          "theme": "dark"
        }
      }
    }
  ]
}</code></pre>

                <h2>Method 1: Dot Notation</h2>
                <p>Access properties using dot-separated path:</p>
                <pre class="code-block"><code>// Get Alice's theme setting
data.users[0].profile.settings.theme
// Returns: "dark"

// Get first user's name
data.users[0].profile.name
// Returns: "Alice"</code></pre>

                <h2>Method 2: Bracket Notation for Dynamic Keys</h2>
                <pre class="code-block"><code>// When key is dynamic or contains special chars
data["users"][0]["profile"]["settings"]["theme"]

// Useful for iteration
for (let user of data.users) {
  console.log(user.profile.name);
}</code></pre>

                <h2>Method 3: Array Filtering</h2>
                <pre class="code-block"><code>// Find user with id=2
const user = data.users.find(u => u.id === 2);

// Get all admin users
const admins = data.users.filter(u => u.role === 'admin');

// Get all usernames
const names = data.users.map(u => u.profile.name);</code></pre>

                <h2>Common Extraction Patterns</h2>
                <ul>
                    <li><strong>First item</strong>: <code>data.items[0]</code></li>
                    <li><strong>Last item</strong>: <code>data.items[data.items.length - 1]</code></li>
                    <li><strong>Count</strong>: <code>data.items.length</code></li>
                    <li><strong>Specific property</strong>: <code>data.results[0].value</code></li>
                </ul>

                <h2>Use Cases</h2>
                <ul>
                    <li>Pulling API response data into your application</li>
                    <li>Extracting configuration values from nested objects</li>
                    <li>Filtering and transforming data arrays</li>
                    <li>Accessing nested user profile information</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../extract.html">JSON Extractor</a> to pull specific data from your JSON using dot notation paths.</p>
"""
    },
    {
        "tool": "sort",
        "slug": "sort-json-arrays-objects-guide",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "4-5 min read",
        "title": "How to Sort JSON Arrays and Objects by Any Field",
        "excerpt": "Need to sort JSON data by date, name, or numeric value? Learn sorting techniques for arrays of objects with examples for different data types.",
        "description": "Sort JSON arrays by string, number, or date fields. Learn JavaScript sort methods for JSON data with examples for ascending and descending order.",
        "keywords": "sort JSON array, sort by date JSON, JSON sort example, order JSON data",
        "body": """
                <p class="lead">Sorting JSON arrays is essential for organizing data. Learn to sort by strings, numbers, and dates with clean JavaScript solutions.</p>

                <h2>Basic Array Sorting</h2>
                <pre class="code-block"><code>// Simple numeric sort
[3, 1, 4, 1, 5].sort((a, b) => a - b);
// [1, 1, 3, 4, 5]

// String sort
['banana', 'apple', 'cherry'].sort();
// ['apple', 'banana', 'cherry']</code></pre>

                <h2>Sort Array of Objects by Field</h2>
                <pre class="code-block"><code>const users = [
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 },
  { name: 'Carol', age: 35 }
];

// Sort by name (alphabetical)
users.sort((a, b) => a.name.localeCompare(b.name));

// Sort by age (ascending)
users.sort((a, b) => a.age - b.age);

// Sort by age (descending)
users.sort((a, b) => b.age - a.age);</code></pre>

                <h2>Sort by Date Field</h2>
                <pre class="code-block"><code>const events = [
  { name: 'Launch', date: '2026-04-15' },
  { name: 'Beta', date: '2026-03-01' },
  { name: 'Alpha', date: '2026-01-01' }
];

// Sort by ISO date string
events.sort((a, b) => new Date(a.date) - new Date(b.date));
// Chronological order: Alpha → Beta → Launch</code></pre>

                <h2>Sort by Nested Field</h2>
                <pre class="code-block"><code>const products = [
  { name: 'Phone', specs: { price: 999 } },
  { name: 'Tablet', specs: { price: 599 } }
];

// Sort by nested price
products.sort((a, b) => a.specs.price - b.specs.price);
// Tablet → Phone (cheapest first)</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li>Sort user lists by registration date</li>
                    <li>Order products by price for comparisons</li>
                    <li>Arrange transactions by timestamp</li>
                    <li>Sort leaderboard entries by score</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../sort.html">JSON Sorter</a> to quickly sort your JSON data by any field.</p>
"""
    },
    {
        "tool": "compare",
        "slug": "compare-json-documents-find-differences",
        "category": "Debugging",
        "cat_class": "cat-debugging",
        "read_time": "5-6 min read",
        "title": "How to Compare Two JSON Documents: Find Differences Instantly",
        "excerpt": "Comparing JSON by eye is error-prone. Learn to programmatically compare JSON documents and highlight exactly what changed between versions.",
        "description": "Compare two JSON documents and find differences. Learn diff algorithms, visual comparison tools, and how to track changes between JSON versions.",
        "keywords": "compare JSON, JSON diff, find JSON differences, JSON compare tool",
        "body": """
                <p class="lead">When JSON data changes, spotting the differences manually is nearly impossible. Here's how to compare JSON documents programmatically.</p>

                <h2>The Challenge: JSON Is Nested</h2>
                <p>Unlike plain text, JSON has structure. A simple value change might be buried in a deeply nested object.</p>

                <h2>Compare Two JSON Objects</h2>
                <pre class="code-block"><code>function deepEqual(obj1, obj2) {
  return JSON.stringify(obj1) === JSON.stringify(obj2);
}

// But this doesn't tell you WHAT changed...</code></pre>

                <h2>Find What Changed</h2>
                <pre class="code-block"><code>function getDiff(oldObj, newObj, path = '') {
  const differences = [];

  for (const key in newObj) {
    const newPath = path ? `${path}.${key}` : key;

    if (!(key in oldObj)) {
      differences.push({ path: newPath, type: 'added', value: newObj[key] });
    } else if (typeof newObj[key] !== typeof oldObj[key]) {
      differences.push({
        path: newPath,
        type: 'type_changed',
        old: oldObj[key],
        new: newObj[key]
      });
    } else if (typeof newObj[key] === 'object') {
      differences.push(...getDiff(oldObj[key], newObj[key], newPath));
    } else if (newObj[key] !== oldObj[key]) {
      differences.push({
        path: newPath,
        type: 'changed',
        old: oldObj[key],
        new: newObj[key]
      });
    }
  }

  return differences;
}</code></pre>

                <h2>Example Output</h2>
                <pre class="code-block"><code>getDiff(
  { user: { name: 'Alice', age: 30 } },
  { user: { name: 'Alice', age: 31 } }
);

// Result:
[
  { path: 'user.age', type: 'changed', old: 30, new: 31 }
]</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li><strong>API testing</strong> - Compare expected vs actual responses</li>
                    <li><strong>Config tracking</strong> - Monitor config file changes</li>
                    <li><strong>Debugging</strong> - Find why your data looks different</li>
                    <li><strong>Version comparison</strong> - Track JSON data evolution</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../compare.html">JSON Compare</a> tool to visually compare two JSON documents and highlight all differences.</p>
"""
    },
    {
        "tool": "viewer",
        "slug": "json-viewer-tree-view-why-you-need-one",
        "category": "Debugging",
        "cat_class": "cat-debugging",
        "read_time": "4-5 min read",
        "title": "JSON Viewer: Why You Need a Tree View for Large JSON Documents",
        "excerpt": "Debugging raw JSON is painful. A tree view makes navigating complex nested structures easy. Learn when to use a viewer and what features to look for.",
        "description": "JSON tree viewer explained: why raw JSON is hard to read, benefits of tree views, and how to use visual JSON exploration for faster debugging.",
        "keywords": "JSON viewer, JSON tree view, visualize JSON, JSON explorer",
        "body": """
                <p class="lead">Raw JSON in a text editor is nearly impossible to navigate for anything beyond simple structures. Here's why you need a tree view.</p>

                <h2>The Problem with Raw JSON</h2>
                <p>Try reading this:</p>
                <pre class="code-block"><code>{"users":[{"id":1,"profile":{"name":"Alice","settings":{"theme":"dark","notifications":{"email":true,"push":false}}},{"id":2,"profile":{"name":"Bob","settings":{"theme":"light","notifications":{"email":false,"push":true}}}}]}</code></pre>

                <h2>Tree View Makes It Clear</h2>
                <pre class="code-block"><code>users: Array[2]
├── 0: object
│   ├── id: 1
│   └── profile: object
│       ├── name: "Alice"
│       └── settings: object
│           ├── theme: "dark"
│           └── notifications: object
│               ├── email: true
│               └── push: false
└── 1: object
    └── ...</code></pre>

                <h2>Key Features of a Good JSON Viewer</h2>
                <ul>
                    <li><strong>Expand/collapse</strong> - Focus on what matters</li>
                    <li><strong>Type indicators</strong> - See strings, numbers, booleans at a glance</li>
                    <li><strong>Search</strong> - Find values anywhere in the tree</li>
                    <li><strong>Path display</strong> - Know exactly where you are</li>
                    <li><strong>Copy path</strong> - Extract the location to code</li>
                </ul>

                <h2>When to Use a JSON Viewer</h2>
                <ul>
                    <li><strong>API debugging</strong> - Inspect response structure</li>
                    <li><strong>Config files</strong> - Explore complex nested settings</li>
                    <li><strong>Data exploration</strong> - Understand unfamiliar JSON formats</li>
                    <li><strong>Learning</strong> - Visualize JSON structure while learning</li>
                </ul>

                <h2>Use Cases</h2>
                <ul>
                    <li>Inspecting API responses during development</li>
                    <li>Understanding complex configuration files</li>
                    <li>Exploring nested data from databases</li>
                    <li>Teaching JSON structure to beginners</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../viewer.html">JSON Viewer</a> to explore your JSON data with an interactive tree view.</p>
"""
    },
    # ===== YAML COMPARISON ARTICLES =====
    {
        "tool": "yaml",
        "slug": "json-vs-yaml-when-to-use-each",
        "category": "Comparison",
        "cat_class": "cat-comparison",
        "read_time": "6-8 min read",
        "title": "JSON vs YAML: When to Use Each Format in 2026",
        "excerpt": "JSON and YAML look similar but serve different purposes. Learn the key differences, trade-offs, and when each format is the better choice for your project.",
        "description": "JSON vs YAML comparison: when to use each format, key differences in syntax and use cases, and how to convert between them. Practical guide for developers.",
        "keywords": "JSON vs YAML, YAML vs JSON, when to use YAML, JSON YAML conversion",
        "body": """
                <p class="lead">JSON and YAML can often be used interchangeably, but choosing the right one matters. Here's when to use each format.</p>

                <h2>Side-by-Side Comparison</h2>
                <pre class="code-block"><code>// JSON
{
  "name": "Alice",
  "age": 30,
  "active": true,
  "tags": ["developer", "admin"]
}

// YAML
name: Alice
age: 30
active: true
tags:
  - developer
  - admin</code></pre>

                <h2>JSON Advantages</h2>
                <ul>
                    <li><strong>Universal support</strong> - Every programming language has native JSON parsing</li>
                    <li><strong>Strict syntax</strong> - No ambiguity, consistent parsing</li>
                    <li><strong>Compact</strong> - Less whitespace means smaller files</li>
                    <li><strong>Fast parsing</strong> - Native browser/JS integration</li>
                    <li><strong>API standard</strong> - The de facto format for web APIs</li>
                </ul>

                <h2>YAML Advantages</h2>
                <ul>
                    <li><strong>Human-readable</strong> - Less noisy syntax, easier to read</li>
                    <li><strong>Comments</strong> - YAML supports # comments, JSON doesn't</li>
                    <li><strong>Multi-document</strong> - One file, multiple documents separated by ---</li>
                    <li><strong>Complex data</strong> - Anchors, aliases, and advanced features</li>
                    <li><strong>No brackets</strong> - Clean visual structure</li>
                </ul>

                <h2>When to Use JSON</h2>
                <ul>
                    <li><strong>Web APIs</strong> - REST and GraphQL both use JSON</li>
                    <li><strong>Configuration in code</strong> - Package.json, tsconfig.json</li>
                    <li><strong>Data exchange</strong> - Between different systems and languages</li>
                    <li><strong>Storage</strong> - Database documents, cached data</li>
                    <li><strong>Speed-critical</strong> - When parsing performance matters</li>
                </ul>

                <h2>When to Use YAML</h2>
                <ul>
                    <li><strong>Application config</strong> - Docker Compose, Kubernetes, Ansible</li>
                    <li><strong>Documentation</strong> - Where comments add value</li>
                    <li><strong>Configuration files</strong> - Rails, Jekyll, CircleCI configs</li>
                    <li><strong>Multi-document files</strong> - One file with multiple related docs</li>
                    <li><strong>Human-maintained</strong> - Where readability trumps all</li>
                </ul>

                <h2>Converting Between Formats</h2>
                <p>Use our <a href="../yaml.html">JSON to YAML converter</a> to transform between formats instantly.</p>
"""
    },
    {
        "tool": "yaml",
        "slug": "convert-json-to-yaml-online",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "3-4 min read",
        "title": "How to Convert JSON to YAML: A Quick Guide",
        "excerpt": "Need YAML but have JSON? Learn the conversion process, understand the mapping, and use online tools to transform JSON to YAML instantly.",
        "description": "Convert JSON to YAML: learn the conversion rules, common pitfalls, and how to use online converters. Includes examples and best practices.",
        "keywords": "JSON to YAML, convert JSON YAML, YAML converter online",
        "body": """
                <p class="lead">Converting JSON to YAML is straightforward once you understand the mapping. Here's everything you need to know.</p>

                <h2>Basic Conversion Rules</h2>
                <table style="width: 100%; border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid var(--border);">
                        <th style="text-align: left; padding: 0.5rem;">JSON</th>
                        <th style="text-align: left; padding: 0.5rem;">YAML</th>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>{"key": "value"}</code></td>
                        <td style="padding: 0.5rem;"><code>key: value</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>{"array": [1, 2, 3]}</code></td>
                        <td style="padding: 0.5rem;"><code>array:<br>&nbsp;&nbsp;- 1<br>&nbsp;&nbsp;- 2<br>&nbsp;&nbsp;- 3</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>{"bool": true}</code></td>
                        <td style="padding: 0.5rem;"><code>bool: true</code></td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border);">
                        <td style="padding: 0.5rem;"><code>{"null": null}</code></td>
                        <td style="padding: 0.5rem;"><code>null: ~</code></td>
                    </tr>
                </table>

                <h2>Example: JSON to YAML</h2>
                <pre class="code-block"><code>// JSON Input
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": {
      "user": "admin",
      "password": "secret"
    }
  }
}

// YAML Output
database:
  host: localhost
  port: 5432
  credentials:
    user: admin
    password: secret</code></pre>

                <h2>Conversion Considerations</h2>
                <ul>
                    <li><strong>Quoted strings</strong> - YAML infers types; use quotes to force strings</li>
                    <li><strong>Multiline strings</strong> - Use | for preserved newlines, > for folding</li>
                    <li><strong>Special characters</strong> - Escape colon after space: <code>"JSON:YAML"</code></li>
                </ul>

                <h2>Use Cases</h2>
                <ul>
                    <li>Convert API config to Docker Compose format</li>
                    <li>Transform JSON exports to human-readable config</li>
                    <li>Migrate from JSON to YAML-based tooling</li>
                    <li>Create YAML documentation from JSON data</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../yaml.html">JSON to YAML converter</a> to transform your JSON to YAML instantly.</p>
"""
    },
    # ===== XML COMPARISON ARTICLES =====
    {
        "tool": "xml",
        "slug": "json-vs-xml-what-to-choose",
        "category": "Comparison",
        "cat_class": "cat-comparison",
        "read_time": "6-8 min read",
        "title": "JSON vs XML: Choosing the Right Data Format for Modern Development",
        "excerpt": "XML dominated the web era, but JSON won modern APIs. Learn when XML still makes sense and why JSON became the default for new projects.",
        "description": "JSON vs XML comparison for modern developers. When to use each format, migration strategies, and how to convert between JSON and XML.",
        "keywords": "JSON vs XML, XML vs JSON, when to use XML, legacy XML to JSON",
        "body": """
                <p class="lead">XML ruled enterprise data for a decade. Now JSON dominates web APIs. Here's when XML still has a place.</p>

                <h2>Side-by-Side</h2>
                <pre class="code-block"><code><!-- XML -->
<user>
  <name>Alice</name>
  <age>30</age>
  <active>true</active>
</user>

// JSON
{
  "user": {
    "name": "Alice",
    "age": 30,
    "active": true
  }
}</code></pre>

                <h2>XML Strengths</h2>
                <ul>
                    <li><strong>Namespaces</strong> - Avoid element name conflicts</li>
                    <li><strong>Schemas (XSD)</strong> - Rich validation with built-in types</li>
                    <li><strong>Stylesheets (XSLT)</strong> - Transform XML to other formats</li>
                    <li><strong>Rich tooling</strong> - XPath, XQuery, XML databases</li>
                    <li><strong>Legacy systems</strong> - SOAP, RSS, SVG, Office documents</li>
                </ul>

                <h2>JSON Strengths</h2>
                <ul>
                    <li><strong>Native web</strong> - Built into JavaScript, parsers everywhere</li>
                    <li><strong>Compact</strong> - Less verbose, smaller payloads</li>
                    <li><strong>Modern APIs</strong> - REST, GraphQL, OpenAPI all default to JSON</li>
                    <li><strong>Type inference</strong> - Numbers stay numbers, booleans stay booleans</li>
                    <li><strong>Ecosystem</strong> - Every modern tool speaks JSON</li>
                </ul>

                <h2>When to Use XML</h2>
                <ul>
                    <li><strong>Legacy integrations</strong> - SOAP APIs, older enterprise systems</li>
                    <li><strong>Document formats</strong> - Office Open XML (.docx, .xlsx)</li>
                    <li><strong>Strict validation</strong> - When XSD schemas are required</li>
                    <li><strong>RSS/Atom feeds</strong> - Feed standards still use XML</li>
                    <li><strong>SVG graphics</strong> - Vector graphics are XML-based</li>
                </ul>

                <h2>When to Use JSON</h2>
                <ul>
                    <li><strong>New web APIs</strong> - Default choice for modern REST APIs</li>
                    <li><strong>Configuration</strong> - package.json, tsconfig.json, etc.</li>
                    <li><strong>Real-time data</strong> - WebSockets, Server-Sent Events</li>
                    <li><strong>NoSQL databases</strong> - MongoDB, CouchDB document stores</li>
                    <li><strong>Microservices</strong> - Inter-service communication</li>
                </ul>

                <h2>Converting XML to JSON</h2>
                <p>Use our <a href="../xml.html">XML to JSON converter</a> to transform legacy XML data to modern JSON format.</p>
"""
    },
    # ===== CSV COMPARISON ARTICLES =====
    {
        "tool": "json2csv",
        "slug": "json-vs-csv-when-to-convert",
        "category": "Comparison",
        "cat_class": "cat-comparison",
        "read_time": "5-6 min read",
        "title": "JSON vs CSV: When to Convert and Why It Matters",
        "excerpt": "JSON for nested data, CSV for flat tables. Learn when to convert between them and how to handle complex nested structures when converting to tabular format.",
        "description": "JSON vs CSV comparison: when to use each format, how to flatten nested JSON for CSV export, and common conversion pitfalls to avoid.",
        "keywords": "JSON vs CSV, JSON to CSV, CSV vs JSON, flatten JSON",
        "body": """
                <p class="lead">JSON and CSV solve different problems. Nested data stays in JSON; flat tables belong in CSV. Here's how to choose and convert wisely.</p>

                <h2>When JSON Is Better</h2>
                <pre class="code-block"><code>{
  "order": {
    "id": "ORD-123",
    "customer": {
      "name": "Alice",
      "email": "alice@example.com"
    },
    "items": [
      { "product": "Widget", "qty": 2 },
      { "product": "Gadget", "qty": 1 }
    ]
  }
}</code></pre>

                <h2>When CSV Is Better</h2>
                <pre class="code-block"><code>product,qty,price
Widget,2,19.99
Gadget,1,29.99
Total,3,69.97</code></pre>

                <h2>Flattening Nested JSON for CSV</h2>
                <p>Complex nested JSON must be flattened to export to CSV:</p>
                <pre class="code-block"><code>// Nested JSON
{ "name": "Alice", "address": { "city": "NYC", "zip": "10001" } }

// Flattened for CSV
name,address.city,address.zip
Alice,NYC,10001</code></pre>

                <h2>Conversion Challenges</h2>
                <ul>
                    <li><strong>Arrays</strong> - Arrays need special handling: one row per item or join to string</li>
                    <li><strong>Deep nesting</strong> - Very deep structures become unwieldy in CSV</li>
                    <li><strong>Missing values</strong> - Sparse data wastes columns</li>
                    <li><strong>Mixed types</strong> - Arrays of objects with different keys</li>
                </ul>

                <h2>When to Convert JSON to CSV</h2>
                <ul>
                    <li><strong>Excel/Sheets import</strong> - Non-technical users need tabular data</li>
                    <li><strong>Database import</strong> - SQL databases prefer flat structures</li>
                    <li><strong>Data analysis</strong> - Pandas, R, BI tools work better with tables</li>
                    <li><strong>Print/export</strong> - Simple reports look better as tables</li>
                </ul>

                <h2>Use Cases</h2>
                <ul>
                    <li>Exporting API data to spreadsheets</li>
                    <li>Loading JSON API data into SQL databases</li>
                    <li>Preparing data for statistical analysis</li>
                    <li>Creating reports from nested API responses</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../json2csv.html">JSON to CSV converter</a> to transform your JSON data to tabular format.</p>
"""
    },
    # ===== API TESTING ARTICLES =====
    {
        "tool": "format",
        "slug": "format-json-for-api-testing-debugging",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "4-5 min read",
        "title": "How to Format JSON for API Testing and Debugging",
        "excerpt": "Minified API responses are impossible to read. Learn to format JSON instantly for easier debugging, testing, and understanding API responses.",
        "description": "Format JSON for API testing. Learn to prettify minified JSON, validate responses, and debug API issues faster with proper JSON formatting tools.",
        "keywords": "format JSON API, API testing JSON, JSON debugging, prettify JSON",
        "body": """
                <p class="lead">API responses often come minified. Formatting them is the first step to debugging. Here's how to do it efficiently.</p>

                <h2>The Problem: Minified API Response</h2>
                <pre class="code-block"><code>{"status":"success","data":{"users":[{"id":1,"name":"Alice","email":"alice@example.com"},{"id":2,"name":"Bob","email":"bob@example.com"}],"total":2,"page":1}}</code></pre>

                <h2>After Formatting</h2>
                <pre class="code-block"><code>{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
      },
      {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com"
      }
    ],
    "total": 2,
    "page": 1
  }
}</code></pre>

                <h2>Common API Testing Workflow</h2>
                <ol>
                    <li><strong>Copy response</strong> - Paste API response from Postman/curl/browser</li>
                    <li><strong>Format</strong> - Use JSON formatter to prettify</li>
                    <li><strong>Validate</strong> - Check for syntax errors</li>
                    <li><strong>Extract</strong> - Pull specific values for assertions</li>
                    <li><strong>Compare</strong> - Check against expected responses</li>
                </ol>

                <h2>Validating API Responses</h2>
                <p>Before testing, validate the JSON is well-formed:</p>
                <pre class="code-block"><code>// In JavaScript
try {
  const data = JSON.parse(responseBody);
  console.log('Valid JSON');
} catch (e) {
  console.error('Invalid JSON:', e.message);
}</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li>Debugging API responses in Postman or curl</li>
                    <li>Validating webhook payloads</li>
                    <li>Checking database JSON output</li>
                    <li>Comparing API versions</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../format.html">JSON Formatter</a> to prettify and validate API responses instantly.</p>
"""
    },
    {
        "tool": "clean",
        "slug": "common-api-response-data-quality-issues",
        "category": "Debugging",
        "cat_class": "cat-debugging",
        "read_time": "5-6 min read",
        "title": "Common API Response Data Quality Issues and How to Fix Them",
        "excerpt": "Real-world API responses are messy. Learn to handle nulls, missing fields, inconsistent types, and other data quality issues in API responses.",
        "description": "API response data quality issues: handling nulls, missing fields, inconsistent types, and data cleaning strategies for API integration.",
        "keywords": "API data quality, clean API response, handle null JSON, API debugging",
        "body": """
                <p class="lead">Production APIs rarely return perfect data. Here's how to handle the common data quality issues you'll encounter.</p>

                <h2>Issue #1: Inconsistent Null Handling</h2>
                <pre class="code-block"><code>// API sometimes returns null, sometimes empty string
{ "phone": null }
{ "phone": "" }
{ "phone": " " }

// Normalize during processing
const phone = data.phone?.trim() || null;</code></pre>

                <h2>Issue #2: Missing Fields</h2>
                <pre class="code-block"><code>// API returns different shapes
{ "name": "Alice" }
{ "name": "Bob", "age": 30 }
{ }

// Safe access with defaults
const age = data.age ?? 0;
const email = data.email ?? 'no-email@placeholder.com';</code></pre>

                <h2>Issue #3: Type Coercion Issues</h2>
                <pre class="code-block"><code>// Numbers as strings
{ "price": "29.99" }
{ "active": "true" }
{ "count": "42" }

// Convert to proper types
const price = parseFloat(data.price);
const active = data.active === 'true';
const count = parseInt(data.count, 10);</code></pre>

                <h2>Issue #4: Trailing Whitespace</h2>
                <pre class="code-block"><code>// Fields with hidden whitespace
{ "name": "Alice  " }
{ "email": " alice@example.com " }

// Trim all string values
const clean = Object.fromEntries(
  Object.entries(data).map(([k, v]) =>
    [k, typeof v === 'string' ? v.trim() : v]
  )
);</code></pre>

                <h2>Cleaning Pipeline Pattern</h2>
                <pre class="code-block"><code>function cleanApiResponse(data) {
  return {
    ...data,
    phone: data.phone?.trim() || null,
    email: data.email?.trim().toLowerCase() || null,
    age: Number(data.age) || 0,
    active: data.active === true || data.active === 'true'
  };
}</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li>Normalizing third-party API responses</li>
                    <li>Preparing data for database storage</li>
                    <li>Handling edge cases in webhook processing</li>
                    <li>Building resilient API clients</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../clean.html">JSON Cleaner</a> to remove nulls, trim whitespace, and normalize your API responses.</p>
"""
    },
    # ===== REGEX/EXTRACT TUTORIALS =====
    {
        "tool": "extract",
        "slug": "extract-data-from-complex-json-arrays",
        "category": "Tutorial",
        "cat_class": "cat-tutorial",
        "read_time": "5-6 min read",
        "title": "Extract Data from Complex JSON Arrays: Filtering, Mapping, and Transforming",
        "excerpt": "Need specific data from large JSON arrays? Learn array filtering, property extraction, and transformation techniques to get exactly what you need.",
        "description": "Extract data from JSON arrays: filter by conditions, map to new shapes, flatten nested arrays. Practical examples for common data extraction scenarios.",
        "keywords": "extract JSON array, filter JSON, map JSON array, JSON transformation",
        "body": """
                <p class="lead">Large JSON arrays often contain exactly the data you need—buried under layers of structure. Here's how to extract it.</p>

                <h2>Filtering Arrays by Condition</h2>
                <pre class="code-block"><code>const products = [
  { name: "Widget", price: 29, category: "tools" },
  { name: "Gadget", price: 99, category: "electronics" },
  { name: "Wrench", price: 15, category: "tools" }
];

// Get only tools
const tools = products.filter(p => p.category === 'tools');

// Get items under $50
const affordable = products.filter(p => p.price < 50);</code></pre>

                <h2>Extracting Single Values</h2>
                <pre class="code-block"><code>// Get all product names
const names = products.map(p => p.name);
// ["Widget", "Gadget", "Wrench"]

// Get prices as numbers
const prices = products.map(p => p.price);
// [29, 99, 15]</code></pre>

                <h2>Flattening Nested Arrays</h2>
                <pre class="code-block"><code>const orders = [
  { id: 1, items: ["Widget", "Gadget"] },
  { id: 2, items: ["Wrench"] }
];

// Flatten all items into one array
const allItems = orders.flatMap(o => o.items);
// ["Widget", "Gadget", "Wrench"]

// Count total items
const totalItems = orders.reduce((sum, o) => sum + o.items.length, 0);
// 3</code></pre>

                <h2>Finding Specific Items</h2>
                <pre class="code-block"><code>// Find first matching item
const expensiveItem = products.find(p => p.price > 50);
// { name: "Gadget", price: 99, category: "electronics" }

// Check if any item matches
const hasExpensive = products.some(p => p.price > 50);
// true</code></pre>

                <h2>Transforming Array Shape</h2>
                <pre class="code-block"><code>// Extract to a simpler shape
const productList = products.map(p => ({
  title: p.name,
  cost: p.price
}));
// [{ title: "Widget", cost: 29 }, ...]</code></pre>

                <h2>Use Cases</h2>
                <ul>
                    <li>Pull user data from API response arrays</li>
                    <li>Filter transaction history by date</li>
                    <li>Extract IDs for bulk operations</li>
                    <li>Transform API data for UI display</li>
                </ul>

                <h2>Try It Out</h2>
                <p>Use our <a href="../extract.html">JSON Extractor</a> to pull specific data from your JSON arrays.</p>
"""
    },
]

# ============================================================================
# FILE PATHS
# ============================================================================
PROJECT_ROOT = r'd:\网站开发-json'
BLOG_PATH = os.path.join(PROJECT_ROOT, 'pages', 'blog.html')
BLOG_DIR = os.path.join(PROJECT_ROOT, 'pages', 'blog')
INDEX_PATH = os.path.join(PROJECT_ROOT, 'index.html')
PUSH_SCRIPT = os.path.join(PROJECT_ROOT, 'scripts', 'push_to_github.py')
PYTHON_EXE = r'C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe'


# ============================================================================
# UTILITY
# ============================================================================
def get_display_date():
    return datetime.now().strftime('%Y-%m-%d')


def get_article_page_path(slug):
    return os.path.join(BLOG_DIR, f'{slug}.html')


def get_article_url(slug):
    return f'https://www.aijsons.com/pages/blog/{slug}.html'


def get_article_rel_path(slug):
    """Relative path from blog.html to article page."""
    return f'blog/{slug}.html'


# ============================================================================
# GENERATE STANDALONE ARTICLE PAGE
# ============================================================================
NAVBAR_TOOLS = """<div class="nav-dropdown"><a href="#" class="nav-link nav-dropdown-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>Tools</a><div class="nav-dropdown-menu wide"><div class="nav-dropdown-menu-box"><a href="../format.html" class="nav-link">Format</a><a href="../escape.html" class="nav-link">Escape</a><a href="../extract.html" class="nav-link">Extract</a><a href="../sort.html" class="nav-link">Sort</a><a href="../clean.html" class="nav-link">Clean</a><a href="../xml.html" class="nav-link">XML</a><a href="../yaml.html" class="nav-link">YAML</a><a href="../viewer.html" class="nav-link">Viewer</a><a href="../json2csv.html" class="nav-link">CSV</a><a href="../compare.html" class="nav-link">Compare</a></div></div></div>"""


def create_article_page(topic, date_str):
    slug = topic['slug']
    title = topic['title']
    description = topic['description']
    keywords = topic['keywords']
    category = topic['category']
    cat_class = topic['cat_class']
    read_time = topic['read_time']
    body = topic['body']
    url = get_article_url(slug)
    tool = topic.get('tool', 'format')
    tool_link = TOOL_MAPPING.get(tool, '../format.html')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">

    <title>{title} | AI JSON</title>
    <link rel="canonical" href="{url}">

    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="article:published_time" content="{date_str}">
    <meta property="article:section" content="{category}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
    <link rel="stylesheet" href="../../css/styles.css">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "description": "{description}",
        "datePublished": "{date_str}",
        "author": {{"@type": "Organization", "name": "AI JSON"}},
        "publisher": {{"@type": "Organization", "name": "AI JSON", "url": "https://www.aijsons.com"}},
        "url": "{url}",
        "articleSection": "{category}"
    }}
    </script>
</head>
<body>
    <nav class="navbar">
        <a href="../../index.html" class="navbar-brand"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>AI JSON</a>
        <button class="menu-toggle" aria-label="Menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
        <div class="navbar-links">
            <a href="../../index.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>Home</a>
            {NAVBAR_TOOLS}
            <a href="index.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>Blog</a>
            <a href="../best-practices.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>Practices</a>
            <a href="../news.html" class="nav-link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>News</a>
            <a href="../about.html" class="nav-link">About</a>
            <a href="../changelog.html" class="nav-link">Changelog</a>
        </div>
    </nav>

    <main class="main-container">
        <article>
            <div class="article-header">
                <div class="breadcrumb"><a href="index.html">Blog</a> / <span>Article</span></div>
                <div class="article-category {cat_class}">{category}</div>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta"><span>Published: {date_str}</span> · <span>{read_time}</span></div>
                <div style="margin-top: 1rem;">
                    <a href="{tool_link}" class="btn btn-primary">Try the Related Tool →</a>
                </div>
            </div>

            <div class="article-content">
{body}
            </div>
        </article>
    </main>

    <footer class="footer">
        <p>AI JSON - Instant client-side JSON processing. Your data stays private.</p>
        <p class="text-sm mt-sm">
            <a href="../about.html" class="text-primary">About</a> |
            <a href="../changelog.html" class="text-primary">Changelog</a> |
            <a href="../../privacy.html" class="text-primary">Privacy Policy</a> |
            <a href="../../terms.html" class="text-primary">Terms of Service</a>
        </p>
        <p class="text-small mt-sm">&copy; 2026 AI JSON. All rights reserved.</p>
    </footer>

    <script src="../../js/app.js" defer></script>
</body>
</html>
'''
    return html


# ============================================================================
# UPDATE BLOG.HTML
# ============================================================================
FEATURED_MARKER = '<!-- Featured Article -->'
ARTICLES_GRID_MARKER = '<!-- All Articles Grid -->'
ARTICLES_GRID_INNER_MARKER = '<div class="articles-grid">'


def update_blog_html(topic, date_str):
    """Update blog.html:
    1. Replace featured article section with new article card
    2. Prepend new article card to All Articles Grid
    """
    slug = topic['slug']
    title = topic['title']
    excerpt = topic['excerpt']
    category = topic['category']
    cat_class = topic['cat_class']
    read_time = topic['read_time']
    rel_path = get_article_rel_path(slug)

    with open(BLOG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Replace Featured Article section ---
    featured_start = content.find(FEATURED_MARKER)
    if featured_start < 0:
        print('[WARN] Could not find Featured Article marker in blog.html')
        return False

    # Find the closing </section> for the featured section
    section_end = content.find('</section>', featured_start) + len('</section>')

    new_featured = f'''<!-- Featured Article -->
        <section class="featured-section">
            <h2 class="section-title">Latest Article</h2>
            <article class="article-card featured-article">
                <div class="article-category {cat_class}">{category}</div>
                <h2><a href="{rel_path}">{title}</a></h2>
                <p class="article-excerpt">{excerpt}</p>
                <div class="article-meta">
                    <span>{date_str}</span> |
                    <span>{read_time}</span>
                </div>
                <a href="{rel_path}" class="read-more">Read full article →</a>
            </article>
        </section>'''

    content = content[:featured_start] + new_featured + content[section_end:]

    # --- 2. Prepend new card to All Articles Grid ---
    grid_marker_pos = content.find(ARTICLES_GRID_INNER_MARKER,
                                   content.find(ARTICLES_GRID_MARKER))
    if grid_marker_pos < 0:
        print('[WARN] Could not find articles-grid in blog.html')
        return False

    grid_open_end = content.find('>', grid_marker_pos) + 1

    new_card = f'''
                <article class="article-card">
                    <div class="article-category {cat_class}">{category}</div>
                    <h3><a href="{rel_path}">{title}</a></h3>
                    <p class="article-excerpt">{excerpt}</p>
                    <div class="article-meta">
                        <span>{date_str}</span> |
                        <span>{read_time}</span>
                    </div>
                    <a href="{rel_path}" class="read-more">Read article →</a>
                </article>'''

    content = content[:grid_open_end] + new_card + content[grid_open_end:]

    with open(BLOG_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'[OK] Updated blog.html with article card: {rel_path}')
    return True


# ============================================================================
# UPDATE INDEX.HTML
# ============================================================================
def update_index_html(topic, date_str):
    """Insert new article card into index.html Latest Articles section."""
    slug = topic['slug']
    title = topic['title']
    excerpt = topic['excerpt']
    rel_path = f'pages/blog/{slug}.html'

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    new_card = f'''<article class="feature-card" style="text-align: left;">
    <span style="font-size: 0.8rem; color: var(--text-secondary);">{date_str}</span>
    <h3 style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);">{title}</h3>
    <p style="color: var(--text-secondary); font-size: 0.95rem;">{excerpt[:150]}...</p>
    <a href="{rel_path}" style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;">Read more →</a>
</article>'''

    grid_start = content.find('<div class="feature-grid">', content.find('Latest Articles'))
    if grid_start < 0:
        print('[WARN] Could not find Latest Articles feature-grid in index.html')
        return False

    grid_open_end = content.find('>', grid_start) + 1
    content = content[:grid_open_end] + '\n    ' + new_card + content[grid_open_end:]

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'[OK] Updated index.html with article card: {title[:50]}')
    return True


# ============================================================================
# PUSH TO GITHUB
# ============================================================================
def push_to_github(commit_message):
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print('[WARN] GITHUB_TOKEN not set, skipping push')
        return False
    try:
        result = subprocess.run(
            [PYTHON_EXE, PUSH_SCRIPT, commit_message],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        if result.returncode == 0:
            print('[OK] Pushed to GitHub')
            return True
        else:
            print(f'[FAIL] Push failed: {result.stderr}')
            return False
    except Exception as e:
        print(f'[FAIL] Push error: {e}')
        return False


# ============================================================================
# DUPLICATE CHECK
# ============================================================================
def article_exists(slug):
    return os.path.exists(get_article_page_path(slug))


# ============================================================================
# VALIDATE ARTICLE STRUCTURE
# ============================================================================
def validate_article_structure(article_path):
    """Validate that new article has correct HTML structure."""
    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required = ['article-header', 'article-title', 'article-content', '../../css/styles.css']
    missing = [r for r in required if r not in content]
    
    if missing:
        print(f'[WARN] Article missing: {missing}')
        return False
    return True


# ============================================================================
# MAIN
# ============================================================================
def main():
    print('=' * 60)
    print('Tool-Focused Blog Automation - AIJSON')
    print(f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('=' * 60)

    date_str = get_display_date()
    day_of_year = datetime.now().timetuple().tm_yday
    topic_index = day_of_year % len(TOOL_BLOG_TOPICS)
    topic = TOOL_BLOG_TOPICS[topic_index]

    print(f'\nTopic: {topic["slug"]}')
    print(f'Tool:  {topic["tool"]}')
    print(f'Slug:  {topic["slug"]}')

    # Check if today's article already exists
    if article_exists(topic['slug']):
        print(f'[SKIP] Article already exists: {topic["slug"]}')
        return 0

    # Ensure blog directory exists
    Path(BLOG_DIR).mkdir(parents=True, exist_ok=True)

    # 1. Create standalone article page
    article_html = create_article_page(topic, date_str)
    article_path = get_article_page_path(topic['slug'])
    with open(article_path, 'w', encoding='utf-8') as f:
        f.write(article_html)
    print(f'[OK] Created article page: {article_path}')

    # Validate structure
    if not validate_article_structure(article_path):
        print('[FAIL] Article structure validation failed')
        return 1

    # 2. Update blog.html
    blog_ok = update_blog_html(topic, date_str)

    # 3. Update index.html
    index_ok = update_index_html(topic, date_str)

    if not blog_ok or not index_ok:
        print('\n[FAIL] Failed to update some files')
        return 1

    # 4. Push to GitHub
    commit_msg = f'Tool blog: {topic["title"][:60]}'
    push_to_github(commit_msg)

    print('\n' + '=' * 60)
    print('[OK] Tool-focused blog update completed!')
    print('=' * 60)
    return 0


if __name__ == '__main__':
    exit(main())
