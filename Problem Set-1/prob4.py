li=[[14.5,4], [67.8,98.9], [1,2,3], [78.9,67.8]]
l=[]
for i in range(len(li)):
    for j in range(len(li[i])):
        l.append(li[i][j])
f=[]
t=[]
for i in l:
    if type(i)==float:
        f.append(i)
    else:
        t.append(i)
s=f+t
print(type(s))       
