"""Hamming Distance — Question

Problem:
Given two integers x and y, find the Hamming Distance between them.

The Hamming distance is the number of positions at which the corresponding bits in the binary representations of x and y are different.

Example 1:

Input:  x = 1, y = 4
Output: 2

Explanation:

1 = 001
4 = 100
     ↑ ↑
Different bits = 2

Example 2:

Input:  x = 3, y = 1
Output: 1"""
def hamming_distance(x,y):
    c=x^y
    count=0
    for i in bin(c)[2:]:
        if i=='1':
            count+=1
    return count
print(hamming_distance(1,4))