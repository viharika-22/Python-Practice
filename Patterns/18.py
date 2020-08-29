n=int(input())
for i in range(n+1):
    for j in range(i):
        print(i,end='')
        if(j!=i-1):
            print("*",end='')
    print()
for i in range(n+1):
    for j in range(n-i):
        print(n-i,end='')
        if(j!=n-i-1):
            print("*",end='')
    print()