n=int(input(

))
li=[]
li.append(n)
su=0
for i in range(len(li)):
    su=su+li[i]
print("avg age of the family",su/len(li))
