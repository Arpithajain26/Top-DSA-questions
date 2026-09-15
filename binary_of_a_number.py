"""🧩 Binary of a Number — Coding Question

Question:

Write a Python program to convert a given decimal number into its binary representation without using Python's built-in bin() function.

Example 1:

Input: 10
Output: 1010

Explanation:

10 ÷ 2 → remainder 0
5  ÷ 2 → remainder 1
2  ÷ 2 → remainder 0
1  ÷ 2 → remainder 1

Reading remainders from bottom to top:
1010

Example 2:

Input: 7
Output: 111

Example 3:

Input: 15
Output: 1111
💡 Hint

Use:

% 2 → to get the remainder
// 2 → to reduce the number
Remember that the remainders need to be read in reverse order.

Try writing the code yourself first, and send it to me. I'll check it without directly giving you the solution."""
def binary_number(num):
    return bin(num)[2:]
print(binary_number(3))
"""another technique"""
def binary_number(num):
    result=""
    while num>0:
        rem=num%2
        result=str(rem)+result
        num//=2
    return result
print(binary_number(3))