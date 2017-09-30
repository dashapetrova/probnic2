#скачивает статью в файл и чистит её

import urllib.request
import re

def Download_page(page):
    i=0
    req = urllib.request.Request(page)
    with urllib.request.urlopen(req) as response:
       html = response.read().decode('utf-8')

    regPostTitle = re.compile('<p>.*?</p>', flags= re.DOTALL)
    titles = regPostTitle.findall(html)

    new_titles = []
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    for t in titles:
        clean_t = regSpace.sub("", t)
        clean_t = regTag.sub("", clean_t)
        new_titles.append(clean_t)
        
    name=str(i)+'.txt'
    f = open(name, 'w', encoding = "utf-8")
    i+=1
    for i in range(len(new_titles)):
        f.write(new_titles[i]+'\n')
    f.close()
page='http://pav-edin23.ru/2017/09/30/sdelaem-krasivee-rodinu/'
Download_page(page)

