s=list(input())
s1=list()
l=[]
for i in range(len(s)):
    o=ord(s[i])
    l.append(o)
l.sort()
for i in range(len(l)):
    c=chr(l[i])
    s1.append(c)
print("".join(s1))

