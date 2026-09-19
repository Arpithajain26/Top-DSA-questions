"""ower of 2 – Coding Question

Question:

Write a Python program to check whether a given positive integer is a power of 2 or not.

A number is a power of 2 if it can be expressed as:

2⁰, 2¹, 2², 2³, ...

Examples:

Input: 16
Output: Power of 2

Explanation:
16 = 2⁴
Input: 18
Output: Not a Power of 2"""
def check_power_of_2(num):
    x=1
    for i in range(num):
        x=2**i
        if x==num:
            return "true"
    return "false"
print(check_power_of_2(4))
print(check_power_of_2(7))

# another method
def check_power_of_2(num):
    if num>0 and (num & (num-1)==0):
        return "true"
    return "false"
print(check_power_of_2(2))
def check_power_of(num):
    if num>0 and (num&(num-1)==0):
        return True
    else:
        return False
print(check_power_of(4))
        