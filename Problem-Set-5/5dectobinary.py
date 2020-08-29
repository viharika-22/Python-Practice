def db(n):
    if n>1:
        db(n//2)
    print(n%2,end='')
db(int(input()))