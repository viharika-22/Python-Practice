n=int(input())
l=1
for i in range(1,n+1):
    for j in range(i):
        print(l,end='')
        l+=1
        if(j!=i-1):
            print("*",end='')
    print()
