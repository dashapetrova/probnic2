import os
d = {}
lst = os.listdir('thai_pages')
for fl in lst:
    with open('thai_pages/'+fl, 'r', encoding='utf-8') as f:
        html = f.read()
print(html)
