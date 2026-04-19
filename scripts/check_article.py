# -*- coding: utf-8 -*-
content = open('d:/网站开发-json/index.html', encoding='utf-8').read()
idx = content.find('2026-04-15')
print('04-15 found at:', idx)
if idx > 0:
    # Show surrounding context
    ctx = content[idx-100:idx+500]
    print("Context around 04-15:")
    print(ctx[:300])
