n=int(input())
t=0
while(n>0):
    r=n%10
    t=t+r
    n=n//10
print(t)