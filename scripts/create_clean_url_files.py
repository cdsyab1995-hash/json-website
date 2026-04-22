# -*- coding: utf-8 -*-
"""创建无后缀文件

将 pages/ 目录下的 HTML 文件复制到根目录，去掉 .html 后缀
并修复内部相对路径

需要复制的文件：
- pages/best-practices.html -> best-practices.html
- pages/blog.html -> blog.html
- pages/news.html -> news.html
- pages/about.html -> about.html
- pages/changelog.html -> changelog.html
- pages/privacy.html -> privacy.html
- pages/terms.html -> terms.html
- pages/cookie.html -> cookie.html

对于 pages/tools/ 子目录下的工具页：
- pages/format.html -> tools/json-formatter/index.html (SPA 方式)
"""
import os
import re
import shutil

# 需要复制到根目录的文件（去掉 .html）
FILES_TO_COPY = [
    'about.html',
    'blog.html',
    'changelog.html',
    'cookie.html',
    'privacy.html',
    'terms.html',
    'news.html',
    'best-practices.html',
]

def fix_relative_paths(content, from_dir='pages', to_root=True):
    """修复相对路径
    
    从 pages/ 目录到根目录：
    - href="format.html" -> href="/tools/json-formatter" (如果是工具页)
    - href="css/xxx" -> href="/css/xxx"
    - href="../css/xxx" -> href="/css/xxx"
    - href="../js/xxx" -> href="/js/xxx"
    - src="../css/xxx" -> src="/css/xxx"
    - src="../js/xxx" -> src="/js/xxx"
    """
    
    # URL 映射
    URL_MAPPINGS = {
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
        'blog.html': '/blog',
        'news.html': '/news',
        'about.html': '/about',
        'changelog.html': '/changelog',
        'best-practices.html': '/best-practices',
        'privacy.html': '/privacy',
        'terms.html': '/terms',
        'cookie.html': '/cookie',
    }
    
    new_content = content
    
    # 替换 href="xxx.html" 为 /tools/xxx 或 /xxx
    for old_path, new_url in URL_MAPPINGS.items():
        pattern = r'href="(' + re.escape(old_path) + r')"'
        replacement = f'href="{new_url}"'
        new_content = re.sub(pattern, replacement, new_content)
    
    # 替换 href="blog/xxx.html" 为 /blog/xxx
    new_content = re.sub(
        r'href="blog/([^"]+\.html)"',
        r'href="/blog/\1"',
        new_content
    )
    new_content = re.sub(
        r'href="/blog/([^"]+\.html)"',
        r'href="/blog/\1"',
        new_content
    )
    # 去掉 blog 下的 .html 后缀
    new_content = re.sub(
        r'href="/blog/([^"]+)\.html"',
        r'href="/blog/\1"',
        new_content
    )
    
    # 替换 href="news/xxx.html" 为 /news/xxx
    new_content = re.sub(
        r'href="news/([^"]+\.html)"',
        r'href="/news/\1"',
        new_content
    )
    new_content = re.sub(
        r'href="/news/([^"]+\.html)"',
        r'href="/news/\1"',
        new_content
    )
    # 去掉 news 下的 .html 后缀
    new_content = re.sub(
        r'href="/news/([^"]+)\.html"',
        r'href="/news/\1"',
        new_content
    )
    
    # 修复 ../css/ -> /css/
    new_content = re.sub(r'href="\.\./css/', 'href="/css/', new_content)
    new_content = re.sub(r'href="\.\./js/', 'href="/js/', new_content)
    new_content = re.sub(r'href="\.\./images/', 'href="/images/', new_content)
    
    # 修复 src="../css/ -> /css/
    new_content = re.sub(r'src="\.\./css/', 'src="/css/', new_content)
    new_content = re.sub(r'src="\.\./js/', 'src="/js/', new_content)
    
    # 修复页脚的 ../privacy.html 等
    new_content = re.sub(r'href="\.\./privacy\.html"', 'href="/privacy"', new_content)
    new_content = re.sub(r'href="\.\./terms\.html"', 'href="/terms"', new_content)
    new_content = re.sub(r'href="\.\./cookie\.html"', 'href="/cookie"', new_content)
    
    # 修复 href="css/ -> /css/
    new_content = re.sub(r'href="css/', 'href="/css/', new_content)
    new_content = re.sub(r'href="js/', 'href="/js/', new_content)
    new_content = re.sub(r'href="images/', 'href="/images/', new_content)
    
    # 修复 src="css/ -> /css/
    new_content = re.sub(r'src="css/', 'src="/css/', new_content)
    new_content = re.sub(r'src="js/', 'src="/js/', new_content)
    
    return new_content

def copy_and_fix_files():
    """复制并修复文件"""
    base_dir = r"d:\网站开发-json\pages"
    root_dir = r"d:\网站开发-json"
    
    count = 0
    
    for filename in FILES_TO_COPY:
        src = os.path.join(base_dir, filename)
        if not os.path.exists(src):
            print(f"[SKIP] {filename} not found")
            continue
        
        # 目标文件名（去掉 .html）
        dst_name = filename.replace('.html', '')
        dst = os.path.join(root_dir, dst_name)
        
        # 读取源文件
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复路径
        content = fix_relative_paths(content)
        
        # 写入目标文件
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] Created: {dst_name}")
        count += 1
    
    print(f"\nTotal files created: {count}")
    return count

if __name__ == "__main__":
    print("=" * 50)
    print("Creating clean URL files (without .html extension)")
    print("=" * 50)
    count = copy_and_fix_files()
    print("\nDone!")
