for i in range(1,100):
    i=str(i)
    if i==[1,2,3,4,5,6,7,8,9]:
        i=int('0'+i)
    if i==i[::-1]:
        print(i,end=" ")