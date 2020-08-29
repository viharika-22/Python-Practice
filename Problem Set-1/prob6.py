patient_1 = [[1,56.7], [2,34.6], [3, 34.2]]
patient_2 = [[1,76.8], [2,46.7], [3, 56.7]]
p1=[]
p2=[]
for i in range(len(patient_1)):
    for j in range(len(patient_1[i])):
        if not 34.5<patient_1[i][j]<67.7:
            p1.append(patient_1[i])
print(p1)
for i in range(len(patient_2)):
    for j in range(len(patient_2[i])):
        if not 34.5<patient_2[i][j]<67.7:
            p2.append(patient_2[i])
print(p2)
