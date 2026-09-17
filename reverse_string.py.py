"""Question:
Given a string s, write a Python program to reverse the string without using Python's built-in reverse() function.

Example:

Input:  "hello"
Output: "olleh"

Another example:

Input:  "python"
Output: "nohtyp"

LeetCode:
This exact problem is commonly practiced as LeetCode 344 – Reverse String, where the input is a list of characters and you reverse it in-place."""
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))
print(reverse_string("python"))