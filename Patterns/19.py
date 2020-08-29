n=1
l=0
li=list()
for i in range(5):
    for j in range(i):
        if(j==0):
            li.append(n)
        print(n,end='')
        if(j!=i-1):
            print("*",end='')
        n+=1
    print()
for i in range(5):
    for j in range(5-i-1):
        for k in range(len(li)):
           l=li[k]
           k+=1
        print(l,end=' ')
        l+=1
        
    print()

