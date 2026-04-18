# 视频脚本

> 配套文档：docs/VIDEO-CONTENT-PLAN.md
> 更新时间：2026-04-18

---

## 视频 #2: JSON vs XML vs YAML — One Video to Decide

**标题**: JSON vs XML vs YAML — One Video to Decide
**目标关键词**: json vs xml vs yaml comparison, when to use yaml, xml vs json
**时长**: 8 分钟（480 秒）
**难度**: 初级

---

### 脚本正文

**[0:00-0:20] HOOK**

"Confused about when to use JSON, XML, or YAML? You're not alone. In this video, I'll break it down once and for all — with real examples you'll actually encounter."

**[0:20-0:40] AGENDA**

"Three parts: First, what each format looks like. Second, when to use each one. Third, the decision tree so you never have to think about it again."

**[0:40-2:00] WHAT DO THEY LOOK LIKE?**

"Let's start with XML — the old guard:

```xml
<user>
  <name>Sarah</name>
  <age>28</age>
  <skills>
    <skill>JavaScript</skill>
    <skill>Python</skill>
  </skills>
</user>
```

Verbose, but self-describing. You know exactly what everything is.

Now JSON — the modern standard:

```json
{
  "name": "Sarah",
  "age": 28,
  "skills": ["JavaScript", "Python"]
}
```

Half the size. Still human-readable. Every language can parse it.

And YAML — the human-friendly one:

```yaml
name: Sarah
age: 28
skills:
  - JavaScript
  - Python
```

No quotes needed for most values. Indentation matters. It's almost like writing in English."

**[2:00-4:00] WHEN TO USE EACH**

"Here's my rule of thumb.

**Use JSON when:**
- You're building web APIs
- You're exchanging data between services
- You need language-agnostic data storage
- Speed and size matter

JSON is the lingua franca of the web. If you're building an API, use JSON. That's not a suggestion — that's the industry standard.

**Use XML when:**
- You're dealing with legacy enterprise systems
- You need document validation with complex rules
- You're working with financial or government systems
- You need namespaces to avoid conflicts

Banks, hospitals, and governments still live on XML. If you're integrating with these systems, you'll need XML.

**Use YAML when:**
- You're writing configuration files
- You want human-editable files
- You're documenting something non-sensitive
- You need comments in your data

Dockerfiles, Kubernetes configs, GitHub Actions, Ansible — all YAML. It's not for data exchange. It's for config."

**[4:00-6:00] THE DECISION TREE**

"Let me make this dead simple.

Question 1: Are you building an API or exchanging data?
→ YES: Use JSON. Always. No exceptions.

Question 2: Are you writing a config file?
→ YES: Use YAML. It's the standard for config.

Question 3: Are you dealing with enterprise or government systems?
→ YES: Use XML. You have no choice.

Question 4: None of the above?
→ Use JSON. It's always safe.

Let me give you real-world examples:

GitHub's API? JSON.
Docker Compose file? YAML.
Bank transfer protocol? XML.
Your REST API? JSON.
Application config? YAML or JSON.
Database storage? JSON or XML depending on the DB."

**[6:00-7:30] LIVE DEMO**

"Let me show you a real transformation.

Here's a configuration in YAML:

```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret123
```

Same thing in JSON:

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": {
      "username": "admin",
      "password": "secret123"
    }
  }
}
```

Same thing in XML:

```xml
<database>
  <host>localhost</host>
  <port>5432</port>
  <credentials>
    <username>admin</username>
    <password>secret123</password>
  </credentials>
</database>
```

The YAML is cleanest for humans. JSON is cleanest for machines. XML is... well, it's still around for a reason."

**[7:30-8:00] SUMMARY**

"Quick recap:

JSON — for APIs and data exchange. Fast, small, universal.
XML — for enterprise and government systems. Verbose but powerful.
YAML — for config files and human-editable documents. Clean and readable.

One more thing: You don't have to pick just one. Modern applications use all three. The key is knowing which tool fits which job.

If you want to try JSON yourself, aijsons.com has free tools — formatter, validator, minifier. Link in the description.

Hit like if this helped, and subscribe for more developer tips."

---

## 视频 #3: 10 cURL Tips for JSON APIs

**标题**: 10 cURL Tips for JSON APIs — Command Line Mastery
**目标关键词**: curl json api command line, curl tutorial, json api request
**时长**: 8 分钟（480 秒）
**难度**: 中级

---

### 脚本正文

**[0:00-0:15] HOOK**

"If you're not using cURL for API testing, you're wasting time. These 10 tips will save you hours every week."

**[0:15-0:30] SETUP**

"Before we start — make sure cURL is installed. It comes with macOS and Linux. On Windows, use WSL or download from curl.se."

**[0:30-1:30] TIP 1-2: BASIC GET & HEAD**

"Tip 1: The simplest request

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

That's it. One command, JSON response.

Tip 2: Just headers, please

```bash
curl -I https://jsonplaceholder.typicode.com/posts/1
```

The -I flag gives you only the HTTP headers. Great for checking status codes, content-type, and cache headers without downloading the body."

**[1:30-2:30] TIP 3-4: POST WITH DATA**

"Tip 3: POST a JSON body

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"My Post","body":"Content here","userId":1}'
```

Three flags:
- -X POST specifies the method
- -H sets a header (always set Content-Type for JSON APIs)
- -d is the request body

Tip 4: Pretty print the response

```bash
curl -s https://jsonplaceholder.typicode.com/posts/1 | python3 -m json.tool
```

The -s flag silences the progress meter. Pipe to jq or python -m json.tool for pretty formatting."

**[2:30-3:30] TIP 5-6: AUTH & HEADERS**

"Tip 5: Bearer token authentication

```bash
curl https://api.github.com/user \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

Tip 6: Custom headers

```bash
curl https://api.example.com/data \
  -H "Accept: application/json" \
  -H "X-API-Key: your-key-here" \
  -H "User-Agent: MyApp/1.0"
```

Different APIs need different headers. The -H flag is your best friend."

**[3:30-4:30] TIP 7-8: SAVE & UPLOAD**

"Tip 7: Save response to file

```bash
curl -s https://api.example.com/large-data -o response.json
```

-o saves to a file. Essential for large responses.

Tip 8: Upload a JSON file

```bash
curl -X POST https://api.example.com/upload \
  -H "Content-Type: application/json" \
  -d @data.json
```

The @ symbol tells cURL to read from a file instead of the command line."

**[4:30-5:30] TIP 9-10: FOLLOW & DEBUG**

"Tip 9: Follow redirects

```bash
curl -L https://short.url/abc123
```

The -L flag follows HTTP redirects. Always use this if you expect redirects.

Tip 10: Verbose mode for debugging

```bash
curl -v https://api.example.com/secure \
  -H "Authorization: Bearer token"
```

The -v flag shows everything: request headers, response headers, status code. When something breaks, this is the first thing to try."

**[5:30-7:00] BONUS: CHAINED REQUESTS**

"Here's a real-world workflow — get a token, then use it:

```bash
# Step 1: Login and extract token
TOKEN=$(curl -s -X POST https://api.example.com/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"secret"}' \
  | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

# Step 2: Use the token
curl -H "Authorization: Bearer $TOKEN" \
  https://api.example.com/protected
```

In bash, you can chain these. Login → extract token → use token for authenticated requests."

**[7:00-8:00] SUMMARY**

"10 tips in 8 minutes:

1. Basic GET — just the URL
2. Headers only — use -I
3. POST with JSON — use -H and -d
4. Pretty print — pipe to jq or json.tool
5. Bearer auth — Authorization header
6. Custom headers — multiple -H flags
7. Save to file — use -o
8. Upload file — use @filename
9. Follow redirects — use -L
10. Debug everything — use -v

Bookmark this video. You'll come back to it.

Try it yourself at aijsons.com/tools/curl — or just open your terminal."

---

## 视频 #4: JSON Formatter — 60 秒演示

**标题**: JSON Formatter: Format, Validate & Minify in 60 Seconds
**时长**: 5 分钟（300 秒）

### 脚本正文

**[0:00-0:10] HOOK**

"Sixty seconds. That's all you need to master JSON formatting."

**[0:10-0:20] DEMO START**

"Open aijsons.com/format — I'll show you everything."

**[0:20-1:30] FORMAT**

"Step 1: Paste any JSON. Messy, minified, whatever. Hit Format."

**[1:30-2:30] VALIDATE**

"Step 2: Try the validator. I'll break the JSON. See the error? Line number and everything."

**[2:30-3:30] MINIFY**

"Step 3: Click Minify. The same JSON, compressed. Ready for production."

**[3:30-4:30] SYNTAX HIGHLIGHTING**

"Notice the colors — strings, numbers, booleans, keys all different. That's syntax highlighting."

**[4:30-5:00] CTA**

"aijsons.com/format. Free, no signup, instant. Link in the description."
