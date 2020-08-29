n=list(map(int,input().split()))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(n[i]>n[j]):
            t=n[i]
            n[i]=n[j]
            n[j]=t
print("minimum number",n[0])
print("secund minimum number",n[1])
print("maxmum number",n[len(n)-1])
print("secund maxmum number",n[len(n)-2])