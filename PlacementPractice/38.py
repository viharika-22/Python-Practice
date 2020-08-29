str1="agatfahatagagagayheirnrkuutthhtuuqoop"
d=dict()
l=[]
for i in range(len(str1)):
    d[str1[i]]=d.get(str1[i],0)+1
for i,j in d.items():
    l.append((j,i))
print(l)
