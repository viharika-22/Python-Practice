n=int(input())
for i in range(n):
    for j in range(n-i):
        print(end=' ')
    for k in range(0,i):
        print("* ",end="")
    print()