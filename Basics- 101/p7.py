li1=[]
li=['how    ', 1 , '   are', 2.98, 'you?']
for i in range(0,len(li)):
    if i%2==0:
        li1.append(li[i])
str2=li1[0].strip()
str1=li1[1].strip()
str3=li1[2]
str4=str2+" "+str1+" "+str3
print(str4)
