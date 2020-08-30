a,b=list(map(int,input().split()))
if a**b==int(str(b)+str(a)):
    print("they are automorphic")
else:
    print("not")
print(int(str(b)+str(a)))