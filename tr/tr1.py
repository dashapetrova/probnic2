import random
def words():
    f = open("tr.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.lower().strip('.,<>/?"123456789—0-=_+''[]{}()*&^%$#@!;:|\...')
        if b!='':
            m.append(b)
    f.close()
    return m

def numb():
    m = words()
    n = 0
    for i in m:
        n += 1
    return n

def dic():
    m = words()
    d = {}
    k = 0
    for i in m:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
            k += 1
    return d

def record():
    d = dic()
    m = []
    for i in d.keys():
        m.append(i)
    m.sort()
    f = open('ress.csv','w',encoding='utf-8')
    for i in m:
        f.write(i+','+str(d[i])+'\n')   
    f.close()
record()
