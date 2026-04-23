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
TODAY = datetime.date.today().strftime('%Y-%m-%d')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')

# ==================== 文章模板 ====================
def get_article_template():
    """返回新的博客文章内容 - 根据主题自动选择"""
    
    # 选择主题：基于当前日期和时间戳生成多样化主题
    topics = [
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
        }
    ]
    
    # 基于日期选择主题
    index = int(datetime.datetime.now().strftime('%H')) % len(topics)
    return topics[index]

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
    print('\n[1/3] Generating new article...')
    new_article = generate_article()
    
    # 2. 更新博客索引
    print('\n[2/3] Updating blog index...')
    update_blog_index(new_article)
    
    # 3. 推送到 GitHub
    print('\n[3/3] Pushing to GitHub...')
    commit_msg = f'Blog: Add new article - {new_article["title"]}'
    push_to_github(commit_msg)
    
    print('\n' + '=' * 50)
    print('✓ Daily blog update completed!')
    print(f'  Article: https://www.aijsons.com/blog/{new_article["slug"]}')
    print('=' * 50)

if __name__ == '__main__':
    main()
