n=int(input())
a=0
b=1
c=0
print(a,end=' ')
print(b,end=' ')
for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c