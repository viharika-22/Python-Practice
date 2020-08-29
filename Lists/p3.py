li=[]
li=str(input())
caps=0
low=0
for i in range(len(li)):
    if 65<=ord(str(li[i]))<=90:
        caps+=1
    else:
        low+=1
print("capitals= ",caps," lowercase=",low)
w=low-caps
print(w)
