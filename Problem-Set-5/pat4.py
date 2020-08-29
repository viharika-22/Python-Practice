for i in range(1,4):
    for j in range(4-i-1):
        print(end=' ')
    for k in range(1,i+1):
        if(k!=i-1):
            print(k,end=' ')
        else:
            print(i,end=" ")
    print()