#!/usr/bin/env python3
"""
复制所有工具页面到 tools/ 目录，使用干净的 slug URL
pages/format.html -> tools/json-formatter.html
"""

import os
import re
import shutil
from pathlib import Path

# 工具页面映射：filename -> slug
TOOL_MAPPING = {
    'format.html': 'json-formatter',
    'escape.html': 'json-escape',
    'extract.html': 'json-extract',
    'sort.html': 'json-sort',
    'clean.html': 'json-clean',
    'xml.html': 'json-to-xml',
    'yaml.html': 'json-to-yaml',
    'viewer.html': 'json-viewer',
    'json2csv.html': 'json-to-csv',
    'compare.html': 'json-compare',
    'csv-to-excel.html': 'csv-to-excel',
    'merge-csv.html': 'merge-csv',
    'excel-remove-duplicates.html': 'excel-remove-duplicates',
    'css-minifier.html': 'css-minifier',
    'html-encoder.html': 'html-encoder',
    'url-encoder.html': 'url-encoder',
    'base64.html': 'base64',
    'jwt-decoder.html': 'jwt-decoder',
    'regex-tester.html': 'regex-tester',
    'uuid-generator.html': 'uuid-generator',
    'timestamp-converter.html': 'timestamp-converter',
    'hash-generator.html': 'hash-generator',
    'pdf-split.html': 'pdf-split',
    'batch-file-renamer.html': 'batch-renamer',
}

# 所有工具的 slug 列表（用于导航栏）
ALL_TOOL_SLUGS = list(TOOL_MAPPING.values())

# 导航栏工具链接映射（slug -> slug，用于生成链接）
NAV_TOOL_LINKS = {slug: slug for slug in ALL_TOOL_SLUGS}

def process_html_content(content, current_slug, tool_mapping):
    """处理 HTML 内容，修复所有路径"""
    
    # 修复 ../css/ -> /css/
    content = re.sub(r'href="\.\./css/', 'href="/css/', content)
    
    # 修复 ../js/ -> /js/
    content = re.sub(r'href="\.\./js/', 'href="/js/', content)
    
    # 修复 ../images/ -> /images/
    content = re.sub(r'href="\.\./images/', 'href="/images/', content)
    
    # 修复 src="../css/ -> /css/
    content = re.sub(r'src="\.\./css/', 'src="/css/', content)
    content = re.sub(r'src="\.\./js/', 'src="/js/', content)
    
    # 修复页脚链接 ../xxx.html -> /xxx
    content = re.sub(r'href="\.\./privacy\.html"', 'href="/privacy"', content)
    content = re.sub(r'href="\.\./terms\.html"', 'href="/terms"', content)
    content = re.sub(r'href="\.\./cookie\.html"', 'href="/cookie"', content)
    
    # 修复工具页面链接格式
    # href="xxx.html" -> href="/tools/slug" (for tool pages only)
    for filename, slug in tool_mapping.items():
        # 匹配 href="xxx.html" 或 href="./xxx.html"
        content = re.sub(
            rf'href="/?{re.escape(filename)}"',
            f'href="/tools/{slug}"',
            content
        )
    
    # 修复博客链接
    content = re.sub(r'href="blog\.html"', 'href="/blog"', content)
    content = re.sub(r'href="\.\./blog\.html"', 'href="/blog"', content)
    
    # 修复新闻链接
    content = re.sub(r'href="news\.html"', 'href="/news"', content)
    content = re.sub(r'href="\.\./news\.html"', 'href="/news"', content)
    
    # 修复博客子页面链接
    content = re.sub(r'href="blog/(.+?)\.html"', r'href="/blog/\1"', content)
    content = re.sub(r'href="\.\./blog/(.+?)\.html"', r'href="/blog/\1"', content)
    
    # 修复新闻子页面链接
    content = re.sub(r'href="news/(.+?)\.html"', r'href="/news/\1"', content)
    content = re.sub(r'href="\.\./news/(.+?)\.html"', r'href="/news/\1"', content)
    
    # 修复静态页面链接
    content = re.sub(r'href="about\.html"', 'href="/about"', content)
    content = re.sub(r'href="changelog\.html"', 'href="/changelog"', content)
    content = re.sub(r'href="best-practices\.html"', 'href="/best-practices"', content)
    content = re.sub(r'href="\.\./about\.html"', 'href="/about"', content)
    content = re.sub(r'href="\.\./changelog\.html"', 'href="/changelog"', content)
    content = re.sub(r'href="\.\./best-practices\.html"', 'href="/best-practices"', content)
    
    # 修复相关工具链接 (Related Tools section)
    # href="format.html" -> href="/tools/json-formatter"
    for filename, slug in tool_mapping.items():
        content = re.sub(
            rf'(href=")([^"]*?)(format\.html|escape\.html|extract\.html|sort\.html|clean\.html|xml\.html|yaml\.html|viewer\.html|json2csv\.html|compare\.html|csv-to-excel\.html|merge-csv\.html|excel-remove-duplicates\.html|css-minifier\.html|html-encoder\.html|url-encoder\.html|base64\.html|jwt-decoder\.html|regex-tester\.html|uuid-generator\.html|timestamp-converter\.html|hash-generator\.html|pdf-split\.html|batch-file-renamer\.html)(")',
            lambda m: f'{m.group(1)}/tools/{tool_mapping.get(m.group(2), m.group(2).replace(".html", ""))}{m.group(3)}',
            content
        )
    
    # 修复 canonical 链接
    content = re.sub(
        r'<link rel="canonical" href="[^"]*?/pages/([^"]+?)\.html"',
        lambda m: f'<link rel="canonical" href="https://www.aijsons.com/tools/{TOOL_MAPPING.get(m.group(1), m.group(1))}"',
        content
    )
    
    # 修复 JSON-LD url
    content = re.sub(
        r'"url"\s*:\s*"[^"]*?/pages/([^"]+?)\.html"',
        lambda m: f'"url": "https://www.aijsons.com/tools/{TOOL_MAPPING.get(m.group(1), m.group(1))}"',
        content
    )
    
    # 修复 og:url
    content = re.sub(
        r'<meta property="og:url" content="[^"]*?/pages/([^"]+?)\.html"',
        lambda m: f'<meta property="og:url" content="https://www.aijsons.com/tools/{TOOL_MAPPING.get(m.group(1), m.group(1))}"',
        content
    )
    
    return content


def main():
    base_dir = Path('d:/网站开发-json')
    pages_dir = base_dir / 'pages'
    tools_dir = base_dir / 'tools'
    
    # 创建 tools 目录
    tools_dir.mkdir(exist_ok=True)
    
    count = 0
    for filename, slug in TOOL_MAPPING.items():
        source_file = pages_dir / filename
        target_file = tools_dir / f'{slug}.html'
        
        if not source_file.exists():
            print(f"[SKIP] {filename} not found")
            continue
        
        # 读取源文件
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 处理内容
        new_content = process_html_content(content, slug, TOOL_MAPPING)
        
        # 写入目标文件
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        count += 1
        print(f"[OK] {filename} -> tools/{slug}.html")
    
    print(f"\n总计：{count} 个工具页面已复制到 tools/ 目录")
    
    # 更新 _redirects 文件
    redirects_file = base_dir / '_redirects'
    with open(redirects_file, 'r', encoding='utf-8') as f:
        redirects_content = f.read()
    
    # 添加新的重定向规则（工具页面）
    new_redirects = []
    for filename, slug in TOOL_MAPPING.items():
        old_url = f'/pages/{filename}'
        new_url = f'/tools/{slug}'
        # 检查是否已存在
        if old_url not in redirects_content:
            new_redirects.append(f'{old_url}    {new_url}')
    
    if new_redirects:
        with open(redirects_file, 'a', encoding='utf-8') as f:
            f.write('\n# Tool pages (clean URL)\n')
            for rule in new_redirects:
                f.write(rule + '\n')
        print(f"已更新 _redirects，添加 {len(new_redirects)} 条规则")
    else:
        print("_redirects 已包含所有工具页面规则")


if __name__ == '__main__':
    main()
