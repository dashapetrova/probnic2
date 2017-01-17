d = {1: 'a',2: 'b'}

d['aa']='d'
abc=d[2]
#de=d[3] нет такого ключа error

if 3 in d:
    de=d[3]

if d[3]==4:
    de=d[3]

d[1] += 'qwe'

d[3] = []
d[3].append('abc')

d[4]=0
d[4]+=1

a = [1,2,3]
a[0] = 4

for k in d:
    print(d[k])

for k in sorted(d):
    print(k)
    
#так низя
for k in d:
    d[2]=3

a=[1,2,3,4]
for x in a:
    dic[3]=1
    
a = ['1','2','3']
a[0] = 4
#a[12] = 4 нет такого индекса error

#задача про частотность
words=['abc','def','ghi','abc']
word_count={}
for word in words:
    if word not in word_count:
        word_count[word]=1
    else:
        word_count[word]+=1
for word in sorted(word_count):# по алфавиту
    print(word, word_count[word])

#получить список всех ключей
key_list = list(word_count.keys())
#получить список всех значений
val_list = list(word_count.values())
#удалить значение
del(word_count[word])

d={'a1': 1,'a2': 3,'a3': {2:'123'}}
d['a3'][2]

a=[1,2,3]
b=a #фокус
print(b)
#[1,2,3]
b.append(4)
print(b)
#[1,2,3,4]
print(a)
#[1,2,3,4]
b=a[:] # тогда копия, а не ссылка
d1=d.copy() # то же самое

