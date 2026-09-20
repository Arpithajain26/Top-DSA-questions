"""Perfect Number — Coding Question

Question:
Given a positive integer n, write a Python program to check whether it is a Perfect Number or not.

A number is called a Perfect Number if the sum of its proper positive divisors (excluding the number itself) is equal to the number.

Example:

For n = 28
Proper divisors: 1, 2, 4, 7, 14
Sum = 1 + 2 + 4 + 7 + 14 = 28

Therefore, 28 is a Perfect Number.

Input:

28

Output:

Perfect Number

Another example:

Input: 12
Output: Not a Perfect Number

Your task: Write the function:"""
def perfect_number(n):
    sum_n=1
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum_n+=i
            if i!=n//i:
                sum_n+=n//i
    return sum_n==n
print(perfect_number(28))
print(perfect_number(12))
def perfect_number(n):
    sum_n=1
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum_n+=i
            if i!=n//i:
                sum_n+=n//i
    return sum_n==n
print(perfect_number(28))
    