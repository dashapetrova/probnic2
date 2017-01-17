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
    mc={}
    s=''
    for i in m:
        if i not in mc:
            mc[i]=1
        else:
            mc[i]+=1
    for i in sorted(mc):
        if mc[i]>10:
            s=s+i+' '
    return s
print(main())
