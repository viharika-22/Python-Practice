# 153 is amstrong if 1^3+5^3+3^3=153
n=int(input())
number=n
num=0
p=len(str(n))
while n>0:
    r=n%10
    num=num+r**p
    n=n//10
if(number==num):
    print("yes ")
else:
    print("no")