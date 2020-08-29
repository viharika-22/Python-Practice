s=list(input())
l=[]
for i in range(len(s)):
    if s[i]=="i" or s[i]=="o" or s[i]=="a" or s[i]=="e" or s[i]=="u":
        l.append(s[i])
    else:
        continue
print("".join(l))