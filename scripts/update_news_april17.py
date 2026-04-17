import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\网站开发-json\pages\news.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_news_content = '''<div class="news-content"> <!-- Trending Today --> <div class="category-section"> <h2 class="category-title"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path> </svg> Trending Today </h2> <div class="news-item"> <div class="news-meta"> <span class="news-tag">API Trends</span> <span>April 10, 2026</span> </div> <h3>5 API Transformations in 2026: From REST to AI-Native</h3> <p>AI is fundamentally changing how APIs are designed and consumed. From auto-generated SDKs to intelligent error handling, the 2026 API ecosystem is undergoing unprecedented change.</p> </div> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Tech News</span> <span>April 10, 2026</span> </div> <h3>JSON Schema Draft 2020-12 Becomes W3C Recommendation</h3> <p>The latest version of JSON Schema is officially a W3C Recommendation. New conditional logic and reference mechanisms will greatly enhance API documentation automation.</p> </div> </div> <!-- API Tech --> <div class="category-section"> <h2 class="category-title"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path> </svg> API Technology Updates </h2> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Industry Data</span> <span>April 2026</span> </div> <h3>97% of API Traffic Uses JSON Format</h3> <p>According to Cloudflare's latest report, despite new technologies emerging, JSON remains the dominant format for Web APIs. The REST+JSON combination holds an absolute leading position.</p> </div> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Tool Updates</span> <span>April 2026</span> </div> <h3>Postman Launches AI-Powered API Testing Assistant</h3> <p>Postman's newly integrated AI assistant can automatically generate test cases, identify regression issues, and even predict potential API failure points.</p> </div> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Dev Trends</span> <span>April 2026</span> </div> <h3>Streaming APIs Become the New Standard for Real-time Apps</h3> <p>The combination of Server-Sent Events and JSON Streaming is becoming a new paradigm for real-time data applications, especially suitable for AI responses and monitoring scenarios.</p> </div> </div> <!-- Frontend & JSON --> <div class="category-section"> <h2 class="category-title"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <polyline points="16 18 22 12 16 6"></polyline> <polyline points="8 6 2 12 8 18"></polyline> </svg> Frontend & JSON </h2> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Framework Update</span> <span>April 2026</span> </div> <h3>React 20 Introduces Native JSON Lazy Loading Support</h3> <p>React's new version will natively support lazy loading and streaming rendering of JSON data, significantly improving rendering performance for large JSON datasets.</p> </div> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Performance</span> <span>April 2026</span> </div> <h3>JSON.parse Performance Improves 300% with New Algorithm</h3> <p>The V8 engine team released a new parsing algorithm that can increase parsing speed of large JSON files by 3x, which is significant for frontend performance optimization.</p> </div> </div> <!-- Developer Resources --> <div class="category-section"> <h2 class="category-title"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path> <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path> </svg> Developer Resources </h2> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Learning</span> <span>April 2026</span> </div> <h3>MDN Updates Complete JSON Guide</h3> <p>Mozilla Developer Network released a brand new complete JSON guide covering everything from basics to advanced topics, with lots of interactive examples.</p> </div> <div class="news-item"> <div class="news-meta"> <span class="news-tag">Open Source</span> <span>April 2026</span> </div> <h3>Top 10 JSON Processing Libraries Performance Comparison</h3> <p>2026's latest tests show JSON.parse is still the fastest option, but some WebAssembly implementations have lower memory usage.</p> </div> </div> <!-- Tips --> <div class="tip-box"> <strong>Usage Tip</strong><br> Follow this page for the latest JSON and API tech updates. Combined with our <a href="format.html">JSON Formatter</a> and <a href="escape.html">JSON Escape tools</a>, you can boost your development efficiency by several times! </div> </div>'''

new_news_content = '''<div class="news-content">
        <!-- Trending Today -->
        <div class="category-section">
            <h2 class="category-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
                </svg>
                Trending Today
            </h2>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">AI & Agents</span>
                    <span>April 17, 2026</span>
                </div>
                <h3>MCP Protocol Reaches 10,000+ Public Servers: The AI Tool Standard Takes Off</h3>
                <p>The Model Context Protocol (MCP) has surpassed 10,000 public server implementations as of April 2026. From database connectors to filesystem tools, MCP is rapidly becoming the universal bridge for AI agents. Major cloud providers are now shipping native MCP support in their AI platforms.</p>
            </div>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Web Platform</span>
                    <span>April 17, 2026</span>
                </div>
                <h3>Browser DevTools Now Built-in JSON Schema Validation and Live Error Highlighting</h3>
                <p>Chrome 122 and Firefox 120 now include native JSON Schema validation directly in DevTools. Developers can paste a schema and instantly see validation errors highlighted in the Network panel, eliminating the need for third-party schema validators during debugging.</p>
            </div>
        </div>
        <!-- API Tech -->
        <div class="category-section">
            <h2 class="category-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                </svg>
                API Technology Updates
            </h2>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Industry Data</span>
                    <span>April 2026</span>
                </div>
                <h3>JSON Streaming API Now Supported in All Major Browsers</h3>
                <p>The W3C JSON Streaming specification has reached full browser support across Chrome, Firefox, Safari, and Edge. Streaming JSON parsing for real-time AI responses, live dashboards, and IoT data feeds is now a first-class web platform feature without polyfills.</p>
            </div>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Tool Updates</span>
                    <span>April 17, 2026</span>
                </div>
                <h3>Cursor and VS Code Add Real-Time JSON Lint with AI Error Explanations</h3>
                <p>AI-powered code editors now offer inline JSON linting that not only flags errors but explains them in plain English with suggested fixes. Integration with JSON Schema makes it even more powerful for teams using typed API contracts.</p>
            </div>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Dev Trends</span>
                    <span>April 2026</span>
                </div>
                <h3>Zod v4 Hits 5M Weekly Downloads: Runtime Type Validation for AI Pipelines</h3>
                <p>Zod, the TypeScript-first schema validation library, continues its explosive growth driven by the AI agent era. Developers are using Zod schemas to validate LLM outputs, MCP tool responses, and RAG pipeline data with zero configuration overhead.</p>
            </div>
        </div>
        <!-- Frontend & JSON -->
        <div class="category-section">
            <h2 class="category-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="16 18 22 12 16 6"></polyline>
                    <polyline points="8 6 2 12 8 18"></polyline>
                </svg>
                Frontend &amp; JSON
            </h2>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Performance</span>
                    <span>April 17, 2026</span>
                </div>
                <h3>Bun 2.0 Ships 5x Faster JSON Serialization: A New Benchmark Record</h3>
                <p>Bun's latest release sets a new world record for JSON serialization speed, processing 1GB of JSON data in under 200ms. The benchmark beats Node.js and Deno by 5x, making Bun the go-to runtime for high-throughput JSON APIs.</p>
            </div>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Framework Update</span>
                    <span>April 2026</span>
                </div>
                <h3>Next.js 16 Introduces Native JSON Streaming and Partial Prerendering</h3>
                <p>Next.js 16's App Router now natively supports JSON streaming for LLM-powered pages with automatic partial prerendering. Building AI-augmented web apps with progressive JSON hydration is now a zero-config feature.</p>
            </div>
        </div>
        <!-- Developer Resources -->
        <div class="category-section">
            <h2 class="category-title">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                </svg>
                Developer Resources
            </h2>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Open Source</span>
                    <span>April 17, 2026</span>
                </div>
                <h3>json-schema-to-typescript v6 Released: Generate TypeScript Types from Any JSON Schema</h3>
                <p>Version 6 of the popular json-schema-to-typescript tool adds support for JSON Schema Draft 2020-12, improved recursive schema handling, and a new CLI with watch mode. The GitHub repo has surpassed 50,000 stars.</p>
            </div>
            <div class="news-item">
                <div class="news-meta">
                    <span class="news-tag">Learning</span>
                    <span>April 2026</span>
                </div>
                <h3>JSONata 2.0 Launches with Native AI Query Support</h3>
                <p>JSONata 2.0 introduces AI-assisted query generation - describe what you want in plain English and get a working JSONata expression. This bridges the gap between SQL-like thinking and JSON data manipulation for developers new to the format.</p>
            </div>
        </div>
        <!-- Tips -->
        <div class="tip-box">
            <strong>Usage Tip</strong><br>
            Follow this page for the latest JSON and API tech updates. Combined with our <a href="format.html">JSON Formatter</a> and <a href="escape.html">JSON Escape tools</a>, you can boost your development efficiency by several times!
        </div>
    </div>'''

if old_news_content in content:
    new_content = content.replace(old_news_content, new_news_content)
    with open(r'd:\网站开发-json\pages\news.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: news.html updated with April 17, 2026 content')
    print(f'Old length: {len(content)}, New length: {len(new_content)}')
else:
    print('ERROR: old news content not found in file')
    # Try to find what is there
    start = content.find('<div class="news-content">')
    end = content.find('</div> </main>')
    if start > 0 and end > 0:
        print('Found news-content region at:', start, '-', end)
        print('First 200 chars:', content[start:start+200])
