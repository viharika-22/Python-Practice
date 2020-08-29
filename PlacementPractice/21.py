n=input()
l=n.split()
l1=[]
for i in range(len(l)):
    if 65<=ord(l[i][0])<=90:
        l1.append(l[i])
print(l1)
