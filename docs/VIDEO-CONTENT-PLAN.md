# 视频内容规划

> AIJSONS.COM - YouTube 频道视频计划
> 更新：2026-04-18

---

## 频道定位

- **目标用户**：全球开发者，尤其是后端/全栈工程师
- **内容风格**：技术深度 + 实用导向，每期解决一个具体问题
- **视频时长**：5-15 分钟（移动端友好）
- **更新节奏**：每周 1-2 个视频

---

## 10 个视频选题

### 第1批（易制作，快速上线）

| # | 标题 | 时长 | 难度 | 配套文章 | 脚本状态 |
|---|------|------|------|---------|---------|
| 1 | **What is JSON? 5-Minute Beginner Guide** | 5min | 初级 | JSON 入门 | ✅ 草稿完成 |
| 2 | **JSON vs XML vs YAML - One Video to Decide** | 8min | 初级 | 对比文章 | 🔨 编写中 |
| 3 | **10 cURL Tips for JSON APIs** | 8min | 中级 | curl JSON Guide | 📋 计划中 |

### 第2批（核心工具演示）

| # | 标题 | 时长 | 难度 | 配套文章 | 脚本状态 |
|---|------|------|------|---------|---------|
| 4 | **JSON Formatter: Format, Validate & Minify in 60 Seconds** | 5min | 初级 | format.html | 📋 计划中 |
| 5 | **JSON Compare: Find Differences Between Two JSON Files** | 6min | 初级 | compare.html | 📋 计划中 |
| 6 | **JSON to CSV: Export Any JSON to Excel** | 5min | 初级 | json2csv.html | 📋 计划中 |

### 第3批（深度技术）

| # | 标题 | 时长 | 难度 | 配套文章 | 脚本状态 |
|---|------|------|------|---------|---------|
| 7 | **JSON Patch vs Merge Patch - Which One to Use?** | 10min | 中级 | JSON Patch 文章 | 📋 计划中 |
| 8 | **JSON Schema Tutorial: From Zero to Production** | 12min | 中级 | JSON Schema Guide | 📋 计划中 |
| 9 | **JSON API Error Handling: Stop Returning 200 + Error** | 8min | 中级 | API Error 文章 | 📋 计划中 |
| 10 | **MCP + JSON: How AI Tools Talk to Each Other** | 10min | 高级 | MCP 文章 | 📋 计划中 |

---

## 录制脚本模板

### 开头模板（每期使用）

```
[0:00-0:15] HOOK
"Most developers use JSON wrong. In the next X minutes, I'll show you exactly why — and how to fix it."

[0:15-0:30] AGENDA  
"Today we'll cover three things: [topic 1], [topic 2], and [topic 3]. Let's dive in."

[0:30-...] BODY
```

### 结尾模板（每期使用）

```
[End - 0:30] SUMMARY
"Here's what we covered today: [3 bullet points]"

[End - 0:15] CTA
"If you found this useful, hit like and subscribe. And try it yourself at aijsons.com — link in the description."

[End] OUTRO
"See you in the next one. Happy coding!"
```

---

## 视频 #1 完整脚本

**标题**: What is JSON? 5-Minute Beginner Guide for Developers
**目标关键词**: json tutorial, what is json, json for beginners
**配套文章**: Blog 文章 - JSON 入门
**时长**: 5 分钟（300 秒）

### 脚本正文

---

**[0:00-0:15] HOOK**

"Every API you've ever used — Twitter, Stripe, GitHub — they all speak the same language. And after this 5-minute video, you'll master it."

**[0:15-0:30] AGENDA**

"By the end, you'll know what JSON is, why it exists, how to read it, and how to use it in your code. Let's go."

**[0:30-1:30] WHAT IS JSON?**

"JSON stands for JavaScript Object Notation. But here's the thing — it has nothing to do with JavaScript anymore. It's a universal data format that every language can read and write.

Think of it as a way to structure data as text. Here's the simplest example:

```
{
  "name": "John",
  "age": 30,
  "isDeveloper": true
}
```

That's it. It's just key-value pairs — like a dictionary in Python, a Map in Java, or an object in JavaScript.

Notice a few things:
- Keys are always strings, wrapped in quotes
- Values can be strings, numbers, booleans, arrays, objects, or null
- There's no trailing comma at the end — that's a common mistake"

**[1:30-2:30] WHY JSON AND NOT XML?**

"You might be thinking — we've had XML for decades. Why did JSON take over?

Three reasons:

**1. It's simpler.** XML has opening and closing tags, attributes, namespaces. JSON is just key-value pairs.

**2. It's smaller.** A JSON payload is typically 20-30% smaller than the equivalent XML.

**3. It's native to JavaScript.** Since JSON is derived from JavaScript object syntax, parsing it in JS is literally one function call."

**[2:30-3:45] COMMON DATA TYPES**

"Let me show you all the data types JSON supports:

```
{
  "string": "Hello World",
  "number": 42,
  "decimal": 3.14,
  "boolean": true,
  "null": null,
  "array": [1, 2, 3],
  "object": { "key": "value" },
  "nested": {
    "user": {
      "name": "Sarah",
      "skills": ["JavaScript", "Python", "Go"]
    }
  }
}
```

See that nested object? That's how you represent complex data structures. And arrays can contain anything — numbers, strings, objects, even other arrays.

The key rule: arrays are ordered, objects are unordered."

**[3:45-4:30] HOW TO USE IT IN CODE**

"Here's how you parse JSON in the most common languages.

JavaScript:
```javascript
const data = JSON.parse(jsonString);
const jsonString = JSON.stringify(data);
```

Python:
```python
import json
data = json.loads(json_string)
json_string = json.dumps(data)
```

Go:
```go
import "encoding/json"
var data map[string]interface{}
json.Unmarshal([]byte(jsonString), &data)
```

One function to read, one to write. That's all you need."

**[4:30-5:00] SUMMARY & CTA**

"Here's what we covered:
1. JSON is a universal text format for structured data
2. It's simpler and smaller than XML
3. Every language has built-in functions to parse and generate it

Now try it yourself. Go to aijsons.com — the link is in the description. You can format, validate, and minify JSON for free, right in your browser.

If this was useful, hit like and subscribe. See you in the next one."

---

## 录制安排

### 第一周（4月21-25日）
- 周一：录制视频 #1（JSON 入门）
- 周三：录制视频 #2（JSON vs XML vs YAML）
- 周五：录制视频 #3（10 cURL Tips）

### 第二周（4月28-5月2日）
- 周一：录制视频 #4（JSON Formatter 演示）
- 周三：录制视频 #5（JSON Compare 演示）
- 周五：录制视频 #6（JSON to CSV 演示）

### 第三周（5月5-9日）
- 周一：录制视频 #7（JSON Patch）
- 周三：录制视频 #8（JSON Schema）

### 第四周（5月12-16日）
- 周一：录制视频 #9（API 错误处理）
- 周三：录制视频 #10（MCP + JSON）

---

## 技术设置

### 录制工具
- **录制**: OBS Studio（免费，跨平台）
- **剪辑**: DaVinci Resolve（免费）
- **提词器**: OBS + Window Capture 或 Teleprompter Timer App

### 显示设置
- **分辨率**: 1920x1080
- **帧率**: 30fps
- **编码**: H.264 (NVENC 如果有独显)
- **码率**: 8-12 Mbps

### 音频设置
- **采样率**: 48kHz
- **麦克风**: 独立 USB 麦克风优先
- **降噪**: Adobe Audition 或 Audacity

### 演示代码
- 使用 VS Code + Syntax Highlight Theme
- 字体：JetBrains Mono（代码），Inter（PPT/标题）
- 终端：Windows Terminal 或 iTerm2
