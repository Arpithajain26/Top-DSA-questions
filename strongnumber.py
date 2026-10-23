n=int(input("enter the value of n: "))
copy=n
sum=0
while n!=0:
    r=n%10
    n//=10
    fact=1
    for i in range(1,r+1):
        fact*=i
    sum+=fact
if sum==copy:
    print("strong number")
else:
    print("not strong number")
    