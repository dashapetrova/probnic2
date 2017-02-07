import re
def sub():
    s=''
    f = open("lerm.txt","r",encoding="utf-8")
    for line in f.readlines():
        line=re.sub('\.$','.@',line)
        #s2='(\.) [А-Я][а-я]+'
        #res=re.search(s2,line)
        #if res!=None:
            #line=re.sub('\\1','.@',line)
        s=s+line
    return s
sub()
def main():
    s=sub()
    a=s.split("@")
    return a
print(main())
