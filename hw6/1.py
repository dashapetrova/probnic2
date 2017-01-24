import re
def text():
    f = open("1.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.lower().rstrip('.,<>/?""1234567890-=_+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def main():
    m=text()
    s='.+[аиюоыэеуё].+[июэоаыеуё].+[аиюоыэеуё].*'
    mas=[]
    for i in m:
        res=re.match(i,s)
        if res!='None':
            mas.append(i)
    return mas
print(main())
        
