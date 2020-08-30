def palindromecheck(n):
    n=str(n)
    if n==n[::-1]:
        print("it s a palindrome")
    else:
        print("not a palindrome")
palindromecheck(input())