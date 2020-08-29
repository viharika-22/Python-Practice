s=input()
l=[]
s1=str()
for i in range(len(s)):
    if 65<=ord(s[i])<=90:
        s1=chr(ord(s[i])+32)
        l.append(s1)
print("".join(l))