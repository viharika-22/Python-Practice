s="viharika"
n=int(input())
l=[]
for i in range(1,n+1):
    r=s[i:]+s[:i]
    l.append(r)
for i in range(1,n+1):
    le=s[-i:]+s[:-i]
    l.append(le)
print(l)


