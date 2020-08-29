n=int(input())
num=n
p=len(str(n))
t=0
while(n>0):
    r=n%10
    t+=r**p
    n=n//10
if(t==num):
    print("it is amstrong num")
else:
    print("not amstrong num")