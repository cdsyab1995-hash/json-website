# -*- coding: utf-8 -*-
"""
Daily Blog Update Script
自动生成 SEO 优化博客文章，更新 blog/index.html，并推送到 GitHub
"""
import sys, os, re, subprocess, datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# ==================== 配置 ====================
BLOG_DIR = r'd:\网站开发-json\blog'
INDEX_FILE = r'd:\网站开发-json\blog\index.html'
SITEMAP_FILE = r'd:\网站开发-json\sitemap.xml'
TODAY = datetime.date.today().strftime('%Y-%m-%d')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')

# ==================== 文章模板 ====================
def get_article_template():
    """返回新的博客文章内容 - 根据主题自动选择"""
    
    # 选择主题：基于当前日期和时间戳生成多样化主题
    topics = [
        {
            'slug': 'json-validator-debug-api-errors-faster',
            'title': 'JSON Validator: Debug API Errors Faster with Instant Validation',
            'category': 'Development',
            'category_class': 'cat-development',
            'description': 'Learn how a JSON validator helps you catch syntax errors, schema violations, and API integration issues before they become production bugs.',
            'keywords': 'JSON validator, validate JSON online, JSON syntax checker, JSON error detection, API debugging',
            'excerpt': 'A JSON validator is your first line of defense against data integration errors. Learn how to use validation to catch issues early, debug API responses, and ensure data quality.',
            'read_time': '6-8 min read',
            'content': '''
                <p class="lead">JSON validation is often an afterthought, but catching errors early saves hours of debugging. A good JSON validator can spot syntax errors, schema violations, and data quality issues before they reach production.</p>

                <h2>Why JSON Validation Matters</h2>
                <p>Every time your application receives JSON data from an API, database, or user input, there's a chance the data is malformed. Without validation, these errors propagate through your system:</p>
                <ul>
                    <li><strong>API Integration Failures</strong>: Third-party APIs may return unexpected data formats</li>
                    <li><strong>Database Corruption</strong>: Bad data saved to your database causes downstream issues</li>
                    <li><strong>Security Vulnerabilities</strong>: Invalid data can bypass input sanitization</li>
                    <li><strong>Silent Failures</strong>: Many JSON parsers fail silently, making bugs hard to trace</li>
                </ul>

                <h2>Common JSON Validation Errors</h2>
                <p>Understanding common errors helps you debug faster:</p>
                <pre class="code-block"><code>// Trailing commas - invalid in JSON
{ "name": "John", "age": 30, }

// Single quotes - must use double quotes
{ 'name': 'John', "age": 30 }

// Unquoted keys - must be strings
{ name: "John", "age": 30 }

// Comments - not allowed in JSON
{ "name": "John" /* comment */ }</code></pre>

                <h2>JSON Schema Validation</h2>
                <p>Beyond syntax, JSON Schema validates the structure and content of your data:</p>
                <pre class="code-block"><code>{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string", "minLength": 1 },
    "age": { "type": "integer", "minimum": 0 },
    "email": { "type": "string", "format": "email" }
  },
  "required": ["name", "email"]
}</code></pre>

                <h2>Real-World Validation Workflows</h2>
                <h3>1. API Response Validation</h3>
                <pre class="code-block"><code>// Validate API response against expected schema
const response = await fetch('/api/user/123');
const data = await response.json();

const valid = validate(data, userSchema);
if (!valid) {
    console.error('API response invalid:', validate.errors);
    // Alert monitoring system
}</code></pre>

                <h3>2. Request Body Validation</h3>
                <pre class="code-block"><code>// Validate before processing
app.post('/api/users', async (req, res) => {
    const { error } = userSchema.validate(req.body);
    if (error) {
        return res.status(400).json({
            error: 'Validation failed',
            details: error.details
        });
    }
    // Proceed with creating user
});</code></pre>

                <h2>Best Practices for JSON Validation</h2>
                <ul>
                    <li><strong>Validate at Boundaries</strong>: Check all external data (APIs, files, user input)</li>
                    <li><strong>Fail Fast</strong>: Reject invalid data immediately, don't let it propagate</li>
                    <li><strong>Provide Clear Errors</strong>: Show users exactly what's wrong and where</li>
                    <li><strong>Use Schema Validation</strong>: Define expected structure with JSON Schema</li>
                    <li><strong>Log Validation Failures</strong>: Track patterns to improve data quality</li>
                </ul>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>JSON validation catches errors before they cause downstream issues</li>
                    <li>Syntax validation checks JSON grammar; schema validation checks structure</li>
                    <li>Validate all external data sources: APIs, databases, user input</li>
                    <li>Use JSON Schema for reusable, documented validation rules</li>
                    <li>Provide actionable error messages to speed up debugging</li>
                </ul>
            '''
        },
        {
            'slug': 'json-path-vs-jsonata-choose-right-query-language',
            'title': 'JSONPath vs JSONata: Choosing the Right Query Language for Your Data',
            'category': 'Development',
            'category_class': 'cat-development',
            'description': 'Compare JSONPath and JSONata for querying JSON data. Learn when to use each syntax, their strengths, and practical examples for common use cases.',
            'keywords': 'JSONPath, JSONata, JSON query, JSONPath vs JSONata, extract JSON data, JSON manipulation',
            'excerpt': 'JSONPath and JSONata both let you query JSON, but they have different strengths. JSONPath is XPath-inspired and great for simple extraction. JSONata adds transformations, computations, and a more expressive syntax.',
            'read_time': '7-9 min read',
            'content': '''
                <p class="lead">When working with JSON data, you often need to extract specific values, filter arrays, or transform structures. Two popular query languages dominate this space: JSONPath and JSONata. Each has distinct philosophies and use cases.</p>

                <h2>What is JSONPath?</h2>
                <p>JSONPath is inspired by XPath and provides a syntax for traversing JSON structures. It uses dot and bracket notation similar to JavaScript:</p>
                <pre class="code-block"><code>$.store.book[0].title          // First book's title
$..author                     // All authors (recursive)
$.store.book[?(@.price < 10)] // Books under $10</code></pre>
                
                <h3>JSONPath in Different Languages</h3>
                <p>Most languages have JSONPath libraries:</p>
                <ul>
                    <li><strong>JavaScript</strong>: <code>jsonpath-plus</code>, <code>jsonpath</code></li>
                    <li><strong>Python</strong>: <code>jsonpath-ng</code>, <code>jsonpath-rw</code></li>
                    <li><strong>Go</strong>: <code>github.com/exp//jsonpath</code></li>
                    <li><strong>Java</strong>: <code>com.jayway.jsonpath</code></li>
                </ul>

                <h2>What is JSONata?</h2>
                <p>JSONata is a more powerful query and transformation language. Unlike JSONPath's extraction-focused approach, JSONata can transform data with built-in functions and operators:</p>
                <pre class="code-block"><code>$.store.book#$[price < 10].title     // Books under $10
$.store.book{ "title": title, "cheap": price < 10 }  // Transform structure
$sum($.orders[].total)              // Sum all order totals</code></pre>

                <h3>JSONata Features</h3>
                <ul>
                    <li><strong>Transformations</strong>: Reshape JSON into new structures</li>
                    <li><strong>Aggregations</strong>: Sum, average, count, min, max</li>
                    <li><strong>Functions</strong>: Built-in string, number, array functions</li>
                    <li><strong>Compositions</strong>: Chain operations elegantly</li>
                </ul>

                <h2>Head-to-Head Comparison</h2>
                <table class="comparison-table">
                    <thead><tr><th>Aspect</th><th>JSONPath</th><th>JSONata</th></tr></thead>
                    <tbody>
                        <tr><td>Purpose</td><td>Extraction</td><td>Extraction + Transformation</td></tr>
                        <tr><td>Syntax</td><td>XPath-inspired</td><td>Custom expressions</td></tr>
                        <tr><td>Built-in functions</td><td>Limited</td><td>Extensive</td></tr>
                        <tr><td>Aggregations</td><td>Manual</td><td>Native operators</td></tr>
                        <tr><td>Data reshaping</td><td>No</td><td>Yes</td></tr>
                        <tr><td>Learning curve</td><td>Low</td><td>Medium</td></tr>
                        <tr><td>Performance</td><td>Fast</td><td>Slightly slower</td></tr>
                    </tbody>
                </table>

                <h2>When to Use JSONPath</h2>
                <ul>
                    <li>Simple extraction: pulling specific fields from deeply nested structures</li>
                    <li>Filtering arrays based on conditions</li>
                    <li>When you need cross-language consistency</li>
                    <li>Performance-critical scenarios with large datasets</li>
                    <li>API response parsing where you just need specific values</li>
                </ul>

                <h3>JSONPath Example: API Response Parsing</h3>
                <pre class="code-block"><code>// Extract all product names from an e-commerce API response
const productNames = jsonPath(response, '$.data.products[*].name');

// Get all orders over $100
const highValueOrders = jsonPath(response, '$.orders[?(@.total > 100)]');</code></pre>

                <h2>When to Use JSONata</h2>
                <ul>
                    <li>Data transformation: reshaping JSON for different formats</li>
                    <li>Complex aggregations: sums, averages, grouping</li>
                    <li>Template-based generation: creating new JSON from existing data</li>
                    <li>Data validation with computed properties</li>
                    <li>When you need readable, expressive queries</li>
                </ul>

                <h3>JSONata Example: Data Transformation</h3>
                <pre class="code-block"><code>// Transform API response to a summary format
{
    "totalRevenue": $sum(orders.total),
    "orderCount": $count(orders),
    "topProducts": orders.products[$limit(3)],
    "generated": $now()
}</code></pre>

                <h2>Using Both Together</h2>
                <p>In practice, you might use both:</p>
                <pre class="code-block"><code>// JSONPath to extract the data
const rawData = jsonPath(apiResponse, '$.data');

// JSONata to transform it
const summary = jsonata(rawData, '{ total: $sum(items.price) }');</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li><strong>JSONPath</strong>: Best for simple, fast extraction across multiple languages</li>
                    <li><strong>JSONata</strong>: Best for transformations, aggregations, and expressive queries</li>
                    <li>Use JSONPath when you just need to pull values from complex JSON</li>
                    <li>Use JSONata when you need to reshape, compute, or generate new JSON</li>
                    <li>Consider using both: JSONPath for extraction, JSONata for transformation</li>
                    <li>For AI JSON tools, both query languages power the extraction and transformation features</li>
                </ul>
            '''
        },
        {
            'slug': 'json-performance-optimization-2026',
            'title': 'JSON Performance Optimization: 12 Techniques for Faster Parsing in 2026',
            'category': 'Performance',
            'category_class': 'cat-performance',
            'description': 'Learn 12 proven techniques to optimize JSON parsing performance. From streaming parsers to schema validation, these strategies will speed up your data processing.',
            'keywords': 'JSON performance, JSON parsing optimization, fast JSON parser, streaming JSON, JSON speed',
            'excerpt': 'JSON parsing can be a bottleneck in high-throughput applications. These 12 optimization techniques will help you process JSON data faster and more efficiently.',
            'read_time': '8-10 min read',
            'content': '''
                <p class="lead">JSON parsing is often a silent performance killer. When processing thousands of requests per second, milliseconds add up. These 12 techniques will dramatically improve your JSON processing speed.</p>

                <h2>1. Use Streaming Parsers for Large Payloads</h2>
                <p>Traditional JSON parsers load the entire document into memory. Streaming parsers process data incrementally:</p>
                <pre class="code-block"><code>// Node.js streaming JSON parser
import { JSONParser } from '@streamparser/json';

const parser = new JSONParser({
    onValue: (key, value, path) => {
        // Process each value as it's parsed
        console.log(`${path.join('.')}:`, value);
    }
});

fs.createReadStream('large.json').pipe(parser);</code></pre>

                <h2>2. Choose the Fastest Parser for Your Runtime</h2>
                <p>Benchmark results vary by runtime:</p>
                <ul>
                    <li><strong>Node.js</strong>: <code>simdjson</code>, <code>JSON.stream</code></li>
                    <li><strong>Python</strong>: <code>orjson</code> (2-3x faster than stdlib)</li>
                    <li><strong>Java</strong>: <code>jackson-core</code> with streaming API</li>
                    <li><strong>Go</strong>: <code>json-iterator</code> (drop-in replacement)</li>
                </ul>

                <h2>3. Validate Schema During Parse</h2>
                <p>Combining parsing and validation eliminates double processing:</p>
                <pre class="code-block"><code>// Fast schema validation with Ajv
import Ajv from 'ajv8';
const ajv = new Ajv({ allErrors: true });

// Compile schema once
const validate = ajv.compile(schema);

// Validate while parsing
const data = parseJSONWithValidation(jsonString, validate);</code></pre>

                <h2>4. Pre-parse Frequently Accessed Data</h2>
                <p>Cache parsed results for repeated access patterns:</p>
                <pre class="code-block"><code>// Pre-parse common access patterns
const userCache = new Map();
const cachedUser = userCache.get(userId) || parseAndCache(userId);

function parseAndCache(id) {
    const data = JSON.parse(apiResponse);
    userCache.set(id, {
        name: data.user.name,
        email: data.user.email,
        // Only store what you need
    });
    return userCache.get(id);
}</code></pre>

                <h2>5. Use TypedArrays for Numeric Data</h2>
                <p>When working with numeric-heavy JSON, TypedArrays are faster:</p>
                <pre class="code-block"><code>// Float64Array for numeric arrays
const buffer = new Float64Array(jsonData.values);

// Access is 10x faster than string parsing
for (let i = 0; i < buffer.length; i++) {
    sum += buffer[i];  // Direct memory access
}</code></pre>

                <h2>6. Lazy Parsing with Projection</h2>
                <p>Only parse the fields you need:</p>
                <pre class="code-block"><code>// Project only needed fields
const userProjection = {
    parse: (json) => {
        const doc = JSON.parse(json);
        return {
            id: doc.id,
            name: doc.profile.name,
            avatar: doc.profile.avatar.url
        };
    }
};</code></pre>

                <h2>7. Incremental Serialization</h2>
                <p>For building JSON, use incremental approaches:</p>
                <pre class="code-block"><code>// Streaming JSON builder
const builder = new JSONBuilder();
builder.startObject()
    .writeKey('users')
    .startArray();
    
for (const user of users) {
    builder.writeValue(formatUser(user));
}

builder.endArray().endObject();
const json = builder.build();</code></pre>

                <h2>8. Shared interned Strings</h2>
                <p>Repeated strings can be interned for memory savings:</p>
                <pre class="code-block"><code>// String interning for repeated values
const internPool = new Map();

function intern(str) {
    if (!internPool.has(str)) {
        internPool.set(str, str);
    }
    return internPool.get(str);
}

// "status": "active" uses same string object
const status = intern("active");</code></pre>

                <h2>9. Batch Processing with Worker Threads</h2>
                <p>Offload parsing to background threads:</p>
                <pre class="code-block"><code>// worker.js
import { parentPort } from 'worker_threads';

parentPort.on('message', ({ data }) => {
    const parsed = JSON.parse(data);
    parentPort.postMessage(processData(parsed));
});

// main.js
const worker = new Worker('./worker.js');
worker.postMessage({ data: largeJson });</code></pre>

                <h2>10. Compact Encoding for Storage</h2>
                <p>Consider more compact formats for storage:</p>
                <ul>
                    <li><strong>MessagePack</strong>: Binary JSON, ~30% smaller</li>
                    <li><strong>CBOR</strong>: IETF standard binary format</li>
                    <li><strong>Protobuf</strong>: Schema-based, best for repeated data</li>
                </ul>

                <h2>11. Gzip Compression for Transfer</h2>
                <p>Compress JSON during network transfer:</p>
                <pre class="code-block"><code>// Server-side compression
app.use(compression({ level: 6 }));

// Client-side decompression
const data = JSON.parse(pako.inflate(response, { to: 'string' }));</code></pre>

                <h2>12. Schema-based Code Generation</h2>
                <p>Generate typed parsers from schemas:</p>
                <pre class="code-block"><code>// Generate efficient parsers from JSON Schema
import { codegen } from 'json-schema-to-typescript';
const parserCode = codegen(schema);

// Compile generated code for maximum speed
const parser = new Function('return ' + parserCode)();</code></pre>

                <h2>Performance Comparison</h2>
                <table class="comparison-table">
                    <thead><tr><th>Technique</th><th>Speed Gain</th><th>Use Case</th></tr></thead>
                    <tbody>
                        <tr><td>simdjson</td><td>2-3x faster</td><td>All JSON parsing</td></tr>
                        <tr><td>Streaming parser</td><td>50% memory</td><td>Large files</td></tr>
                        <tr><td>TypedArrays</td><td>10x for numbers</td><td>Numeric data</td></tr>
                        <tr><td>Worker threads</td><td>Full CPU use</td><td>Batch processing</td></tr>
                        <tr><td>Schema projection</td><td>2-5x faster</td><td>Partial data</td></tr>
                    </tbody>
                </table>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Choose the right parser: simdjson for raw speed, streaming for memory efficiency</li>
                    <li>Combine parsing with validation to avoid double processing</li>
                    <li>Project only needed fields for partial data access</li>
                    <li>Use Worker threads to utilize all CPU cores</li>
                    <li>Consider binary formats for storage and internal transfer</li>
                    <li>Profile before optimizing — use benchmarks to guide your choices</li>
                </ul>
            '''
        },
        {
            'slug': 'json-schema-validation-complete-guide-2026',
            'title': 'JSON Schema Validation: The Complete Guide for API Developers in 2026',
            'category': 'API Design',
            'category_class': 'cat-api',
            'description': 'Master JSON Schema validation for REST APIs. Learn keywords, draft-2020-12 features, custom validators, and best practices for production APIs.',
            'keywords': 'JSON Schema, JSON validation, API validation, JSON Schema draft 2020-12, schema best practices',
            'excerpt': 'JSON Schema is the standard for validating JSON data structures. This guide covers everything from basic type checks to advanced composition patterns for production APIs.',
            'read_time': '9-11 min read',
            'content': '''
                <p class="lead">JSON Schema provides a powerful, declarative way to validate JSON data. Whether you are building REST APIs, processing configuration files, or validating form submissions, understanding JSON Schema is essential for any developer working with structured data.</p>

                <h2>Why JSON Schema Matters</h2>
                <p>Without validation, your API accepts anything — malformed payloads, missing fields, wrong data types. JSON Schema catches these problems at the boundary:</p>
                <ul>
                    <li><strong>Early error detection</strong>: Reject invalid data before it reaches business logic</li>
                    <li><strong>Self-documenting APIs</strong>: The schema itself describes expected data shapes</li>
                    <li><strong>Auto-generated forms</strong>: Frontend tools can build UI from schemas</li>
                    <li><strong>Contract testing</strong>: Verify that producers and consumers agree on data formats</li>
                </ul>

                <h2>Core Keywords You Need to Know</h2>
                <h3>Type Validation</h3>
                <pre class="code-block"><code>{
  "type": "object",
  "properties": {
    "name": { "type": "string", "minLength": 1, "maxLength": 100 },
    "age": { "type": "integer", "minimum": 0, "maximum": 150 },
    "email": { "type": "string", "format": "email" },
    "isActive": { "type": "boolean", "default": true },
    "score": { "type": "number", "exclusiveMinimum": 0 }
  },
  "required": ["name", "email"]
}</code></pre>

                <h3>Array Validation</h3>
                <pre class="code-block"><code>{
  "type": "array",
  "items": { "$ref": "#/$defs/product" },
  "minItems": 1,
  "maxItems": 100,
  "uniqueItems": true
}</code></pre>

                <h2>Advanced Composition Patterns</h2>
                <p>Draft-2020-12 introduced powerful composition keywords:</p>
                <pre class="code-block"><code>{
  "oneOf": [
    { "required": ["creditCard"] },
    { "required": ["paypalEmail"] },
    { "required": ["bankAccount"] }
  ],
  "properties": {
    "creditCard": { "$ref": "#/$defs/creditCard" },
    "paypalEmail": { "type": "string", "format": "email" },
    "bankAccount": { "$ref": "#/$defs/bankAccount" }
  }
}</code></pre>

                <h3>Composition Keywords Compared</h3>
                <table class="comparison-table">
                    <thead><tr><th>Keyword</th><th>Behavior</th><th>Use Case</th></tr></thead>
                    <tbody>
                        <tr><td><code>allOf</code></td><td>Must match ALL schemas</td><td>Combining required fields from multiple schemas</td></tr>
                        <tr><td><code>anyOf</code></td><td>Must match at least ONE</td><td>Flexible input formats (e.g., string or number ID)</td></tr>
                        <tr><td><code>oneOf</code></td><td>Must match EXACTLY one</td><td>Mutually exclusive payment methods</td></tr>
                        <tr><td><code>not</code></td><td>Must NOT match</td><td>Excluding specific values or patterns</td></tr>
                    </tbody>
                </table>

                <h2>Using $defs for Reusable Subschemas</h2>
                <pre class="code-block"><code>{
  "$defs": {
    "address": {
      "type": "object",
      "properties": {
        "street": { "type": "string" },
        "city": { "type": "string" },
        "zipCode": { "type": "string", "pattern": "^[0-9]{5}$" }
      },
      "required": ["street", "city"]
    },
    "customer": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "shipping": { "$ref": "#/$defs/address" },
        "billing": { "$ref": "#/$defs/address" }
      }
    }
  }
}</code></pre>

                <h2>Custom Validators and Formats</h2>
                <p>Built-in formats cover common cases, but you often need custom validation:</p>
                <pre class="code-block"><code>// Ajv custom format
ajv.addFormat('hex-color', '^#[0-9a-fA-F]{6}$');
ajv.addFormat('username', '^[a-zA-Z0-9_]{3,20}$');

// Custom keyword for cross-field validation
ajv.addKeyword({
  keyword: 'passwordMatch',
  type: 'object',
  validate: (schema, data) => data.password === data.confirmPassword
});</code></pre>

                <h2>Performance Tips</h2>
                <ul>
                    <li><strong>Compile once, validate many</strong>: Schema compilation is the expensive step</li>
                    <li><strong>Use <code>$ref</code> instead of deep nesting</strong>: References are resolved once at compile time</li>
                    <li><strong>Avoid heavy regex</strong>: Complex patterns slow down validation significantly</li>
                    <li><strong>Set <code>allErrors: false</code></strong>: Stop at the first error for faster validation</li>
                </ul>

                <h2>Best Practices for Production APIs</h2>
                <ul>
                    <li>Version your schemas alongside your API</li>
                    <li>Use <code>$id</code> for schema identification and cross-referencing</li>
                    <li>Provide clear <code>$comment</code> annotations for documentation</li>
                    <li>Write schemas for both request bodies and response bodies</li>
                    <li>Use strict mode (<code>additionalProperties: false</code>) to prevent unexpected fields</li>
                </ul>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>JSON Schema is the standard for validating JSON — use it instead of writing custom validators</li>
                    <li>Master composition keywords (allOf, anyOf, oneOf) for complex validation rules</li>
                    <li>Use $defs for reusable subschemas and keep your validation DRY</li>
                    <li>Compile schemas once and reuse the validator for best performance</li>
                    <li>Draft-2020-12 is the current standard — upgrade from draft-07 if you haven't</li>
                </ul>
            '''
        },
        {
            'slug': 'json-vs-xml-2026-when-to-use-each',
            'title': 'JSON vs XML in 2026: Which Format Should You Use?',
            'category': 'Comparison',
            'category_class': 'cat-development',
            'description': 'A practical comparison of JSON and XML in modern development. Learn when each format excels, migration strategies, and why JSON dominates APIs while XML still matters.',
            'keywords': 'JSON vs XML, JSON XML comparison, when to use JSON, when to use XML, data format comparison',
            'excerpt': 'The JSON vs XML debate is far from settled. While JSON dominates web APIs, XML remains essential in enterprise systems, configuration, and document formats. Here is when to use each.',
            'read_time': '7-9 min read',
            'content': '''
                <p class="lead">In 2026, JSON has become the default data format for web development, but XML is far from dead. Understanding when to use each format is a key skill for any developer building modern applications.</p>

                <h2>Where JSON Dominates</h2>
                <ul>
                    <li><strong>REST APIs</strong>: Over 95% of public REST APIs use JSON</li>
                    <li><strong>Configuration files</strong>: package.json, tsconfig.json, .eslintrc.json</li>
                    <li><strong>NoSQL databases</strong>: MongoDB, CouchDB store native JSON</li>
                    <li><strong>Real-time communication</strong>: WebSocket messages, Server-Sent Events</li>
                    <li><strong>AI/ML data</strong>: Training configurations, model metadata, prompt templates</li>
                </ul>

                <h2>Where XML Still Matters</h2>
                <ul>
                    <li><strong>SOAP web services</strong>: Enterprise systems, banking, healthcare</li>
                    <li><strong>Document formats</strong>: XHTML, SVG, MathML, RSS/Atom feeds</li>
                    <li><strong>Configuration</strong>: Spring Framework, Maven, Android layouts</li>
                    <li><strong>Legal and publishing</strong>: DOCX, EPUB, and XBRL are XML-based</li>
                    <li><strong>Telecom and aviation</strong>: Industry standards still rely on XML schemas</li>
                </ul>

                <h2>Technical Comparison</h2>
                <table class="comparison-table">
                    <thead><tr><th>Aspect</th><th>JSON</th><th>XML</th></tr></thead>
                    <tbody>
                        <tr><td>Syntax</td><td>Lightweight, minimal</td><td>Verbose, tag-based</td></tr>
                        <tr><td>Data types</td><td>Native (string, number, boolean, null)</td><td>Everything is a string</td></tr>
                        <tr><td>Comments</td><td>No native support</td><td>Yes (&lt;!-- comment --&gt;)</td></tr>
                        <tr><td>Namespaces</td><td>No</td><td>Yes (critical for enterprise)</td></tr>
                        <tr><td>Schema validation</td><td>JSON Schema</td><td>XSD (more mature)</td></tr>
                        <tr><td>Streaming</td><td>NDJSON, JSON streaming</td><td>SAX, StAX (very mature)</td></tr>
                        <tr><td>XPath-like queries</td><td>JSONPath, JSONata</td><td>XPath, XSLT</td></tr>
                        <tr><td>File size</td><td>~30% smaller</td><td>Larger due to tags</td></tr>
                        <tr><td>Parser speed</td><td>Faster</td><td>Slower (more complex)</td></tr>
                    </tbody>
                </table>

                <h2>Performance Benchmarks</h2>
                <p>For equivalent data structures:</p>
                <ul>
                    <li>JSON parsing is typically <strong>2-5x faster</strong> than XML</li>
                    <li>JSON payloads are <strong>20-40% smaller</strong> on the wire</li>
                    <li>Memory usage for JSON objects is <strong>30-50% lower</strong></li>
                    <li>Gzipped, the size difference narrows to <strong>10-15%</strong></li>
                </ul>

                <h2>When to Choose JSON</h2>
                <ul>
                    <li>Building REST APIs or GraphQL endpoints</li>
                    <li>Frontend-backend communication in web/mobile apps</li>
                    <li>Storing configuration for developer tools</li>
                    <li>IoT and embedded systems (lightweight parsing)</li>
                    <li>Any new project without legacy XML requirements</li>
                </ul>

                <h2>When to Choose XML</h2>
                <ul>
                    <li>Integrating with enterprise SOAP services</li>
                    <li>Working with document-centric data (publishing, legal)</li>
                    <li>Projects requiring mixed-content models (text + markup)</li>
                    <li>Industries with existing XML standards (healthcare HL7, finance FIXML)</li>
                    <li>When you need XSLT transformations</li>
                </ul>

                <h2>Migration Strategies</h2>
                <p>If you are migrating from XML to JSON:</p>
                <pre class="code-block"><code>// XML attributes become JSON properties
// &lt;user id="123" active="true"&gt;  →  { "id": "123", "active": true }

// XML namespaces need prefix conventions
// &lt;ns:price xmlns:ns="..."&gt;  →  { "ns:price": 19.99 }

// Mixed content requires careful handling
// &lt;p&gt;Hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;  →  { "html": "&lt;p&gt;Hello &lt;b&gt;world&lt;/b&gt;!&lt;/p&gt;" }</code></pre>

                <h2>The Bottom Line</h2>
                <p>JSON is the right default for most new projects. But XML is not going away — it powers critical infrastructure worldwide. The best developers know both and choose the right tool for each job.</p>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>JSON: Choose as the default for APIs, web apps, and configuration</li>
                    <li>XML: Still essential for enterprise integration, documents, and regulated industries</li>
                    <li>Performance gap favors JSON, but XML has richer validation and transformation tools</li>
                    <li>Many real-world systems use both — focus on clean conversion between formats</li>
                </ul>
            '''
        },
        {
            'slug': 'json-web-tokens-jwt-security-best-practices',
            'title': 'JWT Security Best Practices: Avoiding Common JSON Web Token Vulnerabilities',
            'category': 'Security',
            'category_class': 'cat-api',
            'description': 'Learn critical JWT security best practices. Understand common vulnerabilities like algorithm confusion, token theft, and how to implement secure authentication with JSON Web Tokens.',
            'keywords': 'JWT security, JSON Web Token, JWT best practices, token authentication, JWT vulnerabilities',
            'excerpt': 'JSON Web Tokens are everywhere, but misconfigured JWTs can expose your application to serious security vulnerabilities. These practices will help you implement JWT authentication securely.',
            'read_time': '8-10 min read',
            'content': '''
                <p class="lead">JSON Web Tokens (JWTs) are the backbone of modern stateless authentication. But their flexibility comes with risk — misconfigured JWTs are a top source of authentication bypasses and data leaks.</p>

                <h2>How JWTs Work</h2>
                <p>A JWT consists of three Base64URL-encoded parts separated by dots:</p>
                <pre class="code-block"><code>// Header: algorithm and token type
{ "alg": "RS256", "typ": "JWT" }

// Payload: claims (the actual data)
{ "sub": "user123", "exp": 1745635200, "role": "admin" }

// Signature: cryptographic proof of integrity
HMACSHA256(base64Url(header) + "." + base64Url(payload), secret)</code></pre>

                <h2>Common Vulnerabilities</h2>

                <h3>1. Algorithm Confusion Attack</h3>
                <p>Attackers change the header to <code>"alg": "none"</code> or switch from RS256 to HS256:</p>
                <pre class="code-block"><code>// Attack: Change algorithm to "none"
{ "alg": "none", "typ": "JWT" }.
{ "sub": "admin", "role": "superuser" }.
// Empty signature — server accepts it!</code></pre>
                <p><strong>Fix</strong>: Always explicitly whitelist allowed algorithms on the server.</p>

                <h3>2. Weak Signing Secrets</h3>
                <p>Using short or predictable secrets enables brute-force attacks:</p>
                <pre class="code-block"><code>// BAD: Weak secrets
const secret = "mySecret";          // Too short
const secret = "password123";       // Dictionary word

// GOOD: Strong secrets
const secret = crypto.randomBytes(64).toString('hex');
// Or use asymmetric keys (RS256) for better security</code></pre>

                <h3>3. Token Expiration Issues</h3>
                <ul>
                    <li>Missing <code>exp</code> claim → tokens valid forever</li>
                    <li>Setting <code>exp</code> in the past → broken auth</li>
                    <li>Very long expiration → larger attack window</li>
                </ul>

                <h2>Security Best Practices</h2>

                <h3>Token Storage</h3>
                <table class="comparison-table">
                    <thead><tr><th>Method</th><th>XSS Risk</th><th>CSRF Risk</th><th>Recommendation</th></tr></thead>
                    <tbody>
                        <tr><td>localStorage</td><td>High</td><td>Low</td><td>Not recommended</td></tr>
                        <tr><td>Cookie (no HttpOnly)</td><td>High</td><td>High</td><td>Never use</td></tr>
                        <tr><td>Cookie (HttpOnly + Secure)</td><td>Low</td><td>Medium</td><td>Recommended</td></tr>
                        <tr><td>In-memory + refresh token</td><td>Low</td><td>Low</td><td>Best for SPAs</td></tr>
                    </tbody>
                </table>

                <h3>Implementation Checklist</h3>
                <ul>
                    <li>✅ Use RS256 (asymmetric) for distributed systems, HS256 for monoliths</li>
                    <li>✅ Set short access token expiration (15-30 minutes)</li>
                    <li>✅ Use refresh tokens with rotation for long-lived sessions</li>
                    <li>✅ Validate all claims: <code>iss</code>, <code>aud</code>, <code>exp</code>, <code>nbf</code></li>
                    <li>✅ Include a unique <code>jti</code> (JWT ID) for token revocation</li>
                    <li>✅ Store tokens in HttpOnly, Secure, SameSite cookies</li>
                    <li>✅ Implement token blocklist for logout and revocation</li>
                </ul>

                <h3>Secure Implementation Example</h3>
                <pre class="code-block"><code>import jwt from 'jsonwebtoken';

// Verify token with strict validation
function verifyToken(token) {
    return jwt.verify(token, publicKey, {
        algorithms: ['RS256'],           // Whitelist algorithms
        issuer: 'https://api.myapp.com',
        audience: 'myapp-frontend',
        clockTolerance: 5,               // 5 second leeway
        maxAge: '30m'                    // Max age even if exp allows
    });
}

// Generate secure access token
function generateAccessToken(user) {
    return jwt.sign(
        {
            sub: user.id,
            role: user.role,
            jti: crypto.randomUUID()     // Unique token ID
        },
        privateKey,
        {
            algorithm: 'RS256',
            expiresIn: '15m',
            issuer: 'https://api.myapp.com',
            audience: 'myapp-frontend'
        }
    );
}</code></pre>

                <h2>Refresh Token Pattern</h2>
                <pre class="code-block"><code>// Access token: short-lived (15 min), stored in memory
// Refresh token: long-lived (7 days), stored in HttpOnly cookie

app.post('/auth/refresh', (req, res) => {
    const refreshToken = req.cookies.refresh_token;
    
    // Verify refresh token
    const payload = verifyRefreshToken(refreshToken);
    
    // Rotate: invalidate old, issue new
    revokeToken(refreshToken);
    const newAccess = generateAccessToken(payload.user);
    const newRefresh = generateRefreshToken(payload.user);
    
    res.cookie('refresh_token', newRefresh, {
        httpOnly: true,
        secure: true,
        sameSite: 'strict',
        maxAge: 7 * 24 * 60 * 60 * 1000
    });
    
    res.json({ access_token: newAccess });
});</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Always whitelist allowed algorithms — never trust the header</li>
                    <li>Use strong signing secrets (256-bit minimum for HS256)</li>
                    <li>Keep access tokens short-lived and use refresh token rotation</li>
                    <li>Store tokens in HttpOnly + Secure cookies, not localStorage</li>
                    <li>Validate all standard claims on every request</li>
                </ul>
            '''
        },
        {
            'slug': 'handling-large-json-files-streaming-parsing',
            'title': 'Handling Large JSON Files: Streaming, Chunking, and Memory-Efficient Processing',
            'category': 'Performance',
            'category_class': 'cat-performance',
            'description': 'Learn how to process large JSON files (GBs) without running out of memory. Covers streaming parsers, NDJSON, ijson, SAX-style processing, and practical examples in Python, JavaScript, and Go.',
            'keywords': 'large JSON files, JSON streaming, JSON parsing memory, NDJSON, ijson, process big JSON',
            'excerpt': 'When JSON files grow to hundreds of megabytes or gigabytes, standard parsers crash with out-of-memory errors. These streaming and chunking strategies let you process massive JSON files efficiently.',
            'read_time': '8-10 min read',
            'content': '''
                <p class="lead">A 2 GB JSON file will consume 4-6 GB of RAM when loaded into memory as a parsed object. For data pipelines, ETL jobs, and server applications, this is simply unacceptable. Streaming and incremental processing are the answer.</p>

                <h2>The Problem with Standard Parsers</h2>
                <pre class="code-block"><code>// BAD: Loads entire file into memory
const data = JSON.parse(fs.readFileSync('large-data.json'));
// 2 GB file → 4-6 GB RAM usage → process crashes

// BETTER: Read file as stream
const stream = fs.createReadStream('large-data.json');</code></pre>

                <h2>Strategy 1: NDJSON (Newline-Delimited JSON)</h2>
                <p>The simplest approach: store each record as a separate JSON line:</p>
                <pre class="code-block"><code>// Each line is a complete JSON object
{"id":1,"name":"Alice","score":95}
{"id":2,"name":"Bob","score":87}
{"id":3,"name":"Carol","score":92}

// Process line by line — constant memory
const rl = readline.createInterface({ input: fs.createReadStream('data.ndjson') });
for await (const line of rl) {
    const record = JSON.parse(line);
    processRecord(record);  // Only one record in memory
}</code></pre>

                <h2>Strategy 2: Streaming JSON Parsers</h2>

                <h3>JavaScript: <code>JSONStream</code></h3>
                <pre class="code-block"><code>const JSONStream = require('JSONStream');

// Stream-parse specific paths from large JSON
fs.createReadStream('huge-array.json')
    .pipe(JSONStream.parse('items.*'))
    .on('data', (item) => {
        // Process each item as it arrives
        processItem(item);
    });</code></pre>

                <h3>Python: <code>ijson</code></h3>
                <pre class="code-block"><code>import ijson

# Parse specific keys from large files
with open('large-data.json', 'rb') as f:
    for item in ijson.items(f, 'users.item'):
        process_user(item)  # One user at a time

# Parse lazily with ijson
for prefix, event, value in ijson.parse(open('data.json', 'rb')):
    if prefix == 'results.item.name':
        print(value)</code></pre>

                <h3>Go: <code>json.Decoder</code></h3>
                <pre class="code-block"><code>file, _ := os.Open("large-data.json")
defer file.Close()
decoder := json.NewDecoder(file)

// Read opening bracket
t, _ := decoder.Token() // "["

// Decode items one at a time
for decoder.More() {
    var item Item
    decoder.Decode(&item)
    processItem(item)
}</code></pre>

                <h2>Strategy 3: SAX-Style Event Parsing</h2>
                <pre class="code-block"><code>import { JSONParser } from '@streamparser/json';

const parser = new JSONParser();
parser.onValue = ({ value, key, parent, stack }) => {
    // Called for every value in the JSON
    if (stack.length > 0 && stack[stack.length - 1].key === 'email') {
        console.log('Found email:', value);
    }
};

fs.createReadStream('users.json').pipe(parser);</code></pre>

                <h2>Strategy 4: File Chunking</h2>
                <p>Split large files into smaller chunks for parallel processing:</p>
                <pre class="code-block"><code># Python: Split NDJSON into chunks
import os

def split_ndjson(input_path, chunk_size=10000):
    chunk = []
    part = 0
    with open(input_path) as f:
        for line in f:
            chunk.append(line)
            if len(chunk) >= chunk_size:
                with open(f'part_{part}.ndjson', 'w') as out:
                    out.writelines(chunk)
                chunk = []
                part += 1

# Process chunks in parallel using multiprocessing
from multiprocessing import Pool
with Pool(4) as p:
    results = p.map(process_chunk, glob('part_*.ndjson'))</code></pre>

                <h2>Memory Comparison</h2>
                <table class="comparison-table">
                    <thead><tr><th>Method</th><th>Memory Usage</th><th>Speed</th><th>Best For</th></tr></thead>
                    <tbody>
                        <tr><td>JSON.parse()</td><td>Full file size × 2-3x</td><td>Fastest</td><td>Small files (&lt;100 MB)</td></tr>
                        <tr><td>NDJSON line-by-line</td><td>Single record</td><td>Fast</td><td>Record-oriented data</td></tr>
                        <tr><td>Streaming parser</td><td>Single node</td><td>Medium</td><td>Large nested objects</td></tr>
                        <tr><td>Event-based (SAX)</td><td>Minimal</td><td>Slower</td><td>Extracting specific fields</td></tr>
                        <tr><td>File chunking + parallel</td><td>Chunk size per worker</td><td>Fastest for big data</td><td>Batch processing pipelines</td></tr>
                    </tbody>
                </table>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Never load multi-hundred-MB JSON files with standard parsers</li>
                    <li>NDJSON is the simplest streaming format — use it for new data pipelines</li>
                    <li>Use ijson (Python), JSONStream (Node.js), or json.Decoder (Go) for existing files</li>
                    <li>Chunk files and process in parallel for maximum throughput</li>
                    <li>Profile memory usage — tools like <code>memory_profiler</code> help identify bottlenecks</li>
                </ul>
            '''
        }
    ]
    
    # 基于日期选择主题（顺序选取，自动跳过已存在文章）
    day_of_year = datetime.date.today().timetuple().tm_yday
    start_index = day_of_year % len(topics)
    # 遍历寻找第一个未生成的主题
    for offset in range(len(topics)):
        candidate = topics[(start_index + offset) % len(topics)]
        article_dir = os.path.join(BLOG_DIR, candidate['slug'])
        if not os.path.exists(article_dir):
            return candidate
    # 全部已生成，返回最近一个（会覆盖）
    return topics[start_index]

# ==================== 生成文章 ====================
def generate_article():
    """生成新文章"""
    article = get_article_template()
    article_dir = os.path.join(BLOG_DIR, article['slug'])
    
    # 创建文章目录
    os.makedirs(article_dir, exist_ok=True)
    
    article_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Bq7rq6iKPPDtIQCMjYquCng3eeVG_Ni0tf1bqUQsQ2w" />
    <meta name="description" content="{article['description']}">
    <meta name="keywords" content="{article['keywords']}">
    <meta name="author" content="AI JSON - Free JSON Tools for Developers">
    <meta name="robots" content="index, follow">

    <title>{article['title']} | AI JSON</title>
    <link rel="canonical" href="https://www.aijsons.com/blog/{article['slug']}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.aijsons.com/blog/{article['slug']}">
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['description']}">
    <meta property="og:image" content="https://www.aijsons.com/og-image.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{article['title']}">
    <meta name="twitter:description" content="{article['description']}">
    <meta name="twitter:image" content="https://www.aijsons.com/og-image.png">

    <meta property="article:published_time" content="{TODAY}">
    <meta property="article:section" content="{article['category']}">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">

    <!-- Styles -->
    <link rel="stylesheet" href="/css/styles.css">

    <!-- JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{article['title']}",
        "description": "{article['description']}",
        "datePublished": "{TODAY}",
        "author": {{"@type": "Organization", "name": "AI JSON"}},
        "publisher": {{"@type": "Organization", "name": "AI JSON", "url": "https://www.aijsons.com"}},
        "url": "https://www.aijsons.com/blog/{article['slug']}",
        "articleSection": "{article['category']}"
    }}
    </script>
</head>
<body>
    <!-- NAVBAR -->
    <div id="navbar-placeholder"></div>

    <main class="main-container">
        <article>
            <div class="article-header">
                <div class="breadcrumb">
                    <a href="/">Home</a> / <a href="/blog">Blog</a> / <span>Article</span>
                </div>
                <div class="article-category {article['category_class']}">{article['category']}</div>
                <h1 class="article-title">{article['title']}</h1>
                <div class="article-meta">
                    <span>Published: {TODAY}</span> · <span>{article['read_time']}</span>
                </div>
            </div>

            <div class="article-body">
                {article['content']}
            </div>
        </article>

        <section class="related-tools-section">
            <h2>Try Our JSON Tools</h2>
            <div class="related-tools-grid">
                <a href="/tools/json-formatter" class="related-tool-card">
                    <strong>JSON Formatter</strong>
                    <span>Format and validate JSON</span>
                </a>
                <a href="/tools/json-viewer" class="related-tool-card">
                    <strong>JSON Viewer</strong>
                    <span>Visualize JSON as tree</span>
                </a>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <p>AI JSON - Free JSON Tools for Developers</p>
        <p class="text-sm mt-sm">
            <a href="/about">About</a> | <a href="/changelog">Changelog</a> | <a href="/">Home</a>
        </p>
    </footer>
    
    <script src="/js/navbar.js"></script>
</body>
</html>'''

    index_path = os.path.join(article_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(article_html)
    
    print(f'✓ Created article: {article["slug"]}')
    return article

# ==================== 更新博客索引 ====================
def update_blog_index(new_article):
    """更新 blog/index.html 添加新文章"""
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建新文章的 HTML 卡片
    new_card = f'''<article class="article-card">
                    <div class="article-category {new_article['category_class']}">{new_article['category']}</div>
                    <h3><a href="/blog/{new_article['slug']}">{new_article['title']}</a></h3>
                    <p class="article-excerpt">{new_article['excerpt']}</p>
                    <div class="article-meta">
                        <span>{TODAY}</span> |
                        <span>{new_article['read_time']}</span>
                    </div>
                    <a href="/blog/{new_article['slug']}" class="read-more">Read the {new_article['category'].lower()} guide →</a>
                </article>'''
    
    # 更新 Featured Article 部分
    featured_pattern = r'(<section class="featured-section">.*?<article class="article-card featured-article">.*?<div class="article-category )[a-z-]+("\>' + new_article['category_class'] + r'\>(.*?<h2><a href=")[^"]+("[^>]*>)[^<]+(</a></h2>.*?<p class="article-excerpt">)[^<]+'
    
    # 直接替换 Featured Article
    featured_section = f'''<section class="featured-section">
            <h2 class="section-title">Latest Article</h2>
            <article class="article-card featured-article">
                <div class="article-category {new_article['category_class']}">{new_article['category']}</div>
                <h2><a href="/blog/{new_article['slug']}">{new_article['title']}</a></h2>
                <p class="article-excerpt">{new_article['excerpt']}</p>
                <div class="article-meta">
                    <span>{TODAY}</span> |
                    <span>{new_article['read_time']}</span>
                </div>
                <a href="/blog/{new_article['slug']}" class="read-more">Read the complete guide →</a>
            </article>
        </section>'''
    
    # 用正则替换 featured section
    import re
    content = re.sub(r'<section class="featured-section">.*?</section>', featured_section, content, flags=re.DOTALL)
    
    # 在文章网格顶部添加新文章卡片
    # 找到第一个 <article class="article-card"> 并在其后添加新卡片
    article_card_pattern = r'(<section>.*?<div class="articles-grid">)(\s*)(<article class="article-card">)'
    
    def add_new_card(match):
        return match.group(1) + match.group(2) + new_card + '\n                ' + match.group(2) + match.group(3)
    
    content = re.sub(article_card_pattern, add_new_card, content, count=1)
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ Updated blog index: {INDEX_FILE}')

# ==================== 更新 sitemap.xml ====================
def update_sitemap(slug):
    """将新文章添加到 sitemap.xml"""
    with open(SITEMAP_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    loc_url = f'https://www.aijsons.com/blog/{slug}'
    if loc_url in content:
        print(f'  ~ Already in sitemap: {slug}')
        return

    new_entry = f'''
  <url>
    <loc>{loc_url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>'''
    content = content.replace('</urlset>', new_entry + '\n</urlset>')
    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ Added to sitemap: {slug}')

# ==================== GitHub 推送 ====================
def push_to_github(commit_msg):
    """推送到 GitHub"""
    if not GITHUB_TOKEN:
        print('⚠ GITHUB_TOKEN not set, skipping GitHub push')
        return
    
    try:
        # 使用已有的 push_to_github.py 脚本
        script = r'd:\网站开发-json\scripts\push_to_github.py'
        result = subprocess.run(
            [r'C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe', 
             script, commit_msg],
            capture_output=True,
            text=True,
            cwd=r'd:\网站开发-json'
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f'⚠ GitHub push failed: {e}')

# ==================== 主流程 ====================
def main():
    print('=' * 50)
    print('Daily Blog Update - AI JSON')
    print(f'Date: {TODAY}')
    print('=' * 50)
    
    # 1. 生成新文章
    print('\n[1/4] Generating new article...')
    new_article = generate_article()
    
    # 2. 更新博客索引
    print('\n[2/4] Updating blog index...')
    update_blog_index(new_article)
    
    # 3. 更新 sitemap
    print('\n[3/4] Updating sitemap...')
    update_sitemap(new_article['slug'])
    
    # 4. 推送到 GitHub
    print('\n[4/4] Pushing to GitHub...')
    commit_msg = f'Blog: Add new article - {new_article["title"]}'
    push_to_github(commit_msg)
    
    print('\n' + '=' * 50)
    print('✓ Daily blog update completed!')
    print(f'  Article: https://www.aijsons.com/blog/{new_article["slug"]}')
    print('=' * 50)

if __name__ == '__main__':
    main()
