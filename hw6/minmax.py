f=open("new1.txt","r",encoding = "utf-8")
mx=mn=len(f.readline())
for line in f:
    if line != "\n":
        if len(line) > mx:
            mx = len(line)
        if len(line) < mn:
            mn=len(line)
print(mx/mn)
f.close()
