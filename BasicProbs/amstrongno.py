n=int(input())
p=len(str(n))
num=n
t=0
while n>0:
    r=n%10
    t=t+r**p
    n=n//10
if(num==t):
    print("yes")
else:
    print("NO")