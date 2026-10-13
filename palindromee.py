def palindrome(n):
    res=0
    temp=n
    while temp!=0:
        rem=temp%10
        res=(res*10)+rem
        temp//=10
    return res==n
print(palindrome(121))