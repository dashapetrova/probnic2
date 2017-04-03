#ключ словоформа, значение позиция
def words():
    f = open("rr.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.strip('.,<>/?""1234567890-=_+''""[]{}()*&^%$#@!;:|\...').lower()
        m.append(b)
    return m
def fff():
    m=words()
    d={}
    j=0
    for i in m:
        if i != '':
            d[i]=j
            j+=1
    return d
def main():
    d=fff()
    k=[]
    for i in d.keys():
        k.append(i)
    k.sort()
    f = open("results.txt",'w',encoding='utf-8')
    for i in k:
        f.write('{} - {}\n'.format(i,d[i]))
    f.close()
main()
