import urllib.request

req = urllib.request.Request('https://habrahabr.ru/')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8') #скачали страничку в html

print(html)
