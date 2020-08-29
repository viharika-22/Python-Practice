names=[]
num=int(input("enter the number of names:"))
for i in range(0,num):
    names.append(str(input("enter the name:")))
print(names)
sortednames=[]
for i in names:
    if i[0]=='a'or i[0]=='i' or i[0]=='e' or i[0]=='o' or i[0]=='u':
        sortednames.append(i)
    else:
        continue

print(sortednames)
