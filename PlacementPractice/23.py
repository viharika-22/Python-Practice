n=int(input())
l=[]
for i in range(n):
    print("enter the float vaule:")
    l.append(float(input()))
l.sort()
print(" secound Highest value is",l[-2])
