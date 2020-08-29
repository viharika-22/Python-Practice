l=[1,3,4,5,6,7,4,6,7,8,1,4,3,1]
li=[]
for i in range(len(l)):
    if l[i] not in li:
        li.append(l[i])
print(li)
