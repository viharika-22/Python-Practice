li= [1,6,7,5,4,3,7,5]
d={}
l=[]
for i in range(len(li)):
    d[li[i]]=d.get(li[i],0)+1
for i,j in d.items():
    l.append((i,j))
print(l)
