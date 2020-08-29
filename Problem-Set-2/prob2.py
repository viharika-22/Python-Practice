''')Write a Python program to change a given string to a new string
  where the first and last chars have been exchanged.'''
n=input()
d=n[0]
r=n[len(n)-1]
s=n[1:len(n)-1]
print(r+s+d)
