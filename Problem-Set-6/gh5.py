import re
handle=open('hushh.txt')
ls=[]
for line in handle:
    line=line.rstrip()
    x=re.findall('@(.+\s)',line)
    ls.append(x)
print("my passwords are:",ls)
