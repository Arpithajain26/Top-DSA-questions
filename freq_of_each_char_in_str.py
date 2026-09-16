"""eetCode-style question: Frequency of Each Character

Question:
Given a string s, return the frequency of each character in the string.

The frequency of a character is the number of times it appears in the string.

Example 1:

Input:  "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Example 2:

Input:  "banana"
Output: {'b': 1, 'a': 3, 'n': 2}

Function:
"""

def char_frequency(s):
    mpp={}
    for i in s:
        mpp[i]=mpp.get(i,0)+1
    return mpp
print(char_frequency("banana"))
print(char_frequency("hello"))
print(char_frequency("banana"))
print(char_frequency("aabbcc"))
print(char_frequency("leetcode"))