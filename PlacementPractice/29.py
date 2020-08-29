li= ["Navya", [3,4,1,3], "Uma", [1,1,2,1], "Kiran", [1,3,5,1], "Mahesh", [3,2,4,5]]
l=[]
l1=[]
n=[]
for i in range(len(li)):
    if i%2!=0:
        l.append(li[i])
l2=[max(i) for i in l]
for i in range(len(li)):
    if i%2==0:
        n.append(li[i])
for i in zip(n,l2):
    print(i)
