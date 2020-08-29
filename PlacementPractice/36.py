l1=[2,3,4,12,4,7,8,1]
l2=[2,4,1,7,5,9,2,5]
g=[]
l=[]
for i in range(len(l1)):
    if l1[i]>l2[i]:
        g.append(l1[i]-l2[i])
    elif l1[i]<l2[i]:
        l.append(l2[i]-l1[i])
print(l)
print(g)
