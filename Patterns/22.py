n=int(input())
a=0
b=1
for i in range(2,n+1):
    for j in range(i):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
    print()