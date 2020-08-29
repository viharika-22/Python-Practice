di= {'sid': 97, 'yamima' : 97.5, 'ramesh':86.9, 'Arjun': 78.9}
count=0
sum1=0
for key in di:
    count += 1
    sum1 += di[key]

print('this is the mean: ', sum1/count)
