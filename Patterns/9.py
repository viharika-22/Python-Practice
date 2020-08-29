n=int(input())
row=0
col=n-1
for i in range(n):
    for j in range(n):
        if(i==row and j==col):
            print("1",end='')
            row+=1
            col-=1
        elif(i==j):
            print("2",end='')
        else:
            print('3',end='')
    print()