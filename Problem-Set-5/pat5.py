n=1
for i in range(1,4):
    for j in range(4-i-1):
        print(end=' ')
    for k in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()