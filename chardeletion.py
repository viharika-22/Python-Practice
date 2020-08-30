s=input()
r=input()
s1=""
for i in range(len(s)):
    if s[i]==r:
        continue
    else:
        s1=s1+s[i]
print(s1)