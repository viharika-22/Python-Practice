li= [{"english":75},{"math":89}, {"sst": 76}, {"science":90}]
l=[]
for i in range(len(li)):
    for j in li[i].values():
        l.append(j)
total=len(l)*100
per=sum(l)/total*100
print(per)
