li= ["Navya", [3,4,1,3], "Uma", [1,1,2,1], "Kiran", [1,3,5,1], "Mahesh", [3,2,4,5]]
li1=[]
li2=[]
for i in li[0:8:2]:
    li1.append(i)
print(li1)
p=li1.copy()
for i in li[0:8:2]:
    li1.remove(i)
for i in li[1:8:2]:
    li2.append(i)
print(li2)
l=[max(i) for i in li2]
print(l)
list3 = []
while True:
    try:
        list3.append(p.pop(0))
        list3.append(l.pop(0))
    except IndexError:
        break
print(list3)
