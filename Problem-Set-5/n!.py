n=int(input())
s=1
if(n==1):
    print("{}factorial is 0".format(n))
else:
    for i in range(1,n+1):
        s=s*i 
print(s)

