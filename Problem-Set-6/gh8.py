di = dict()
li = input().split()
for i in range(len(li)):
       di[li[i]]= int(input())
for v in di.keys():
    if (v>75):
        print(v)
