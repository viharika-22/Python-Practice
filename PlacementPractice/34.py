patient_1 = [[1,56.7], [3,34.6], [3, 34.2]]
patient_2 = [[1,76.8], [2,46.7], [3, 56.7]]
p1=[]
p2=[]
for i in range(len(patient_1)):
    for j in range(len(patient_1[i])):
        p1.append(patient_1[i][1])
for i in range(len(patient_2)):
    for j in range(len(patient_2[i])):
        p2.append(patient_2[i][1])
p1=list(dict.fromkeys(p1))
p2=list(dict.fromkeys(p2))
print(p1)
print(p2)
