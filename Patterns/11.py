n=int(input())
for i in range(n,0,-1):
    for j in range(n,i,-1):
         print(end=' ')
    for k in range(i):
        if (i==1):
            print("x",end='')
        else:
            print("* ",end='')
        
    print()
for i in range(1,n):
    for j in range(n-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print("* ",end='')
    print()
