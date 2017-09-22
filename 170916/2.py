import urllib.request
import time

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl) #скачиваем страницу по ссылке
        print(page.geturl()) #итоговый url после переадресации
        text = page.read().decode('ISO-8859-1') # читаем
        return text
    except:
        print('Error at', pageUrl)
        return
    
commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(2301, 2302): #50-16556
    pageUrl = commonUrl + str(i) #проходит по страницам
    text = download_page(pageUrl) #идем в def
    try:
        for i in range(2,4):
            page = urllib.request.urlopen(pageUrl)
            print(page.geturl())
            text = page.read().decode('ISO-8859-1')
            newpage = text + '/page'+ str(i)
            print(newpage)

    except:
        print('Error')
        

