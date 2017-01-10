#получает номер, выводит слова с таким кол-вом слогов
def text():
    f=open("1.txt","r",encoding="utf-8")
    a=f.read().split()
    m=[]
    for n in a:
        b=n.lower().rstrip('.,<>/?""1234567890-=_+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def f2(n,m):
    s='ёуеэоаыяию'
    mas=[]
    for i in m:
        k=0
        for j in i:
            if j in s:
                k+=1
        if k==n:
            mas.append(i)
    return mas                
def main():
    n=int(input("input number: "))
    m=text()
    a=f2(n,m)
    return a
print(main())
