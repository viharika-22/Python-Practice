s=input()
l1=[]
l2=[]
for i in range(len(s)):
    if(ord(s[i])==45):
        l1.append(s[i])
    else:
        l2.append(s[i])
l=l1+l2
print("".join(l))