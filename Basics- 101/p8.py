str1= "arjun"
n=len(str1)
li=[]
li1=[]
for i in range(0,n):
    for j in range(i,n):
        li.append(str1[i:(j+1)])
print("substrings are:")
for i in li:
    print(i)
    if len(i)==1:
        continue
    li1.append(i)
print(len(li1))
