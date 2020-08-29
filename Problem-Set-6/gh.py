lst=[]
lst2=[]
x=input(int())
for i in x:
    lst.append(i)
for i in lst:
    if int(i) not in lst2:
        lst2.append(int(i))
print(lst2)
