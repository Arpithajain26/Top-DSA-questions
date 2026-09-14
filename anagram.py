"""Question: Check Anagram

Given two strings, write a program to check whether they are anagrams of each other.

Two strings are called anagrams if they contain the same characters with the same frequencies, but the order of the characters can be different.

Example 1:

Input:
s1 = "listen"
s2 = "silent"

Output:
True

Example 2:

Input:
s1 = "hello"
s2 = "world"

Output:
False

Example 3:

Input:
s1 = "triangle"
s2 = "integral"

Output:
True

Constraints:

Strings contain lowercase English letters.
The strings can be of different lengths.

👉 Your task: Return True if the two strings are anagrams; otherwise return False."""
from typing import Counter
def check_anargam(s1,s2):
    if Counter(s1)==Counter(s2):
        return True
    return False
print(check_anargam("listen","silent"))

# another solution
def check_anargam(s1,s2):
    mpp1={}
    mpp2={}
    for i in s1:
        mpp1[i]=mpp1.get(i,0)+1
    for j in s2:
        mpp2[j]=mpp2.get(j,0)+1
    return mpp1==mpp2
print(check_anargam("listen","silent"))