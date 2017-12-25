import urllib.request
import re
import os
import json


def getdic():
    d={}
    site = 'file:///C:/Python33/thai_pages/'
    fs = os.listdir('thai_pages')
    for i in range(0,len(fs)):
        link = site+fs[i]
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        s="<tr><td class=th><a href='/id/.*?'>(.*?)</a></td><td>.*?<span class='.*?'>.*?</span>.*?<span class='.*?'>.*?</span>.*?<span class='.*?'>.*?</span>.*?<span class='.*?'>.*?</span></td><td class=.*?>.*?</td><td>(.*?)</td></tr>"
        rewords = re.compile(s, re.DOTALL)
        reTag = re.compile('<.*?>',re.DOTALL)
        words = rewords.findall(html)
        for i in range(0,len(words)):
            d[words[i][0]]=words[i][1]
    print(d)
getdic()
