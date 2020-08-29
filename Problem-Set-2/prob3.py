'''Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters. '''
n=input()
count=0
for i in range(len(n[:4])):
    if 65<=ord(n[i])<=90:
        count+=1
if count==2:
    print(n.upper())
