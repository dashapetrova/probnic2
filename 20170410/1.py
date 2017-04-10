#путь-предложение
import os
import shutil
s=input('input a sentence: ')
a=s.split()
k=a[1]
for i in a:
    if not os.path.exists(i):
        os.mkdir(i)
        shutil.move(i,k)
        k=i
    else: break
#path=''
#path=[path+'/'+'{}'.format(a[i]) for i in range(len(a))]
#os.makedirs(path)

