str1="abababaabgabgabggggababgab"
l=[]
acount=0
bcount=0
gcount=0
for i in range(len(str1)):
    l.append(str1[i])
for i in range(len(l)):
    if l[i]=='a':
        acount+=1
    elif l[i]=='b':
        bcount+=1
    elif l[i]=='g':
        gcount+=1
print(acount, bcount, gcount)
