# write a program to check if a number is prime number not
def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime number")
check_prime(10)
check_prime(3)