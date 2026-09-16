"""Factorial of a Number — Coding Question

Problem Statement:
Given a non-negative integer n, write a function to find the factorial of n.

The factorial of n is the product of all positive integers from 1 to n.

Formula:
n! = n × (n-1) × (n-2) × ... × 1

Examples:

Input: 5
Output: 120

Input: 4
Output: 24

Input: 0
Output: 1

Expected approach: Use a loop to calculate the factorial.

Function:

def factorial(n):
    # your code

Time Complexity: O(n)
Space Complexity: O(1)"""
def factorial(n):
    if n==1:
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(3))