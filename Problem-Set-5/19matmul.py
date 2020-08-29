rows=int(input())
cols=int(input())
mat1=[[int(input())for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(mat1[i][j],end=' ')
    print()
mat2=[[int(input())for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(mat2[i][j],end=' ')
    print()
result=[[0 for i in range(cols)]for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        if i==j or i+j==rows-1:
            
for i in range(rows):
    for j in range(cols):
        print(result[i][j],end=' ')
    print()