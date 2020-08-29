li=[{'eng':75},{'math':89},{'sst':76},{'sci':90}]
li1=[]
for i in range (len(li)):
    d=li[i]
    for j in d.values():
        li1.append(j)
total=sum(li1)
print("total marks are:",total)
per=total/400
percentage=per*100
print("the percentage is:",percentage)
