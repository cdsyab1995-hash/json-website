"""
修复博客/新闻页面内联 <style> 中缺少的 CSS 颜色属性。
问题：.article-content p 和 .article-content li 没有设置 color
修复：为它们添加 color: var(--text-secondary) 保持与 styles.css 一致
"""

import re
import os

# 需要修复的文件列表
FILES_TO_FIX = [
    # Blog - 有内联 <style> 且缺少 p/li color 的页面
    "d:/网站开发-json/blog/zod-json-schema-validation-ai/index.html",
    "d:/网站开发-json/blog/json-parsing-performance-comparison/index.html",
    "d:/网站开发-json/blog/mcp-json-standardizing-ai-tools/index.html",
    "d:/网站开发-json/blog/json-api-error-handling-2026/index.html",
    "d:/网站开发-json/blog/json-schema-complete-guide-2026/index.html",
    "d:/网站开发-json/blog/ai-tool-calling-mcp-2026/index.html",
    # News
    "d:/网站开发-json/news/json-schema-w3c-recommendation/index.html",
    # News - 使用 article-body 的页面
    "d:/网站开发-json/news/openai-agents-sdk-json-strict-mode/index.html",
    "d:/网站开发-json/news/api-transformations-2026/index.html",
    # Blog - 使用 article-body 的旧文件
    "d:/网站开发-json/blog/curl-json-api-guide.html",
    "d:/网站开发-json/blog/json-patch-vs-merge-patch.html",
    "d:/网站开发-json/blog/json-performance-optimization-2026/index.html",
]

def fix_article_content_color(file_path):
    """修复单个文件中的 article-content 颜色问题"""
    if not os.path.exists(file_path):
        print(f"  ⚠️  文件不存在: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changed = False
    
    # 检查是否有 article-content 或 article-body 相关的内联样式
    if 'article-content' not in content and 'article-body' not in content:
        print(f"  ⏭️  无 article 相关类，跳过")
        return False
    
    # 修复 1: .article-content p -> 添加 color
    # 匹配 .article-content p{...} 但其中没有 color 的情况
    if '.article-content p{' in content:
        # 查找 .article-content p{...} 块
        pattern = r'(\.article-content p\{[^}]*?)(margin-bottom[^}]*?\}'
        def add_color_to_p(match):
            group = match.group(1)
            rest = match.group(2)
            # 如果没有 color 属性，添加 color
            if 'color:' not in group:
                return group + 'color:var(--text-secondary);' + rest
            return match.group(0)
        new_content = re.sub(pattern, add_color_to_p, content)
        if new_content != content:
            content = new_content
            changed = True
    
    # 更简单的方法：直接替换 "color:var(--primary);" 后的内容
    # 对于 .article-content p{margin-bottom:1rem} -> 添加 color:var(--text-secondary);
    
    # 修复模式：在 .article-content p{...} 中添加 color
    # 匹配不含 color 的 .article-content p 规则
    def fix_article_p(match):
        full_rule = match.group(0)
        # 如果已经有 color，跳过
        if 'color:' in full_rule:
            return full_rule
        # 在第一个 } 前插入 color
        return full_rule.replace('{', '{color:var(--text-secondary);', 1)
    
    content = re.sub(r'\.article-content p\{[^}]+\}', fix_article_p, content)
    
    # 修复模式：在 .article-content li{...} 中添加 color
    def fix_article_li(match):
        full_rule = match.group(0)
        if 'color:' in full_rule:
            return full_rule
        return full_rule.replace('{', '{color:var(--text-secondary);', 1)
    
    content = re.sub(r'\.article-content li\{[^}]+\}', fix_article_li, content)
    
    # 同样处理 article-body
    def fix_article_body_p(match):
        full_rule = match.group(0)
        if 'color:' in full_rule:
            return full_rule
        return full_rule.replace('{', '{color:var(--text-secondary);', 1)
    
    content = re.sub(r'\.article-body p\{[^}]+\}', fix_article_body_p, content)
    
    def fix_article_body_li(match):
        full_rule = match.group(0)
        if 'color:' in full_rule:
            return full_rule
        return full_rule.replace('{', '{color:var(--text-secondary);', 1)
    
    content = re.sub(r'\.article-body li\{[^}]+\}', fix_article_body_li, content)
    
    # 最彻底的方案：如果 article-content 本身没有 color，添加一个
    # 匹配 .article-content{...} 中没有 color 的
    def fix_article_content_color(match):
        full_rule = match.group(0)
        if 'color:' in full_rule:
            return full_rule
        # 在 { 后添加 color
        return full_rule.replace('{', '{color:var(--text-secondary);', 1)
    
    content = re.sub(r'\.article-content\{[^}]+\}', fix_article_content_color, content)
    content = re.sub(r'\.article-body\{[^}]+\}', fix_article_content_color, content)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ 已修复: {os.path.basename(os.path.dirname(file_path) or file_path)}")
        return True
    else:
        print(f"  ⏭️  无需修复或已正确")
        return False


def main():
    print("🔧 修复博客/新闻页面文章正文字体颜色\n")
    print(f"将修复 {len(FILES_TO_FIX)} 个文件\n")
    
    fixed_count = 0
    for fp in FILES_TO_FIX:
        print(f"处理: {fp}")
        if fix_article_content_color(fp):
            fixed_count += 1
    
    print(f"\n完成！修复了 {fixed_count}/{len(FILES_TO_FIX)} 个文件")


if __name__ == "__main__":
    main()
