n=str(input())
li=[]
for i in n:
    li.append(i)
if li[::]==li[::-1]:
    print("yes it is palindrome ")
else:
    print("it isn't palindrome")
