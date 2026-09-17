def harshard_number(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    return num%sum==0
print(harshard_number(19))
# number is said to be harshad number if it num is divisible by sum of digits