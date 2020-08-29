'''Write a Python program to find the first non-repeating character in given string'''
n=input()
l=n.split()
r=[]
p=[]
c=0
for i in n:
    word=i
    for j in n:
        if word==j:
            c+=1
        p.append([word,c])
    c=0
print(p)
