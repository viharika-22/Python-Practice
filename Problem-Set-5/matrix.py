rows=int(input())
cols=int(input())
matrix1=[[int(input())for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j],end=' ')
    print()
matrix2=[[int(input())for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(matrix2[i][j],end=' ')
    print()
res=[[0 for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        res[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(rows):
    for j in range(cols):
        print(res[i][j],end=' ') 
    print()
