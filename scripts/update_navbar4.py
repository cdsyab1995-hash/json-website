import os

# Update index.html - add new feature cards after Compare card
index_path = r'd:\网站开发-json\index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Compare card and add new cards after it
    old_compare = '<a href="pages/compare.html" class="feature-card"> <div class="feature-icon"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M16 3h5v5"></path> <path d="M8 3H3v5"></path> <path d="M21 3l-7 7"></path> <path d="M3 3l7 7"></path> <path d="M16 21h5v-5"></path> <path d="M8 21H3v-5"></path> <path d="M21 21l-7-7"></path> <path d="M3 21l7-7"></path> </svg> </div> <h3>JSON Compare</h3> <p> Compare two JSON documents and highlight differences. Detect additions, deletions, and modifications instantly. </p> </a> <!-- Tutorial Card -->'
    
    new_compare = '<a href="pages/compare.html" class="feature-card"> <div class="feature-icon"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M16 3h5v5"></path> <path d="M8 3H3v5"></path> <path d="M21 3l-7 7"></path> <path d="M3 3l7 7"></path> <path d="M16 21h5v-5"></path> <path d="M8 21H3v-5"></path> <path d="M21 21l-7-7"></path> <path d="M3 21l7-7"></path> </svg> </div> <h3>JSON Compare</h3> <p> Compare two JSON documents and highlight differences. Detect additions, deletions, and modifications instantly. </p> </a> <!-- CSV to Excel Card --> <a href="pages/csv-to-excel.html" class="feature-card"> <div class="feature-icon"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect> <line x1="3" y1="9" x2="21" y2="9"></line> <line x1="9" y1="21" x2="9" y2="9"></line> </svg> </div> <h3>CSV to Excel</h3> <p>Convert CSV to Excel XLSX format. Import spreadsheet data with proper formatting.</p> </a> <!-- Remove Duplicates Card --> <a href="pages/excel-remove-duplicates.html" class="feature-card"> <div class="feature-icon"> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"> <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path> <polyline points="22 4 12 14.01 9 11.01"></polyline> </svg> </div> <h3>Remove Duplicates</h3> <p>Remove duplicate rows from CSV or spreadsheet data. Clean your data with one click.</p> </a> <!-- Tutorial Card -->'
    
    if old_compare in content:
        new_content = content.replace(old_compare, new_compare)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: index.html')
    else:
        print(f'index.html: Compare card pattern not found')

print('\nDone!')
