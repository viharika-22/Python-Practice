n=int(input())
spaces=2*n+2
print(" "*(spaces+1),end="*")
print("")
for i in range(1,n+1):
     for j in range(spaces):
          print(" ",end='')
     spaces-=1
     for j in range(i):
          print("*",end='')
     for j in range(i):
          print("*",end='')

     print("")
