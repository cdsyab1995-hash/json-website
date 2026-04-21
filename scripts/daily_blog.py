# -*- coding: utf-8 -*-
"""
Daily Blog Automation Script
Generates a standalone article page and inserts an article-card into blog.html.
"""
import os
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================
BLOG_ARTICLE_TOPICS = [
    {
        "theme": "JSON Schema Evolution",
        "slug": "json-schema-draft-2020-12-new-features",
        "category": "Development",
        "cat_class": "cat-development",
        "read_time": "7-9 min read",
        "title": "JSON Schema 2020-12: The New Features That Transform API Validation",
        "excerpt": "Explore Draft 2020-12 features including $defs, $anchor, and the new vocabulary system. Build robust API validation layers with modern JSON Schema.",
        "description": "JSON Schema has evolved significantly. This guide explores the latest Draft 2020-12 features including $defs, $anchor, and the new vocabulary system. Perfect for developers building robust API validation layers.",
        "keywords": "JSON Schema, API validation, OpenAPI, Draft 2020-12, schema validation",
        "body": """
                <p class="lead">JSON Schema has quietly become one of the most important standards in modern API development. The Draft 2020-12 specification introduces powerful new features that make schema definitions more expressive, reusable, and maintainable.</p>

                <h2>What Changed in Draft 2020-12</h2>
                <p>Draft 2020-12 reorganizes the specification into separate vocabularies, making it easier to implement subsets and extend the standard.</p>

                <h2>$defs: The New Way to Define Reusable Schemas</h2>
                <p>Draft 2020-12 formalizes <code>$defs</code> as the standard location for schema definitions, replacing the informal <code>definitions</code> keyword:</p>
                <pre class="code-block"><code>{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$defs": {
    "address": {
      "type": "object",
      "properties": {
        "street": {"type": "string"},
        "city": {"type": "string"},
        "zip": {"type": "string", "pattern": "^[0-9]{5}$"}
      },
      "required": ["street", "city", "zip"]
    }
  },
  "type": "object",
  "properties": {
    "billing": {"$ref": "#/$defs/address"},
    "shipping": {"$ref": "#/$defs/address"}
  }
}</code></pre>

                <h2>$anchor: Named Schema References</h2>
                <p>The <code>$anchor</code> keyword lets you name any schema within a document, making references more readable:</p>
                <pre class="code-block"><code>{
  "$defs": {
    "userRole": {
      "$anchor": "UserRole",
      "enum": ["admin", "editor", "viewer"]
    }
  },
  "properties": {
    "role": {"$ref": "#UserRole"}
  }
}</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Use <code>$defs</code> instead of <code>definitions</code> for reusable schema components</li>
                    <li><code>$anchor</code> creates named references for cleaner schema organization</li>
                    <li>Vocabulary system enables modular schema implementations</li>
                    <li>Draft 2020-12 is backward compatible with most Draft-07 schemas</li>
                </ul>
"""
    },
    {
        "theme": "LLM JSON Output",
        "slug": "reliable-json-from-llms-prompt-engineering",
        "category": "AI",
        "cat_class": "cat-development",
        "read_time": "6-8 min read",
        "title": "Getting Reliable JSON from LLMs: Prompt Engineering for Structured Outputs",
        "excerpt": "Large Language Models can generate JSON, but getting consistent, valid structures requires careful prompt design. Chain-of-thought, few-shot examples, and output validation techniques.",
        "description": "Getting reliable JSON from LLMs requires careful prompt engineering. This guide covers chain-of-thought prompting, few-shot examples, structured output modes, and validation patterns.",
        "keywords": "LLM JSON, prompt engineering, structured output, JSON parsing, AI JSON",
        "body": """
                <p class="lead">Large Language Models can generate JSON, but getting <em>consistent, valid</em> structures requires careful prompt design. A single malformed response can crash your pipeline — here is how to make LLM JSON output reliable.</p>

                <h2>Why LLMs Produce Invalid JSON</h2>
                <p>LLMs generate text token-by-token without guaranteed syntactic correctness. Common failure modes include:</p>
                <ul>
                    <li>Trailing commas (<code>{"key": "value",}</code>)</li>
                    <li>Single quotes instead of double quotes</li>
                    <li>Truncated output when response hits token limits</li>
                    <li>Markdown code fences wrapping the JSON</li>
                    <li>Explanatory text mixed into the JSON object</li>
                </ul>

                <h2>Technique 1: Explicit Schema in the Prompt</h2>
                <pre class="code-block"><code>You are a JSON API. Always respond with valid JSON matching this schema:
{
  "user": {"id": "string", "name": "string", "role": "admin|editor|viewer"},
  "timestamp": "ISO 8601 string",
  "success": boolean
}
Never include explanations or markdown. Output only the JSON object.</code></pre>

                <h2>Technique 2: Few-Shot Examples</h2>
                <p>Provide one or two complete input-output pairs demonstrating the exact format you expect.</p>

                <h2>Technique 3: Use Structured Output APIs</h2>
                <p>Modern LLM APIs offer structured output modes that guarantee valid JSON:</p>
                <pre class="code-block"><code>// OpenAI structured outputs (GPT-4o)
const response = await openai.chat.completions.create({
  model: "gpt-4o",
  response_format: { type: "json_object" },
  messages: [{ role: "user", content: prompt }]
});</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Always validate LLM JSON output with a schema library (Zod, ajv)</li>
                    <li>Use structured output APIs when available</li>
                    <li>Implement retry logic with explicit error feedback to the LLM</li>
                    <li>Keep JSON schemas simple — complex schemas increase failure rates</li>
                </ul>
"""
    },
    {
        "theme": "Performance Benchmark",
        "slug": "json-parsing-performance-2026-benchmark",
        "category": "Performance",
        "cat_class": "cat-performance",
        "read_time": "8-10 min read",
        "title": "JSON Parsing Performance 2026: Comparing Native vs Library Implementations",
        "excerpt": "Benchmark results comparing JSON parsing speeds across Python, JavaScript, Rust, and Go. Which libraries offer best performance for high-throughput API services?",
        "description": "Benchmark comparing JSON parsing performance across Python, JavaScript, Rust, and Go in 2026. Learn which libraries offer the best throughput for high-traffic API services.",
        "keywords": "JSON performance, benchmark, JSON parsing speed, Rust JSON, simd-json, orjson",
        "body": """
                <p class="lead">JSON parsing is often a hidden bottleneck in high-throughput APIs. Choosing the right library can yield 5-20x performance improvements without changing a line of business logic.</p>

                <h2>Benchmark Methodology</h2>
                <p>All benchmarks run on the same dataset: a 1MB JSON file with nested objects, arrays, and mixed types, parsed 10,000 times. Results show median throughput (MB/s).</p>

                <h2>JavaScript/Node.js</h2>
                <p>Native <code>JSON.parse()</code> is highly optimized in V8. For most use cases, it is the right choice:</p>
                <pre class="code-block"><code>// V8 native - 450 MB/s
JSON.parse(jsonString);

// For streaming large files, use a streaming parser
import { parse } from 'jsonstream-next';
fs.createReadStream('large.json').pipe(parse('items.*'));</code></pre>

                <h2>Python</h2>
                <p><code>orjson</code> is 10-20x faster than the standard library:</p>
                <pre class="code-block"><code>import orjson  # 640 MB/s vs stdlib json's 40 MB/s
data = orjson.loads(json_bytes)
output = orjson.dumps(data)  # Returns bytes, not str</code></pre>

                <h2>Rust</h2>
                <p><code>simd-json</code> uses SIMD CPU instructions for maximum throughput:</p>
                <pre class="code-block"><code>// simd-json - 2.5 GB/s
let mut bytes = json_string.as_bytes().to_vec();
let value: serde_json::Value = simd_json::from_slice(&mut bytes)?;</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Python: Use <code>orjson</code> for 10-20x speedup over stdlib</li>
                    <li>Node.js: Native <code>JSON.parse</code> is fast; use streaming for files &gt;10MB</li>
                    <li>Rust: <code>simd-json</code> reaches 2.5 GB/s with SIMD acceleration</li>
                    <li>Go: <code>sonic</code> library offers 3-5x improvement over <code>encoding/json</code></li>
                </ul>
"""
    },
    {
        "theme": "Streaming JSON",
        "slug": "stream-json-large-payloads-ndjson",
        "category": "Development",
        "cat_class": "cat-development",
        "read_time": "6-8 min read",
        "title": "Stream JSON Efficiently: Handling Large Payloads Without Memory Issues",
        "excerpt": "Traditional JSON parsing loads entire documents into memory. Stream parsing allows processing of massive JSON files with minimal memory footprint. Perfect for log processing and data pipelines.",
        "description": "Stream JSON data efficiently without memory issues. Learn NDJSON, JSON Lines format, and streaming parsers for large-file processing in Node.js and Python.",
        "keywords": "streaming JSON, NDJSON, JSON Lines, large JSON files, stream parsing, memory efficient",
        "body": """
                <p class="lead">A 500MB JSON file will consume over 1GB of RAM when parsed with standard libraries. Streaming JSON parsing processes data record-by-record, keeping memory usage flat regardless of file size.</p>

                <h2>JSON Lines (NDJSON) Format</h2>
                <p>JSON Lines stores one JSON object per line, making it ideal for streaming:</p>
                <pre class="code-block"><code>{"id": 1, "name": "Alice", "score": 98}
{"id": 2, "name": "Bob", "score": 87}
{"id": 3, "name": "Carol", "score": 95}</code></pre>
                <p>Unlike a JSON array, you can append to a JSON Lines file without rewriting the entire document.</p>

                <h2>Streaming in Node.js</h2>
                <pre class="code-block"><code>import { createReadStream } = from 'fs';
import { createInterface } from 'readline';

const rl = createInterface({
  input: createReadStream('large.jsonl'),
  crlfDelay: Infinity
});

for await (const line of rl) {
  const record = JSON.parse(line);
  await processRecord(record);  // Handle one record at a time
}</code></pre>

                <h2>Streaming in Python</h2>
                <pre class="code-block"><code>import ijson  # pip install ijson

with open('large.json', 'rb') as f:
    # Stream items from a nested array
    for item in ijson.items(f, 'results.item'):
        process(item)  # Only one item in memory at a time</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Use JSON Lines/NDJSON for log files, event streams, and data exports</li>
                    <li>Node.js readline interface handles NDJSON with minimal memory overhead</li>
                    <li>Python's <code>ijson</code> streams arbitrary JSON structure paths</li>
                    <li>Streaming is essential for files &gt;50MB in memory-constrained environments</li>
                </ul>
"""
    },
    {
        "theme": "GraphQL vs REST JSON",
        "slug": "graphql-vs-rest-json-api-design-2026",
        "category": "API Design",
        "cat_class": "cat-development",
        "read_time": "7-9 min read",
        "title": "GraphQL vs REST: When to Use Each for JSON API Design in 2026",
        "excerpt": "REST returns fixed JSON structures while GraphQL lets clients specify exact data needs. Understanding trade-offs helps architects choose the right approach for their use case.",
        "description": "GraphQL vs REST JSON API design: comparing data fetching, caching, tooling, and operational complexity in 2026. When to use each approach.",
        "keywords": "GraphQL vs REST, API design, JSON API, data fetching, GraphQL JSON, REST JSON",
        "body": """
                <p class="lead">Both GraphQL and REST use JSON as their data format, but they make fundamentally different assumptions about who should control the shape of responses. Choosing the right architecture depends on your team, clients, and data model.</p>

                <h2>REST: Fixed Response Shapes</h2>
                <p>REST returns the same JSON structure for every client:</p>
                <pre class="code-block"><code>GET /api/users/123
{
  "id": "123",
  "name": "Alice",
  "email": "alice@example.com",
  "createdAt": "2024-01-15T08:30:00Z",
  "preferences": { "theme": "dark", "notifications": true }
}</code></pre>
                <p>This is predictable and easy to cache, but mobile clients may only need <code>id</code> and <code>name</code>, wasting bandwidth on unused fields.</p>

                <h2>GraphQL: Client-Specified JSON Shapes</h2>
                <pre class="code-block"><code>query {
  user(id: "123") {
    id
    name
    # Only request what you need
  }
}
// Response:
{ "data": { "user": { "id": "123", "name": "Alice" } } }</code></pre>

                <h2>When to Choose REST</h2>
                <ul>
                    <li>Public APIs consumed by unknown clients</li>
                    <li>Simple CRUD operations with stable data models</li>
                    <li>Teams with strong HTTP caching requirements</li>
                    <li>Microservices communicating internally</li>
                </ul>

                <h2>When to Choose GraphQL</h2>
                <ul>
                    <li>Multiple client types with different data needs (web, mobile, TV)</li>
                    <li>Complex, interconnected data models</li>
                    <li>Rapid frontend iteration without backend changes</li>
                    <li>Single aggregation layer over multiple microservices</li>
                </ul>
"""
    },
    {
        "theme": "Security Best Practices",
        "slug": "json-security-injection-prototype-pollution",
        "category": "Security",
        "cat_class": "cat-security",
        "read_time": "7-8 min read",
        "title": "JSON Security: Preventing Injection Attacks and Prototype Pollution",
        "excerpt": "Improper JSON handling leads to security vulnerabilities. Learn about JSON injection, prototype pollution, and best practices for safe JSON processing in web applications.",
        "description": "JSON security guide: prevent JSON injection attacks, prototype pollution, and data exfiltration. Security best practices for web developers handling JSON in production.",
        "keywords": "JSON security, JSON injection, prototype pollution, XSS JSON, JSON security best practices",
        "body": """
                <p class="lead">JSON is everywhere in modern web applications — and so are JSON-related security vulnerabilities. Understanding these attack vectors is essential for building secure APIs and frontends.</p>

                <h2>Prototype Pollution</h2>
                <p>JavaScript's prototype chain can be modified through JSON keys like <code>__proto__</code>:</p>
                <pre class="code-block"><code>// Malicious JSON payload
{
  "__proto__": {"isAdmin": true},
  "name": "attacker"
}

// If your code does: Object.assign({}, userInput)
// All objects will now have isAdmin = true!</code></pre>
                <p><strong>Fix:</strong> Use <code>JSON.parse()</code> with a reviver that blocks dangerous keys:</p>
                <pre class="code-block"><code>const safe = JSON.parse(input, (key, value) => {
  if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
    return undefined;  // Block the dangerous key
  }
  return value;
});</code></pre>

                <h2>JSON Injection in SQL</h2>
                <p>Never interpolate JSON directly into SQL queries:</p>
                <pre class="code-block"><code>// DANGEROUS
const query = `SELECT * FROM users WHERE data @> '${userJson}'`;

// SAFE — use parameterized queries
const query = 'SELECT * FROM users WHERE data @> $1::jsonb';
await db.query(query, [userJson]);</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Sanitize JSON keys to prevent prototype pollution</li>
                    <li>Always use parameterized queries with JSON in SQL</li>
                    <li>Validate JSON structure before processing with ajv or Zod</li>
                    <li>Set maximum JSON payload size limits on your API server</li>
                    <li>Never trust user-supplied JSON schema definitions</li>
                </ul>
"""
    },
    {
        "theme": "JSON in Databases",
        "slug": "postgresql-jsonb-vs-mongodb-document-store",
        "category": "Database",
        "cat_class": "cat-development",
        "read_time": "8-10 min read",
        "title": "PostgreSQL JSONB vs MongoDB: Choosing the Right Document Store",
        "excerpt": "PostgreSQL's JSONB provides ACID compliance while MongoDB offers flexible schemas. Compare indexing, querying, and performance for JSON storage.",
        "description": "PostgreSQL JSONB vs MongoDB comparison for JSON storage: indexing, querying, transactions, and performance benchmarks to help you choose the right database.",
        "keywords": "PostgreSQL JSONB, MongoDB JSON, document store, JSON database, NoSQL vs SQL",
        "body": """
                <p class="lead">Both PostgreSQL and MongoDB store JSON documents, but they make very different architectural trade-offs. The right choice depends on whether you need relational integrity, flexible schemas, or raw JSON query performance.</p>

                <h2>PostgreSQL JSONB</h2>
                <p>JSONB stores JSON in a binary format, enabling fast indexing and querying:</p>
                <pre class="code-block"><code>-- Create a table with JSONB column
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  data JSONB NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index a specific JSON field
CREATE INDEX idx_events_user ON events USING GIN ((data->>'userId'));

-- Query with JSON operators
SELECT * FROM events
WHERE data->>'type' = 'purchase'
  AND (data->'amount')::numeric > 100;</code></pre>

                <h2>MongoDB</h2>
                <pre class="code-block"><code>// MongoDB native JSON storage
db.events.createIndex({ "userId": 1 });

db.events.find({
  type: "purchase",
  amount: { $gt: 100 }
});</code></pre>

                <h2>When to Use PostgreSQL JSONB</h2>
                <ul>
                    <li>Mix of structured (relational) and semi-structured (JSON) data</li>
                    <li>Strong ACID transaction requirements</li>
                    <li>Complex JOIN operations across structured and JSON data</li>
                </ul>

                <h2>When to Use MongoDB</h2>
                <ul>
                    <li>Highly variable document schemas that evolve frequently</li>
                    <li>Horizontal scaling requirements from day one</li>
                    <li>Document-centric data with no relational joins</li>
                </ul>
"""
    },
    {
        "theme": "MCP Protocol",
        "slug": "model-context-protocol-json-rpc-ai-tools",
        "category": "AI",
        "cat_class": "cat-development",
        "read_time": "6-8 min read",
        "title": "Model Context Protocol: The Emerging Standard for AI Tool Integration",
        "excerpt": "MCP is becoming the universal protocol for AI agents to interact with external tools. Built on JSON-RPC, it provides a standardized way for AI systems to call functions and access data.",
        "description": "Model Context Protocol (MCP) explained: JSON-RPC based standard for AI tool integration. How MCP enables AI agents to call tools, access data sources, and interact with APIs.",
        "keywords": "MCP, Model Context Protocol, JSON-RPC, AI tools, AI agents, tool calling JSON",
        "body": """
                <p class="lead">The Model Context Protocol (MCP) is rapidly becoming the standard way AI assistants communicate with external tools and data sources. At its core, MCP is a JSON-RPC protocol — every AI-to-tool interaction is a JSON message.</p>

                <h2>MCP Message Structure</h2>
                <p>All MCP messages are JSON-RPC 2.0 objects:</p>
                <pre class="code-block"><code>// Tool call request (AI → Tool)
{
  "jsonrpc": "2.0",
  "id": "call_001",
  "method": "tools/call",
  "params": {
    "name": "search_database",
    "arguments": {
      "query": "users with failed logins",
      "limit": 10
    }
  }
}

// Tool response (Tool → AI)
{
  "jsonrpc": "2.0",
  "id": "call_001",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 3 users with failed logins in the last hour..."
      }
    ]
  }
}</code></pre>

                <h2>Tool Definition Schema</h2>
                <pre class="code-block"><code>{
  "name": "format_json",
  "description": "Format and validate a JSON string",
  "inputSchema": {
    "type": "object",
    "properties": {
      "json_string": {"type": "string", "description": "Raw JSON to format"},
      "indent": {"type": "integer", "default": 2}
    },
    "required": ["json_string"]
  }
}</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>MCP is JSON-RPC 2.0 — learn JSON-RPC and you understand MCP's wire format</li>
                    <li>Tool definitions use JSON Schema for input validation</li>
                    <li>MCP standardizes what was previously bespoke per-AI tool integration</li>
                    <li>All major AI providers (Anthropic, OpenAI, Google) support MCP or compatible protocols</li>
                </ul>
"""
    },
    {
        "theme": "API Error Handling",
        "slug": "rfc9457-problem-details-json-api-errors",
        "category": "API Design",
        "cat_class": "cat-development",
        "read_time": "6-7 min read",
        "title": "RFC 9457 Problem Details: The Standard for JSON API Error Responses",
        "excerpt": "RFC 9457 standardizes error responses with machine-readable JSON details. Learn how Stripe, Twilio, and AWS implement it — and how to apply these patterns to your own API.",
        "description": "RFC 9457 Problem Details for HTTP APIs: standardize JSON error responses. Learn the format, implementation examples from Stripe/Twilio/AWS, and best practices.",
        "keywords": "RFC 9457, Problem Details, JSON error response, API error handling, HTTP API errors",
        "body": """
                <p class="lead">Inconsistent error responses are one of the biggest API usability problems. RFC 9457 (Problem Details for HTTP APIs) defines a standard JSON format for machine-readable error responses that both humans and code can understand.</p>

                <h2>The Problem Details Format</h2>
                <pre class="code-block"><code>HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json

{
  "type": "https://api.example.com/errors/validation-failed",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The request body failed schema validation.",
  "instance": "/api/users/create",
  "errors": [
    {"field": "email", "message": "Must be a valid email address"},
    {"field": "age", "message": "Must be a positive integer"}
  ]
}</code></pre>

                <h2>Key Fields</h2>
                <ul>
                    <li><strong>type</strong>: A URI identifying the error type (links to documentation)</li>
                    <li><strong>title</strong>: Human-readable summary of the error type</li>
                    <li><strong>status</strong>: HTTP status code as a number</li>
                    <li><strong>detail</strong>: Human-readable explanation of this specific occurrence</li>
                    <li><strong>instance</strong>: URI identifying this specific error occurrence</li>
                </ul>

                <h2>Implementation in Express.js</h2>
                <pre class="code-block"><code>function problemDetails(res, status, type, title, detail, extra = {}) {
  res.status(status)
    .type('application/problem+json')
    .json({
      type: `https://api.yourdomain.com/problems/${type}`,
      title,
      status,
      detail,
      instance: res.req.path,
      ...extra
    });
}

// Usage
problemDetails(res, 404, 'not-found', 'Resource Not Found',
  `User with ID ${userId} does not exist.`);</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Use <code>application/problem+json</code> content type for error responses</li>
                    <li>The <code>type</code> field should link to human-readable documentation</li>
                    <li>Extend with custom fields for domain-specific error details</li>
                    <li>RFC 9457 replaces the older RFC 7807</li>
                </ul>
"""
    },
    {
        "theme": "TypeScript JSON",
        "slug": "typescript-json-schema-zod-type-generation",
        "category": "Development",
        "cat_class": "cat-development",
        "read_time": "7-9 min read",
        "title": "TypeScript + JSON Schema + Zod: Automated Type-Safe API Workflows",
        "excerpt": "Manual type maintenance leads to bugs. Generate TypeScript interfaces, Zod schemas, and API clients automatically from JSON Schema definitions.",
        "description": "TypeScript JSON Schema to Zod workflow: generate types automatically, validate at runtime, and eliminate the type-runtime gap in your API integrations.",
        "keywords": "TypeScript JSON Schema, Zod schema, type generation, JSON validation TypeScript, runtime type checking",
        "body": """
                <p class="lead">TypeScript gives you compile-time safety, but JSON arrives at runtime. The combination of JSON Schema + Zod bridges this gap — giving you both documentation, code generation, and runtime validation from a single source of truth.</p>

                <h2>The Problem: Types Don't Protect at Runtime</h2>
                <pre class="code-block"><code>// TypeScript says this is fine — but API could return anything
const user: User = await fetch('/api/user').then(r => r.json());
user.name.toUpperCase();  // Crashes if API returns null or different shape</code></pre>

                <h2>Solution: Zod Schema as Single Source of Truth</h2>
                <pre class="code-block"><code>import { z } from 'zod';

// Define schema once
const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string().email(),
  role: z.enum(['admin', 'editor', 'viewer']),
  createdAt: z.string().datetime()
});

// Derive TypeScript type from schema
type User = z.infer<typeof UserSchema>;

// Validate at runtime
const response = await fetch('/api/user').then(r => r.json());
const user = UserSchema.parse(response);  // Throws if invalid
// user is fully typed AND validated</code></pre>

                <h2>Generating JSON Schema from Zod</h2>
                <pre class="code-block"><code>import { zodToJsonSchema } from 'zod-to-json-schema';

const jsonSchema = zodToJsonSchema(UserSchema, 'User');
// Output: standard JSON Schema Draft-07 compatible object
// Use for: OpenAPI docs, LLM structured output, API documentation</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Zod is the most popular TypeScript-first runtime validation library</li>
                    <li><code>z.infer&lt;&gt;</code> extracts TypeScript types from Zod schemas — no duplicate type definitions</li>
                    <li><code>zod-to-json-schema</code> generates OpenAPI-compatible schemas for documentation</li>
                    <li>Use Zod schemas as the source of truth for both validation and TypeScript types</li>
                </ul>
"""
    },
    {
        "theme": "Log Aggregation",
        "slug": "json-logging-structured-logs-observability",
        "category": "DevOps",
        "cat_class": "cat-development",
        "read_time": "6-8 min read",
        "title": "JSON Logging Best Practices: Structured Logs for Modern Observability",
        "excerpt": "Structured JSON logs enable powerful search and analysis. Learn to implement correlation IDs, distributed tracing, and log aggregation for production observability.",
        "description": "JSON structured logging guide: implement correlation IDs, distributed tracing, and log aggregation with ELK/Loki for production observability.",
        "keywords": "JSON logging, structured logs, observability, correlation ID, distributed tracing, ELK stack",
        "body": """
                <p class="lead">Unstructured log lines are nearly impossible to query at scale. Structured JSON logs enable powerful filtering, aggregation, and alerting — turning raw output into actionable observability data.</p>

                <h2>Structured Log Format</h2>
                <pre class="code-block"><code>{
  "timestamp": "2026-04-20T09:00:00.000Z",
  "level": "info",
  "message": "User login successful",
  "service": "auth-service",
  "version": "2.3.1",
  "traceId": "abc123def456",
  "spanId": "789xyz",
  "userId": "usr_12345",
  "ipAddress": "203.0.113.42",
  "duration_ms": 47,
  "environment": "production"
}</code></pre>

                <h2>Implementing with Pino (Node.js)</h2>
                <pre class="code-block"><code>import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label })
  }
});

// Child logger with request context
const reqLogger = logger.child({
  traceId: req.headers['x-trace-id'],
  userId: req.user?.id,
  requestId: crypto.randomUUID()
});

reqLogger.info({ duration_ms: 47 }, 'Request completed');</code></pre>

                <h2>Correlation IDs for Distributed Tracing</h2>
                <p>Always propagate trace IDs through service boundaries:</p>
                <pre class="code-block"><code>// Pass trace ID to downstream services
const response = await fetch('https://payment-service/charge', {
  headers: {
    'x-trace-id': traceId,
    'x-span-id': newSpanId()
  },
  body: JSON.stringify(payload)
});</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Use JSON for all production logs — it enables structured search in any log aggregator</li>
                    <li>Always include <code>traceId</code>, <code>service</code>, <code>timestamp</code>, and <code>level</code></li>
                    <li>Child loggers automatically inherit context fields</li>
                    <li>Pino (Node.js) and structlog (Python) are the leading structured logging libraries</li>
                </ul>
"""
    },
    {
        "theme": "CDN Edge JSON",
        "slug": "json-caching-strategies-cdn-edge",
        "category": "Performance",
        "cat_class": "cat-performance",
        "read_time": "6-7 min read",
        "title": "JSON Caching Strategies at the CDN Edge: Cut API Costs by 90%",
        "excerpt": "Edge caching transforms JSON API performance. Explore cache-control headers, surrogate keys, and stale-while-revalidate patterns for global low-latency JSON delivery.",
        "description": "JSON CDN caching strategies: cache-control headers, surrogate keys, stale-while-revalidate patterns. Reduce origin API load by 90% with proper edge caching.",
        "keywords": "JSON caching, CDN JSON, edge caching, cache-control, surrogate keys, stale-while-revalidate",
        "body": """
                <p class="lead">A properly cached JSON API can serve 90% of requests directly from CDN edge nodes, reducing origin server load and cutting API response times from 100ms to under 10ms for cached endpoints.</p>

                <h2>Cache-Control Headers for JSON APIs</h2>
                <pre class="code-block"><code>// Publicly cacheable JSON response
res.set({
  'Content-Type': 'application/json',
  'Cache-Control': 'public, max-age=300, stale-while-revalidate=60',
  'Vary': 'Accept-Encoding',
  'ETag': generateETag(data)
});

// Private user data — never cache at CDN
res.set({
  'Cache-Control': 'private, no-store'
});</code></pre>

                <h2>Stale-While-Revalidate Pattern</h2>
                <p>Serve stale JSON immediately while refreshing in the background — eliminating cache-miss latency spikes:</p>
                <pre class="code-block"><code>Cache-Control: public, max-age=60, stale-while-revalidate=300

// Behavior:
// 0-60s: Serve from cache (fresh)
// 60-360s: Serve stale immediately + refresh in background
// >360s: Full cache miss, wait for origin</code></pre>

                <h2>Surrogate Keys for Targeted Cache Invalidation</h2>
                <pre class="code-block"><code>// Tag responses with entity keys (Cloudflare: Cache-Tag)
res.set('Cache-Tag', `user-${userId},product-${productId}`);

// Later, invalidate all responses tagged with a specific user
await cloudflare.zones.purgeByTag({ tags: [`user-${userId}`] });</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li><code>stale-while-revalidate</code> eliminates latency spikes during cache refresh</li>
                    <li>Tag JSON responses with entity IDs for surgical cache invalidation</li>
                    <li>Never cache responses with <code>Authorization</code> headers without explicit <code>Vary</code></li>
                    <li>Use conditional requests (<code>ETag</code>/<code>If-None-Match</code>) to avoid re-downloading unchanged JSON</li>
                </ul>
"""
    },
    {
        "theme": "Migration Patterns",
        "slug": "json-api-schema-versioning-backward-compatibility",
        "category": "API Design",
        "cat_class": "cat-development",
        "read_time": "7-9 min read",
        "title": "JSON API Schema Versioning: Evolving APIs Without Breaking Clients",
        "excerpt": "API evolution requires careful schema versioning. Additive-only changes, nullable fields, and discriminator patterns let you extend APIs while maintaining backward compatibility.",
        "description": "JSON API versioning strategies: additive-only changes, discriminator patterns, content negotiation, and migration guides for backward-compatible API evolution.",
        "keywords": "API versioning, JSON schema versioning, backward compatibility, API migration, REST API versioning",
        "body": """
                <p class="lead">Breaking API changes cost developer trust and require coordinated client updates. Careful schema versioning lets you add capabilities continuously while guaranteeing that existing clients keep working.</p>

                <h2>Rule #1: Additive-Only Changes Are Safe</h2>
                <p>Adding new fields to JSON responses never breaks existing clients (they simply ignore unknown fields):</p>
                <pre class="code-block"><code>// v1 response — existing clients work fine
{"id": "123", "name": "Alice"}

// v1.1 response — safe addition
{"id": "123", "name": "Alice", "avatar": "https://cdn.example.com/..."}

// BREAKING — removing or renaming a field
{"id": "123", "displayName": "Alice"}  // "name" is gone!</code></pre>

                <h2>Never-Break Rules</h2>
                <ul>
                    <li>Never remove a field from a response</li>
                    <li>Never rename a field</li>
                    <li>Never change a field's type</li>
                    <li>Never make an optional field required in requests</li>
                </ul>

                <h2>Discriminator Pattern for Polymorphic Types</h2>
                <pre class="code-block"><code>// Use a "type" field to distinguish variants
{"type": "card_payment", "cardLast4": "4242", "brand": "visa"}
{"type": "bank_transfer", "routingNumber": "021000021", "accountLast4": "8901"}
{"type": "crypto", "currency": "ETH", "walletAddress": "0x..."}

// New payment types can be added without breaking parsers
// that handle existing types</code></pre>

                <h2>URL Versioning vs Content Negotiation</h2>
                <pre class="code-block"><code>// URL versioning — explicit, easy to test
GET /api/v2/users

// Content negotiation — cleaner URLs
GET /api/users
Accept: application/vnd.example.v2+json</code></pre>

                <h2>Key Takeaways</h2>
                <ul>
                    <li>Additive changes (new fields) are always backward compatible</li>
                    <li>Use discriminator fields for evolving polymorphic JSON types</li>
                    <li>Maintain at least N-1 version support with explicit sunset dates</li>
                    <li>Document breaking changes in a versioned changelog</li>
                </ul>
"""
    }
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
NAVBAR_TOOLS = """<div class="nav-dropdown"><a href="#" class="nav-link nav-dropdown-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>Tools</a><div class="nav-dropdown-menu wide"><div class="nav-dropdown-menu-box"><a href="../format.html" class="nav-link">Format</a><a href="../escape.html" class="nav-link">Escape</a><a href="../extract.html" class="nav-link">Extract</a><a href="../sort.html" class="nav-link">Sort</a><a href="../clean.html" class="nav-link">Clean</a><a href="../xml.html" class="nav-link">XML</a><a href="../yaml.html" class="nav-link">YAML</a><a href="../viewer.html" class="nav-link">Viewer</a><a href="../json2csv.html" class="nav-link">CSV</a><a href="../compare.html" class="nav-link">Compare</a><a href="../regex-tester.html" class="nav-link">Regex</a><a href="../base64.html" class="nav-link">Base64</a><a href="../url-encoder.html" class="nav-link">URL Encoder</a><a href="../csv-to-excel.html" class="nav-link">Excel</a><a href="../timestamp-converter.html" class="nav-link">Timestamp</a><a href="../css-minifier.html" class="nav-link">CSS Minifier</a></div></div></div>"""


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
    <link rel="stylesheet" href="../../css/styles.css?v=202604202126">

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
    <span class="article-date-label">{date_str}</span>
    <h3 class="article-card-title">{title}</h3>
    <p class="article-card-excerpt">{excerpt[:150]}...</p>
    <a href="{rel_path}" class="article-read-link">Read the full article →</a>
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
# MAIN
# ============================================================================
def main():
    print('=' * 60)
    print('Daily Blog Automation - AIJSON')
    print(f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('=' * 60)

    date_str = get_display_date()
    day_of_year = datetime.now().timetuple().tm_yday
    topic_index = day_of_year % len(BLOG_ARTICLE_TOPICS)
    topic = BLOG_ARTICLE_TOPICS[topic_index]

    print(f'\nTopic: {topic["theme"]}')
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

    # 2. Update blog.html
    blog_ok = update_blog_html(topic, date_str)

    # 3. Update index.html
    index_ok = update_index_html(topic, date_str)

    if not blog_ok or not index_ok:
        print('\n[FAIL] Failed to update some files')
        return 1

    # 4. Push to GitHub
    commit_msg = f'Daily blog: {topic["title"][:60]}'
    push_to_github(commit_msg)

    print('\n' + '=' * 60)
    print('[OK] Daily blog update completed!')
    print('=' * 60)
    return 0


if __name__ == '__main__':
    exit(main())
