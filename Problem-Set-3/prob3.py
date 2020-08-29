''') a string is given agatfahatagagagayheirnrkuutthhtuuqoop
Find the count of each letter in the above string, and according to number of count
arrange them in descending order and then using this order form a random word.'''
s="agatfahatagagagayheirnrkuutthhtuuqoop"
d={}
c=0
for i in range(len(s)):
    d[s[i]]=d.get(i,0)+1
print({}.format(s,s(i)))
