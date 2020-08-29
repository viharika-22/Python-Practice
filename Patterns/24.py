n=int(input())
for i in range(n+1):
    for j in range(i):
        print("*",end='')
    print()
    for k in range(n-i):
        print(i+1,end='')
    print()
