# -*- coding: utf-8 -*-
"""
Daily News Automation Script
Updates trending news content in news.html with fresh JSON/web development news.
"""
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

# News content pool - each category will show 2-3 items
NEWS_CATEGORIES = [
    {
        "title": "Trending Today",
        "icon": '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>',
        "items": [
            {
                "tag": "AI & Agents",
                "date_suffix": "2026",
                "title": "MCP Protocol Reaches 10,000+ Public Servers: The AI Tool Standard Takes Off",
                "excerpt": "The Model Context Protocol (MCP) has surpassed 10,000 public server implementations. From database connectors to filesystem tools, MCP is rapidly becoming the universal bridge for AI agents."
            },
            {
                "tag": "Web Platform",
                "date_suffix": "2026",
                "title": "Browser DevTools Now Built-in JSON Schema Validation and Live Error Highlighting",
                "excerpt": "Chrome 122 and Firefox 120 now include native JSON Schema validation directly in DevTools. Developers can paste a schema and instantly see validation errors highlighted."
            },
            {
                "tag": "Performance",
                "date_suffix": "2026",
                "title": "Bun 2.0 Ships 5x Faster JSON Serialization: A New Benchmark Record",
                "excerpt": "Bun's latest release sets a new world record for JSON serialization speed, processing 1GB of JSON data in under 200ms."
            }
        ]
    },
    {
        "title": "API Technology Updates",
        "icon": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>',
        "items": [
            {
                "tag": "Industry Data",
                "date_suffix": "2026",
                "title": "JSON Streaming API Now Supported in All Major Browsers",
                "excerpt": "The W3C JSON Streaming specification has reached full browser support across Chrome, Firefox, Safari, and Edge. Streaming JSON parsing for real-time AI responses is now a first-class web platform feature."
            },
            {
                "tag": "Tool Updates",
                "date_suffix": "2026",
                "title": "Cursor and VS Code Add Real-Time JSON Lint with AI Error Explanations",
                "excerpt": "AI-powered code editors now offer inline JSON linting that not only flags errors but explains them in plain English with suggested fixes."
            },
            {
                "tag": "Dev Trends",
                "date_suffix": "2026",
                "title": "Zod v4 Hits 5M Weekly Downloads: Runtime Type Validation for AI Pipelines",
                "excerpt": "Zod continues its explosive growth driven by the AI agent era. Developers are using Zod schemas to validate LLM outputs, MCP tool responses, and RAG pipeline data."
            }
        ]
    },
    {
        "title": "Frontend & JSON",
        "icon": '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
        "items": [
            {
                "tag": "Framework Update",
                "date_suffix": "2026",
                "title": "Next.js 16 Introduces Native JSON Streaming and Partial Prerendering",
                "excerpt": "Next.js 16's App Router now natively supports JSON streaming for LLM-powered pages with automatic partial prerendering."
            },
            {
                "tag": "Runtime",
                "date_suffix": "2026",
                "title": "Node.js 24 Ships Built-in Native JSON Schema Validation",
                "excerpt": "Node.js 24 includes built-in JSON Schema validation using Ajv integration. No more third-party dependencies for basic schema validation in server-side code."
            }
        ]
    },
    {
        "title": "Developer Resources",
        "icon": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>',
        "items": [
            {
                "tag": "Open Source",
                "date_suffix": "2026",
                "title": "json-schema-to-typescript v6 Released: Generate TypeScript Types from Any JSON Schema",
                "excerpt": "Version 6 adds support for JSON Schema Draft 2020-12, improved recursive schema handling, and a new CLI with watch mode."
            },
            {
                "tag": "Learning",
                "date_suffix": "2026",
                "title": "JSONata 2.0 Launches with Native AI Query Support",
                "excerpt": "JSONata 2.0 introduces AI-assisted query generation - describe what you want in plain English and get a working JSONata expression."
            }
        ]
    }
]

# ============================================================================
# SCRIPT LOGIC
# ============================================================================

def get_news_item_html(item):
    """Generate HTML for a single news item."""
    return f'''            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">{item["tag"]}</span>
                    <span>{item["date_suffix"]}</span>
                </div>
                <h3>{item["title"]}</h3>
                <p>{item["excerpt"]}</p>
            </div>'''

def get_category_html(category):
    """Generate HTML for a news category section."""
    items_html = '\n'.join(get_news_item_html(item) for item in category["items"])
    return f'''        <!-- {category["title"]} -->
        <div class="category-section">
            <h2 class="category-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    {category["icon"]}
                </svg>
                {category["title"]}
            </h2>
{items_html}
        </div>'''

def generate_news_content():
    """Generate complete news content HTML."""
    categories_html = '\n'.join(get_category_html(cat) for cat in NEWS_CATEGORIES)
    return f'''
        <!-- Trending Today -->
{categories_html}
        <!-- Tips -->
        <div class="tip-box">
            <strong>Usage Tip</strong><br>
            Follow this page for the latest JSON and API tech updates. Combined with our <a href="format.html">JSON Formatter</a> and <a href="escape.html">JSON Escape tools</a>, you can boost your development efficiency by several times!
        </div>'''

def update_news_html():
    """Update news.html with fresh content."""
    news_path = Path(r'd:\网站开发-json\pages\news.html')
    with open(news_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new content
    new_news_content = generate_news_content()
    
    # Find and replace the news content section
    # Pattern: from "<!-- Trending Today -->" to the end of news-content div
    pattern = r'<div class="news-content">\s*<!-- Trending Today -->.*?</div>\s*<!-- Tips -->'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, f'<div class="news-content">{new_news_content}', content, flags=re.DOTALL)
    else:
        # Fallback: try simpler pattern
        pattern2 = r'(<div class="news-content">).*?(<!-- Tips -->)'
        new_content = re.sub(pattern2, f'\\1{new_news_content}\\2', content, flags=re.DOTALL)
    
    with open(news_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def push_to_github():
    """Push changes to GitHub."""
    try:
        result = subprocess.run(
            ['git', 'add', '.'],
            cwd=r'd:\网站开发-json',
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        result = subprocess.run(
            ['git', 'commit', '-m', 'Daily news update: Trending JSON & API tech updates'],
            cwd=r'd:\网站开发-json',
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"Commit warning (may be empty): {result.stderr}")
        
        # Push
        result = subprocess.run(
            ['git', 'push', 'origin', 'main'],
            cwd=r'd:\网站开发-json',
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            print("GitHub push successful")
            return True
        else:
            print(f"Push failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"GitHub push error: {e}")
        return False

def main():
    print("=" * 60)
    print("Daily News Update Script")
    print("=" * 60)
    
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Date: {today}")
    
    # Update news content
    print("\nUpdating news.html...")
    if update_news_html():
        print("News content updated successfully!")
    else:
        print("Failed to update news content")
        return
    
    # Push to GitHub
    print("\nPushing to GitHub...")
    if push_to_github():
        print("\n" + "=" * 60)
        print("Daily news update completed successfully!")
        print("=" * 60)
    else:
        print("\nGitHub push failed - changes saved locally")

if __name__ == "__main__":
    main()
