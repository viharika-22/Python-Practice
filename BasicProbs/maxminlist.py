li=list(map(int,input().split()))
max=0
min=li[0]
for i in range(len(li)):
    if(li[i]>max):
        max=li[i]
    elif(li[i]<min):
        min=li[i]
print(max,min)
