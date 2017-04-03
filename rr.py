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
    for i in m:
        if i != '':
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
    return d
def main():
    d=fff()
    k=[]
    for i in d.keys():
        k.append(i)
    k.sort()
    f = open("results.txt",'w',encoding='utf-8')
    for i in k:
        f.write(i+' - '+str(d[i])+'\n')
    f.close()
main()
