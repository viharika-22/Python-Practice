n=int(input())
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(end=' ')
    for k in range(0,i):
        print("* ",end='')
    print()