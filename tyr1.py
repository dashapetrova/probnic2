def f1():
    text=open("text.txt")
    s=text.read().lower().split(" ")
    text.close()
    return s
s=f1()
print(s)
i=0
for word in s:
    i+=1
print("количество слов = ",i)
        
    
