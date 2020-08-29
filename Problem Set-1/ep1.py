s="abababaabgabgabggggababgab"
l=[]
for i in s:
    l.append(i)
print(l)
g_count=0
a_count=0
b_count=0
for i in range(len(l)):
    if l[i]=='a':
        a_count+=1
    elif l[i]=='b':
        b_count+=1
    elif l[i]=='g':
        g_count+=1
print("red pixels are",a_count,"blue pixels are",b_count,"green pixels are ",g_count)
