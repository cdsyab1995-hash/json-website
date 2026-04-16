import os

# New nav items to add after "CSV" (json2csv.html) in the dropdown menu
CSV_LINK_REPLACEMENT = '''<a href="json2csv.html" class="nav-link">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="8" y1="13" x2="16" y2="13"></line>
                        <line x1="8" y1="17" x2="16" y2="17"></line>
                    </svg>
                    CSV
                </a>
                <a href="csv-to-excel.html" class="nav-link">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="3" y1="9" x2="21" y2="9"></line>
                        <line x1="9" y1="21" x2="9" y2="9"></line>
                    </svg>
                    Excel
                </a>
                <a href="excel-remove-duplicates.html" class="nav-link">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                    </svg>
                    Remove Duplicates
                </a>'''

# Update pages/*.html files
pages_dir = r'd:\网站开发-json\pages'
count = 0

for f in os.listdir(pages_dir):
    if not f.endswith('.html') or f in ['csv-to-excel.html', 'excel-remove-duplicates.html']:
        continue
    
    fp = os.path.join(pages_dir, f)
    with open(fp, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Only update if this is a tool page with the nav dropdown
    if 'json2csv.html' not in content:
        continue
    
    # Pattern for the CSV link in nav dropdown
    old_pattern = '''<a href="json2csv.html" class="nav-link">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="8" y1="13" x2="16" y2="13"></line>
                        <line x1="8" y1="17" x2="16" y2="17"></line>
                    </svg>
                    CSV
                </a>'''
    
    if old_pattern in content:
        new_content = content.replace(old_pattern, CSV_LINK_REPLACEMENT)
        with open(fp, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f'Updated: {f}')

print(f'\nTotal pages updated: {count}')

# Update index.html separately (different structure)
index_path = r'd:\网站开发-json\index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add new tool cards after CSV card in index.html
    CSV_CARD_PATTERN = '''<a href="pages/json2csv.html" class="feature-card">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                    <line x1="8" y1="13" x2="16" y2="13"></line>
                    <line x1="8" y1="17" x2="16" y2="17"></line>
                </svg>
            </div>
            <h3>JSON to CSV</h3>
            <p>Convert JSON to CSV format for Excel and Google Sheets import. Perfect for data analysis workflows.</p>
        </a>'''
    
    CSV_CARD_REPLACEMENT = CSV_CARD_PATTERN + '''
            <a href="pages/csv-to-excel.html" class="feature-card">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="3" y1="9" x2="21" y2="9"></line>
                    <line x1="9" y1="21" x2="9" y2="9"></line>
                </svg>
            </div>
            <h3>CSV to Excel</h3>
            <p>Convert CSV to Excel XLSX format. Import spreadsheet data with proper formatting.</p>
        </a>
            <a href="pages/excel-remove-duplicates.html" class="feature-card">
            <div class="feature-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
            </div>
            <h3>Remove Duplicates</h3>
            <p>Remove duplicate rows from CSV or spreadsheet data. Clean your data with one click.</p>
        </a>'''
    
    if CSV_CARD_PATTERN in content:
        new_content = content.replace(CSV_CARD_PATTERN, CSV_CARD_REPLACEMENT)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: index.html')
    else:
        print(f'index.html: pattern not found')

print('\nDone!')
