n=int(input())
d={}
l=[]
li=[]
for i in range(n):
    key=input()
    d[key]=float(input())
for i in d.keys():
    l.append([i,d[i]])
for i in range(len(l)):
    li.append(l[i][1])
print(li)
