l=[[14.5,4], [67.8,98.9], [1,2,3], [78.9,67.8]]
il=[]
fl=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        if type(l[i][j])==float:
            fl.append(l[i][j])
        else:
            il.append(l[i][j])
print(sum(fl)-sum(il))
