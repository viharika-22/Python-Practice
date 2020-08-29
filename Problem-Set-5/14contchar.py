s=input()
d=dict()
l=[]
for i in range(len(s)):
    d[s[i]]=d.get(s[i],0)+1
for k,v in d.items():
    l.append((v,k))
print(l)