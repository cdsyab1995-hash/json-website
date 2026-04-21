# -*- coding: utf-8 -*-
"""修复页面内链接为干净的 URL（去掉 .html 后缀）

pages/ 目录下的文件：
- format.html → /tools/json-formatter
- blog.html → /blog
- news.html → /news
- about.html → /about
等

pages/news/ 和 pages/blog/ 子目录：
- ../blog.html → /blog
- ../news.html → /news
等
"""
import os
import re

# URL 映射规则
# 格式：(旧路径, 新路径)
URL_MAPPINGS = {
    # 工具页
    'format.html': '/tools/json-formatter',
    'escape.html': '/tools/json-escape',
    'extract.html': '/tools/json-extract',
    'sort.html': '/tools/json-sort',
    'clean.html': '/tools/json-clean',
    'xml.html': '/tools/json-to-xml',
    'yaml.html': '/tools/json-to-yaml',
    'viewer.html': '/tools/json-viewer',
    'json2csv.html': '/tools/json-to-csv',
    'compare.html': '/tools/json-compare',
    'csv-to-excel.html': '/tools/csv-to-excel',
    'merge-csv.html': '/tools/merge-csv',
    'excel-remove-duplicates.html': '/tools/excel-remove-duplicates',
    'css-minifier.html': '/tools/css-minifier',
    'html-encoder.html': '/tools/html-encoder',
    'url-encoder.html': '/tools/url-encoder',
    'base64.html': '/tools/base64',
    'jwt-decoder.html': '/tools/jwt-decoder',
    'regex-tester.html': '/tools/regex-tester',
    'uuid-generator.html': '/tools/uuid-generator',
    'timestamp-converter.html': '/tools/timestamp-converter',
    'hash-generator.html': '/tools/hash-generator',
    'pdf-split.html': '/tools/pdf-split',
    'batch-file-renamer.html': '/tools/batch-renamer',
    # 静态页
    'blog.html': '/blog',
    'news.html': '/news',
    'about.html': '/about',
    'changelog.html': '/changelog',
    'best-practices.html': '/best-practices',
    'privacy.html': '/privacy',
    'terms.html': '/terms',
    'cookie.html': '/cookie',
    # blog 子目录
    'ai-tool-calling-mcp-2026.html': '/blog/ai-tool-calling-mcp-2026',
    'compare-json-documents-find-differences.html': '/blog/compare-json-documents-find-differences',
    'curl-json-api-guide.html': '/blog/curl-json-api-guide',
    'json-api-error-handling-2026.html': '/blog/json-api-error-handling-2026',
    'json-edge-computing-cloudflare-workers.html': '/blog/json-edge-computing-cloudflare-workers',
    'json-parsing-performance-comparison.html': '/blog/json-parsing-performance-comparison',
    'json-patch-vs-merge-patch.html': '/blog/json-patch-vs-merge-patch',
    'json-schema-complete-guide-2026.html': '/blog/json-schema-complete-guide-2026',
    'jwt-security-best-practices-2026.html': '/blog/jwt-security-best-practices-2026',
    'mcp-json-standardizing-ai-tools.html': '/blog/mcp-json-standardizing-ai-tools',
    'model-context-protocol-json-rpc-ai-tools.html': '/blog/model-context-protocol-json-rpc-ai-tools',
    'postgresql-jsonb-vs-mongodb-document-store.html': '/blog/postgresql-jsonb-vs-mongodb-document-store',
    'sort-json-arrays-objects-guide.html': '/blog/sort-json-arrays-objects-guide',
    'zod-json-schema-validation-ai.html': '/blog/zod-json-schema-validation-ai',
    # news 子目录
    'mcp-10000-servers.html': '/news/mcp-10000-servers',
    'browser-devtools-json-schema.html': '/news/browser-devtools-json-schema',
    'bun-2-json-serialization.html': '/news/bun-2-json-serialization',
    'json-streaming-api-browser.html': '/news/json-streaming-api-browser',
    'cursor-vscode-json-lint-ai.html': '/news/cursor-vscode-json-lint-ai',
    'zod-v4-5m-downloads.html': '/news/zod-v4-5m-downloads',
    'nextjs-16-json-streaming.html': '/news/nextjs-16-json-streaming',
    'nodejs-24-json-schema.html': '/news/nodejs-24-json-schema',
    'json-schema-to-typescript-v6.html': '/news/json-schema-to-typescript-v6',
    'jsonata-2-ai-query.html': '/news/jsonata-2-ai-query',
    'json-schema-w3c-recommendation.html': '/news/json-schema-w3c-recommendation',
    'api-transformations-2026.html': '/news/api-transformations-2026',
}

def fix_pages_directory():
    """修复 pages/ 目录下的 HTML 文件"""
    pages_dir = r"d:\网站开发-json\pages"
    fixed_count = 0
    
    for filename in os.listdir(pages_dir):
        if not filename.endswith('.html'):
            continue
        # 跳过子目录
        if '/' in filename or '\\' in filename:
            continue
            
        filepath = os.path.join(pages_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        
        # 替换 href="xxx.html" 为对应的干净 URL
        for old_path, new_url in URL_MAPPINGS.items():
            # 避免替换已经正确的 URL
            if old_path == filename:
                continue
            # 匹配 href="xxx.html" 但不匹配 href="//xxx.html" 或 href="https://..."
            pattern = r'href="(' + re.escape(old_path) + r')"'
            replacement = f'href="{new_url}"'
            new_content = re.sub(pattern, replacement, new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Fixed: {filename}")
            fixed_count += 1
    
    print(f"\nTotal files fixed in pages/: {fixed_count}")
    return fixed_count

def fix_subdirectories():
    """修复子目录（news/, blog/）下的 HTML 文件"""
    base_dir = r"d:\网站开发-json\pages"
    fixed_count = 0
    
    for subdir in ['news', 'blog']:
        subdir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(subdir_path):
            continue
        
        for filename in os.listdir(subdir_path):
            if not filename.endswith('.html'):
                continue
            
            filepath = os.path.join(subdir_path, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            # 子目录需要用 ../ 相对路径
            # href="../blog.html" → href="/blog"
            for old_path, new_url in URL_MAPPINGS.items():
                # 跳过子目录自身的文章页面
                if old_path == filename:
                    continue
                pattern = r'href="\.\./(' + re.escape(old_path) + r')"'
                replacement = f'href="{new_url}"'
                new_content = re.sub(pattern, replacement, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"[OK] Fixed: {subdir}/{filename}")
                fixed_count += 1
    
    print(f"\nTotal files fixed in subdirectories: {fixed_count}")
    return fixed_count

if __name__ == "__main__":
    print("=" * 50)
    print("Fixing internal links to clean URLs")
    print("=" * 50)
    
    count1 = fix_pages_directory()
    count2 = fix_subdirectories()
    
    print("\n" + "=" * 50)
    print(f"Grand total: {count1 + count2} files fixed")
    print("=" * 50)
