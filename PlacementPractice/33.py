n=input()
l=[]
for i in range(len(n)):
    l.append(n[i])
if l[::]==l[::-1]:
    print("it is palindrome")
else:
    print("not a palindrome")
