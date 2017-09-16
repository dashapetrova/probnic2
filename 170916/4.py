import urllib.request
import time

#m=[]
def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl) #скачиваем страницу по ссылке
        time.sleep(1)
        print(page.geturl()) #итоговый url после переадресации
        text = page.read().decode('ISO-8859-1') # читаем
        #a=1
        #m.append(a)
        #print(len(m))
    except:
        print('Error at', pageUrl)
        return
    
commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(50, 55): #50-16556
    pageUrl = commonUrl + str(i) #проходит по страницам
    download_page(pageUrl) #идем в def
    

