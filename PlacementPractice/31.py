li= [[[1,2,3,4],4,5,6,[2,3]],[[1,2,3],5,6], [[2,3],[4,5],[6,7]], 7,8]
l=[]
l1=[]
for i in range(len(li)):
    if type(li[i])==int:
        l.append(li[i])
    else:
        l1.append(li[i])
for i in range(len(l1)):
    for j in l1[i]:
        if type(l1[i][j])==int:
            l.append(l1[i][j])
print(l)
