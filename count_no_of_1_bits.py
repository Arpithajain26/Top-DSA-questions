"""Question: Count Number of 1 Bits

Given an integer n, write a function to count the number of 1 bits in its binary representation.

Example 1:

Input: n = 11
Binary: 1011
Output: 3

Example 2:

Input: n = 128
Binary: 10000000
Output: 1

Expected approach: Convert the number to binary or use bit manipulation and count how many 1s are present."""
def count_number_of_bits(num):
    x=bin(num)[2:]
    count=0
    for i in str(x):
        if i=='1':
            count+=1
    return count
print(count_number_of_bits(128))
"""another optimised solution"""
def count_bits(n):
    count=0
    while n:
        n=n&(n-1)
        count+=1
    return count
print(count_bits(3))