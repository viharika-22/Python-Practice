n=input()
caps=0
lows=0
for i in range(len(n)):
    if 65<=ord(n[i])<=90:
        caps+=1
    else:
        lows+=1
print(caps-lows)
