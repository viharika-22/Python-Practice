l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in range(len(l1)):
    s=l1[i]-l2[i]
    l.append(s)
print(l)