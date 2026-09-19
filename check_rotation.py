"""🔄 Check Rotation — Coding Question

Question:
Given two strings s1 and s2, write a Python program to check whether s2 is a rotation of s1.

A string is considered a rotation if it can be obtained by moving some characters from the beginning of the string to the end.

Example 1:

Input:
s1 = "abcd"
s2 = "cdab"

Output:
True

Explanation:
"abcd" → move "ab" to the end → "cdab", so s2 is a rotation of s1.

Example 2:

Input:
s1 = "abcd"
s2 = "acbd"

Output:
False

Expected approach:
Try to solve it using the idea that s2 should be present inside s1 + s1.

Example:

"abcd" + "abcd" = "abcdabcd"

"cdab" is present in "abcdabcd" → rotation ✅"""
def check_rotation(s1,s2):
    x=s2+s2
    if s1 in x:
        return True
    return False
    
print(check_rotation("abcd","cdab"))
def check_rotation1(s1,s2):
    x=s1+s2
    if s1 in x:
        return True
    return False
print(check_rotation1("abcd","cdab"))
