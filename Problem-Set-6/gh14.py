 li= [[1,2,3,5], [2,3,4,5],[2,2,3,4], [1,2,4,2]]
 l=[]
 for i in range(len(li)):
     for j in range(len(li[i])):
             l.append(j)
print(sum(l))
