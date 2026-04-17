# -*- coding: utf-8 -*-
"""
Daily Blog Automation Script
Generates and publishes a new blog article daily for SEO purposes.
"""
import os
import re
import json
import hashlib
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURATION
# ============================================================================
BLOG_ARTICLE_TOPICS = [
    {
        "theme": "JSON Schema Evolution",
        "title": "JSON Schema 2024+: The New Features That Will Transform API Validation",
        "description": "JSON Schema has evolved significantly in recent years. This guide explores the latest Draft 2020-12 features including $defs, $anchor, and the new vocabulary system. Perfect for developers building robust API validation layers.",
        "keywords": ["JSON Schema", "API validation", "OpenAPI", "Draft 2020-12"]
    },
    {
        "theme": "LLM JSON Output",
        "title": "Getting Reliable JSON from LLMs: Prompt Engineering for Structured Outputs",
        "description": "Large Language Models can generate JSON, but getting consistent, valid structures requires careful prompt design. This guide covers chain-of-thought prompting, few-shot examples, and output validation techniques.",
        "keywords": ["LLM", "prompt engineering", "structured output", "JSON parsing"]
    },
    {
        "theme": "Performance Benchmark",
        "title": "JSON Parsing Performance: Comparing Native vs Library Implementations in 2024",
        "description": "Benchmark results comparing JSON parsing speeds across Python, JavaScript, Rust, and Go. Learn which libraries offer the best performance for high-throughput API services.",
        "keywords": ["performance", "benchmark", "JSON parsing", "Rust", "Go"]
    },
    {
        "theme": "Streaming JSON",
        "title": "Stream JSON Data Efficiently: Handling Large Payloads Without Memory Issues",
        "description": "Traditional JSON parsing loads entire documents into memory. Stream parsing allows processing of massive JSON files with minimal memory footprint. Perfect for log processing and data pipelines.",
        "keywords": ["streaming", "NDJSON", "JSON lines", "data pipeline"]
    },
    {
        "theme": "GraphQL vs REST JSON",
        "title": "GraphQL vs REST: When to Use Each for JSON API Design",
        "description": "REST and GraphQL handle JSON differently. REST returns fixed structures while GraphQL lets clients specify exact data needs. Understanding trade-offs helps architects choose the right approach.",
        "keywords": ["GraphQL", "REST API", "API design", "data fetching"]
    },
    {
        "theme": "Security Best Practices",
        "title": "JSON Security: Preventing Injection Attacks and Data Exfiltration",
        "description": "Improper JSON handling can lead to security vulnerabilities. Learn about JSON injection, prototype pollution, and best practices for safe JSON processing in web applications.",
        "keywords": ["security", "injection", "prototype pollution", "XSS"]
    },
    {
        "theme": "JSON in Databases",
        "title": "PostgreSQL JSONB vs MongoDB: Choosing the Right Document Store",
        "description": "Modern databases offer JSON storage with different trade-offs. PostgreSQL's JSONB provides ACID compliance while MongoDB offers flexible schemas. Compare indexing, querying, and performance.",
        "keywords": ["PostgreSQL", "MongoDB", "NoSQL", "database design"]
    },
    {
        "theme": "MCP Protocol",
        "title": "Model Context Protocol (MCP): The Emerging Standard for AI Tool Integration",
        "description": "MCP is becoming the universal protocol for AI agents to interact with external tools. Built on JSON-RPC, it provides a standardized way for AI systems to call functions and access data sources.",
        "keywords": ["MCP", "AI agents", "JSON-RPC", "tool calling"]
    },
    {
        "theme": "JSON Generation Patterns",
        "title": "10 Patterns for Generating JSON: From Simple Objects to Complex Hierarchies",
        "description": "Explore proven patterns for JSON generation: factory methods, builder patterns, serialization strategies, and polymorphic types. Includes practical examples in TypeScript and Python.",
        "keywords": ["patterns", "TypeScript", "Python", "serialization"]
    },
    {
        "theme": "API Error Handling",
        "title": "Error Response Design: Why RFC 9457 Problem Details Matters for Your API",
        "description": "RFC 9457 standardizes error responses with machine-readable details. Implementing it improves API usability and debugging. Examples from Stripe, Twilio, and AWS show best practices.",
        "keywords": ["RFC 9457", "error handling", "API design", "Problem Details"]
    },
    {
        "theme": "Streaming Responses",
        "title": "Server-Sent Events vs WebSocket vs Polling: JSON Data Delivery Patterns",
        "description": "Real-time JSON data delivery requires choosing the right protocol. SSE offers simplicity, WebSocket provides bidirectional communication, and polling ensures compatibility. Learn when to use each.",
        "keywords": ["SSE", "WebSocket", "real-time", "polling"]
    },
    {
        "theme": "JSON Schema to Code",
        "title": "From JSON Schema to TypeScript Types: Automated Type Generation Workflows",
        "description": "Manual type maintenance leads to bugs. Learn to generate TypeScript interfaces, Zod schemas, and API clients automatically from JSON Schema definitions. Boost type safety without manual work.",
        "keywords": ["TypeScript", "JSON Schema", "type generation", "Zod"]
    },
    {
        "theme": "Log Aggregation",
        "title": "JSON Logging Best Practices: Structured Logs for Modern Observability",
        "description": "Structured JSON logs enable powerful search and analysis. Learn to implement correlation IDs, distributed tracing, and ELK stack integration for production observability.",
        "keywords": ["logging", "observability", "ELK stack", "distributed tracing"]
    },
    {
        "theme": "CDN Edge JSON",
        "title": "JSON at the Edge: Caching Strategies for API Responses",
        "description": "Edge caching transforms JSON API performance. Explore cache-control strategies, surrogate keys, and edge computing patterns for global low-latency JSON delivery.",
        "keywords": ["CDN", "edge computing", "caching", "Cloudflare"]
    },
    {
        "theme": "Migration Patterns",
        "title": "JSON Schema Migration: Evolving APIs Without Breaking Clients",
        "description": "API evolution requires careful schema versioning. Learn additive-only changes, nullable fields, and discriminator patterns that let you extend APIs while maintaining backward compatibility.",
        "keywords": ["versioning", "API evolution", "backward compatibility"]
    }
]

# ============================================================================
# FILE PATHS
# ============================================================================
PROJECT_ROOT = r'd:\网站开发-json'
BLOG_PATH = os.path.join(PROJECT_ROOT, 'pages', 'blog.html')
INDEX_PATH = os.path.join(PROJECT_ROOT, 'index.html')
PUSH_SCRIPT = os.path.join(PROJECT_ROOT, 'scripts', 'push_to_github.py')

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_date_id():
    """Get today's date ID in YYYYMMDD format with optional letter suffix."""
    today = datetime.now()
    date_id = today.strftime('%Y%m%d')
    return date_id

def get_display_date():
    """Get today's date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')

def generate_article_content(topic, date_id):
    """Generate complete article HTML content."""
    title = topic['title']
    description = topic['description']
    theme = topic['theme']
    
    # Generate SVG diagram based on theme
    diagram = generate_theme_diagram(theme)
    
    # Generate rich content
    content = generate_article_body(theme, title)
    
    article = f'''<article id="ai-daily-{date_id}">
    <h3>{title}</h3>
    <p><strong>Published:</strong> {get_display_date()} | <strong>Reading time:</strong> 5-7 minutes | <strong>Target:</strong> US & Canada Developers</p>
    <div class="article-content">
        <div class="article-diagram">
            {diagram}
        </div>
        <p>{description}</p>
        {content}
        <h4>Key Takeaways</h4>
        <ul>
            <li>Structured JSON data enables better API contracts and documentation</li>
            <li>Client-side processing ensures data privacy and reduces server load</li>
            <li>Modern development workflows benefit from JSON's ubiquity and tooling</li>
        </ul>
    </div>
</article>
'''
    return article

def generate_theme_diagram(theme):
    """Generate appropriate SVG diagram based on article theme."""
    diagrams = {
        "JSON Schema Evolution": '''
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="20" width="360" height="160" rx="8" fill="#1f2940" stroke="#22C55E" stroke-width="2"/>
    <text x="200" y="50" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="14" font-weight="bold">JSON Schema Evolution</text>
    <g transform="translate(40, 70)">
        <rect x="0" y="0" width="100" height="40" rx="4" fill="#2a3654"/>
        <text x="50" y="25" text-anchor="middle" fill="#94A3B8" font-family="Arial" font-size="11">Draft-04</text>
        <line x1="100" y1="20" x2="120" y2="20" stroke="#22C55E" stroke-width="2" marker-end="url(#arrow)"/>
        <rect x="120" y="0" width="100" height="40" rx="4" fill="#2a3654"/>
        <text x="170" y="25" text-anchor="middle" fill="#94A3B8" font-family="Arial" font-size="11">Draft-06</text>
        <line x1="220" y1="20" x2="240" y2="20" stroke="#22C55E" stroke-width="2"/>
        <rect x="240" y="0" width="100" height="40" rx="4" fill="#22C55E"/>
        <text x="290" y="25" text-anchor="middle" fill="#0a0f1a" font-family="Arial" font-size="11" font-weight="bold">2020-12</text>
    </g>
    <g transform="translate(40, 130)">
        <text x="0" y="15" fill="#94A3B8" font-family="Arial" font-size="10">$ref reuse</text>
        <text x="90" y="15" fill="#94A3B8" font-family="Arial" font-size="10">Dynamic refs</text>
        <text x="190" y="15" fill="#F8FAFC" font-family="Arial" font-size="10" font-weight="bold">$defs, $anchor, vocabularies</text>
    </g>
    <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#22C55E"/></marker></defs>
</svg>''',
        "LLM JSON Output": '''
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="20" width="360" height="160" rx="8" fill="#1f2940" stroke="#22C55E" stroke-width="2"/>
    <text x="200" y="50" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="14" font-weight="bold">LLM JSON Generation Pipeline</text>
    <g transform="translate(50, 70)">
        <rect x="0" y="0" width="80" height="50" rx="4" fill="#2a3654" stroke="#94A3B8" stroke-width="1"/>
        <text x="40" y="28" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="10">Prompt</text>
        <line x1="80" y1="25" x2="110" y2="25" stroke="#22C55E" stroke-width="2"/>
        <rect x="110" y="0" width="80" height="50" rx="4" fill="#2a3654" stroke="#94A3B8" stroke-width="1"/>
        <text x="150" y="28" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="10">LLM</text>
        <line x1="190" y1="25" x2="220" y2="25" stroke="#22C55E" stroke-width="2"/>
        <rect x="220" y="0" width="80" height="50" rx="4" fill="#2a3654" stroke="#94A3B8" stroke-width="1"/>
        <text x="260" y="28" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="10">JSON</text>
        <line x1="300" y1="25" x2="330" y2="25" stroke="#22C55E" stroke-width="2"/>
        <rect x="330" y="0" width="30" height="50" rx="4" fill="#dc2626"/>
        <text x="345" y="28" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="10">?</text>
    </g>
    <g transform="translate(50, 140)">
        <text x="0" y="10" fill="#94A3B8" font-family="Arial" font-size="10">Chain-of-thought</text>
        <text x="110" y="10" fill="#94A3B8" font-family="Arial" font-size="10">Structured output</text>
        <text x="220" y="10" fill="#94A3B8" font-family="Arial" font-size="10">Validation</text>
        <text x="310" y="10" fill="#dc2626" font-family="Arial" font-size="10">Retry</text>
    </g>
</svg>''',
        "default": '''
<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="20" width="360" height="80" rx="8" fill="#1f2940" stroke="#22C55E" stroke-width="2"/>
    <text x="200" y="55" text-anchor="middle" fill="#F8FAFC" font-family="Arial" font-size="14" font-weight="bold">JSON Workflow</text>
    <text x="200" y="80" text-anchor="middle" fill="#94A3B8" font-family="Arial" font-size="12">Format → Validate → Process → Export</text>
</svg>'''
    }
    return diagrams.get(theme, diagrams['default'])

def generate_article_body(theme, title):
    """Generate main article body content based on theme."""
    return f'''
<p>In the rapidly evolving landscape of modern web development, {theme.lower()} has become an essential skill for developers building production-grade applications. This article explores key concepts, best practices, and practical implementation strategies.</p>

<h4>Understanding the Fundamentals</h4>
<p>When working with JSON in production environments, developers face common challenges that require thoughtful solutions. Whether you're building REST APIs, processing webhook payloads, or handling real-time data streams, understanding {theme.lower()} is crucial for maintaining clean, maintainable code.</p>

<h4>Practical Implementation</h4>
<p>Modern development workflows benefit from tools that handle JSON processing efficiently. AI JSON provides browser-based utilities that work entirely client-side, ensuring your data never leaves your machine while providing the formatting, validation, and conversion capabilities you need.</p>

<pre><code>{{
  "example": "structured_data",
  "tools": ["formatter", "validator", "converter"],
  "benefits": {{
    "speed": "instant_processing",
    "privacy": "client_side_only",
    "compatibility": "all_browsers"
  }}
}}</code></pre>

<h4>Industry Best Practices</h4>
<p>Leading companies like Stripe, Twilio, and GitHub have established patterns for JSON API design that balance flexibility with predictability. Following these patterns helps teams build APIs that are both developer-friendly and robust against edge cases.</p>

<h4>Performance Considerations</h4>
<p>When processing large JSON payloads, performance becomes critical. Modern JavaScript engines have optimized JSON parsing significantly, but understanding when to use streaming approaches versus batch processing can make the difference between a responsive application and one that freezes during data processing.</p>
'''

def update_blog_html(article_html, date_id):
    """Update blog.html with new article at the top."""
    with open(BLOG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the position after the blog header and before the first article
    # Look for the first <article tag
    first_article_pos = content.find('<article')
    
    if first_article_pos < 0:
        print("ERROR: Could not find article insertion point in blog.html")
        return False
    
    # Insert new article before the first existing article
    new_content = content[:first_article_pos] + article_html + '\n\n' + content[first_article_pos:]
    
    with open(BLOG_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"[OK] Updated blog.html with article ai-daily-{date_id}")
    return True

def update_index_html(title, description, date_id):
    """Update index.html homepage with new article card."""
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create new article card HTML
    new_card = f'''<article class="feature-card" style="text-align: left;">
    <span style="font-size: 0.8rem; color: var(--text-secondary);">{get_display_date()}</span>
    <h3 style="font-size: 1.125rem; margin-bottom: 0.5rem; color: var(--primary);">{title}</h3>
    <p style="color: var(--text-secondary); font-size: 0.95rem;">{description}</p>
    <a href="pages/blog.html#ai-daily-{date_id}" style="display: inline-block; margin-top: 0.75rem; color: var(--primary); font-weight: 500;">Read more →</a>
</article>'''
    
    # Find the Latest Articles section
    articles_start = content.find('<section class="tool-area mt-lg">', content.find('Latest Articles'))
    if articles_start < 0:
        # Try alternative pattern
        articles_start = content.find('class="feature-grid">', content.find('Latest Articles'))
    
    if articles_start < 0:
        print("WARNING: Could not find article insertion point in index.html")
        return False
    
    # Find the closing </div> for the feature-grid
    grid_start = content.find('<div class="feature-grid">', articles_start)
    if grid_start < 0:
        grid_start = content.find('<div class="feature-grid"', articles_start)
    
    if grid_start < 0:
        print("WARNING: Could not find feature-grid in index.html")
        return False
    
    # Insert new card after the opening <div class="feature-grid">
    grid_open_end = content.find('>', grid_start) + 1
    new_content = content[:grid_open_end] + '\n    ' + new_card + content[grid_open_end:]
    
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"[OK] Updated index.html with article card for ai-daily-{date_id}")
    return True

def push_to_github(commit_message):
    """Push changes to GitHub if token is available."""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("WARNING: GITHUB_TOKEN not set, skipping GitHub push")
        return False
    
    try:
        import subprocess
        result = subprocess.run(
            ['python', PUSH_SCRIPT, commit_message],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        if result.returncode == 0:
            print("[OK] Pushed to GitHub")
            return True
        else:
            print(f"[FAIL] GitHub push failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"[FAIL] GitHub push error: {e}")
        return False

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("=" * 60)
    print("Daily Blog Automation - AIJSON")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Get today's date ID
    date_id = get_date_id()
    
    # Select topic based on day of year (rotating through topics)
    day_of_year = datetime.now().timetuple().tm_yday
    topic_index = day_of_year % len(BLOG_ARTICLE_TOPICS)
    topic = BLOG_ARTICLE_TOPICS[topic_index]
    
    print(f"\nSelected Topic: {topic['theme']}")
    print(f"Article ID: ai-daily-{date_id}")
    
    # Generate article
    article_html = generate_article_content(topic, date_id)
    
    # Update files
    print("\nUpdating files...")
    blog_updated = update_blog_html(article_html, date_id)
    index_updated = update_index_html(topic['title'], topic['description'], date_id)
    
    if not blog_updated or not index_updated:
        print("\n[FAIL] Failed to update files")
        return 1
    
    # Commit message
    commit_msg = f"Daily blog: {topic['title']} (ai-daily-{date_id})"
    
    # Push to GitHub
    print("\nAttempting GitHub push...")
    push_to_github(commit_msg)
    
    print("\n" + "=" * 60)
    print("[OK] Daily blog update completed!")
    print("=" * 60)
    return 0

if __name__ == '__main__':
    exit(main())
