import re
from datetime import datetime

news_path = r'd:\网站开发-json\pages\news.html'
with open(news_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找日期
dates1 = re.findall(r'<time[^>]*>([^<]+)</time>', content)
dates2 = re.findall(r'datetime="([^"]+)"', content)
titles = re.findall(r'<h3[^>]*>([^<]+)</h3>', content)

print('=== News.html Content Analysis ===')
print('Time elements: ' + str(len(dates1)))
print('Datetime attrs: ' + str(len(dates2)))
print('H3 titles: ' + str(len(titles)))

if dates2:
    print('Latest: ' + dates2[0])
if titles:
    print('\nFirst 5 titles:')
    for i, t in enumerate(titles[:5]):
        print(str(i+1) + '. ' + t)

# 搜索 2026-04 相关的日期
print('\n=== All April 2026 dates ===')
all_dates = re.findall(r'2026-April-[0-9]+', content)
print(all_dates)
