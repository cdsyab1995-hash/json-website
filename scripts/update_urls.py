# -*- coding: utf-8 -*-
import os
import re

base_dir = r"d:\网站开发-json"
old_domain = "cdsyab1995-hash.github.io/json-website"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace old domain with new
            new_content = content.replace(old_domain, 'aijsons.com')
            
            # Remove hreflang tags (both zh and en alternates)
            new_content = re.sub(r'\s*<link[^>]*hreflang="zh"[^>]*>\s*', '\n', new_content)
            new_content = re.sub(r'\s*<link[^>]*hreflang="en"[^>]*>\s*', '\n', new_content)
            
            # Replace -en.html with .html in URLs
            new_content = re.sub(r'(\w+)-en(\.html)', r'\1\2', new_content)
            
            # Remove any duplicate newlines
            new_content = re.sub(r'\n\s*\n', '\n', new_content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated: {filepath}")

print("Done!")
