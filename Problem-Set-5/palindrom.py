n=input()
l1=list(n)
l2=list(n[::-1])
if (l1==l2):
    print("it is palindrome")
else:
    print("it is not a palindrome")