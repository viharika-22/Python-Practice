nums=list(map(int,input().split()))
nums.sort()
n=len(nums)//2
l=[]
l=nums[:n]+nums[:n-1:-1]
print(l)