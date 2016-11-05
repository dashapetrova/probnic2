#2-ой вариант
s=input("введите слово: ")
i=0
for letter in s:
    if (i+1)%2!=0 :
        if s[i]=='о' or s[i]=='п' or s[i]=='е':
            print(s[i])
    i=i+1
print('\nЧтобы завершить программу, нажмите Enter')
ENTER=input('')
