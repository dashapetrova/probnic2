import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        print(page.geturl()) #итоговый url после переадресации
        text = page.read().decode('ISO-8859-1')
    except:
        print('Error at', pageUrl)
        return
    # do something with the downloaded text

commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(160400, 160425):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)

html_content = '<html>....</html>'  # тут какой-то html

regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)  # это рег. выражение находит все тэги
regScript = re.compile('<script>.*?</script>', flags=re.U | re.DOTALL) # все скрипты
regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)  # все комментарии

# а дальше заменяем ненужные куски на пустую строку
clean_t = regScript.sub("", t)
clean_t = regComment.sub("", clean_t)
clean_t = regTag.sub("", clean_t)
