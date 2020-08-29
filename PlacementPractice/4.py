l=["alisha","siona","amrutha","uma","mouni","siri"]
li=[]
for i in range(len(l)):
    if l[i][0]=='a'or l[i][0]=='i'or l[i][0]=='e' or l[i][0]=='o' or l[i][0]=='u':
        li.append(l[i])
print(li)
