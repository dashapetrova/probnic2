#вывод названий китайских кораблей
import re
def text():
    f = open("31.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.rstrip('.,<>/?""=_-+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def main():
    m = text()
    regex = '«([а-яА-Я]+ ?)+-[0-9]»'
    s = ''
    prev=m[0]
    for i in m:
        j=prev+'-'+i
        res = re.search(regex,j)
        if res != None:
            if j not in s:
                s = s + i + ', '
        prev=i
    return s
print(main())
#массив в строку попробовать переделать и по(в) ней искать
    
