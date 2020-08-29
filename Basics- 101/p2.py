li=[]
li2=[]
str1="Gecko"
str2="Gemma"
for i in str1:
    li.append(i)
for j in str2:
    li2.append(j)
for i in li:
    for j in li2:
        if(i==j):
            print(str1.index(i))
