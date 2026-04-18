# Analysis script for page structure
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    r'd:\网站开发-json\pages\format.html',
    r'd:\网站开发-json\pages\json2csv.html', 
    r'd:\网站开发-json\pages\compare.html',
    r'd:\网站开发-json\pages\viewer.html'
]

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"\n{'='*60}")
        print(f"File: {page.split('\\')[-1]}")
        print(f"Length: {len(content)} chars")
        
        # Find main sections
        main_start = content.find('<main')
        main_end = content.find('</main>')
        
        print(f"<main start: {main_start}")
        print(f"</main> end: {main_end}")
        
        if main_end > 0:
            # Show what's between </main> and </body>
            body_start = content.find('</body>')
            between = content[main_end:body_start] if body_start > 0 else content[main_end:main_end+500]
            print(f"After </main> ({len(between)} chars): {between[:200]}...")
        else:
            print("No </main> found - checking body end...")
            print(f"Last 300 chars: ...{content[-300:]}")
            
    except Exception as e:
        print(f"Error: {e}")
