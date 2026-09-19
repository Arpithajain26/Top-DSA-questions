"""Armstrong Number – Coding Question

Question:
Write a Python program to check whether a given number is an Armstrong number or not.

Example:

Input: 153
Output: Armstrong Number

Explanation:
For 153:
1³ + 5³ + 3³ = 1 + 125 + 27 = 153

So, 153 is an Armstrong number.

Another example:

Input: 123
Output: Not an Armstrong Number"""
def check_armstrong_number(n):
    sum=0
    digits=str(n)
    for i in digits:
        sum+=int(i)**len(str(n))
    if sum==n:
        return True
    return False


        
print(check_armstrong_number(153))
print(check_armstrong_number(123))
def check_anargam1(n):
    digit=str(n)
    sum=0
    for i in digit:
        sum+=int(i)**len(digit)
    return sum==n
print(check_anargam1(153))
        