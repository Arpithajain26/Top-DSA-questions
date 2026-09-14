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
    for i in str(n):
        sum+=int(i)**3
    if sum==n:
        return True
    return False


        
print(check_armstrong_number(153))
print(check_armstrong_number(123))