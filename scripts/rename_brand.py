import os
import re

repo_path = r"d:\网站开发-json"
old_text = "JSON Web Tools"
new_text = "AI JSON"

html_files = [
    r"d:\网站开发-json\index.html",
    r"d:\网站开发-json\pages\format.html",
    r"d:\网站开发-json\pages\escape.html",
    r"d:\网站开发-json\pages\extract.html",
    r"d:\网站开发-json\pages\sort.html",
    r"d:\网站开发-json\pages\clean.html",
    r"d:\网站开发-json\pages\xml.html",
    r"d:\网站开发-json\pages\yaml.html",
    r"d:\网站开发-json\pages\viewer.html",
    r"d:\网站开发-json\pages\blog.html",
    r"d:\网站开发-json\pages\news.html",
    r"d:\网站开发-json\pages\json2csv.html",
    r"d:\网站开发-json\pages\compare.html",
]

count = 0
for file_path in html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_text in content:
            new_content = content.replace(old_text, new_text)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] {os.path.basename(file_path)}")
            count += 1

print(f"\n[OK] Updated {count} files")

# Also update CNAME to use root domain
cname_path = r"d:\网站开发-json\CNAME"
with open(cname_path, 'w', encoding='utf-8') as f:
    f.write("aijsons.com\nwww.aijsons.com")
print("[OK] Updated CNAME")
