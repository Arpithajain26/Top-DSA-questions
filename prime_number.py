# write a program to check if a number is prime number not
def check_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0
# check_prime(10)
# check_prime(3)

# to generate prime numbers from 1 to n
def prime_numbers(a,b):
    list1=[]
    for i in range(a,b+1):
        if check_prime(i):
            list1.append(i)
    return list1
print(prime_numbers(1,100))
