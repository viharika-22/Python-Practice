n1=int(input())
n2=int(input())
for i in range(n2):
    for j in range(i):
        print(n1-1,end=' ')
    n1+=1
    print()
for i in range(n2,0,-1):
    for j in range(i):
        print(n1-1,end=' ')
    n1-=1
    print()