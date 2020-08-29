s=input()
n=int(input())
li=[]
for i in range(n):
    l=s[i:]+s[:i]
    li.append(l)
for i in range(n):
    r=s[-i:]+s[:-i]
    li.append(r)
print(li)