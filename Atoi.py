"""Coding Question – Atoi (String to Integer)

Question:

Write a Python program to implement the atoi() function, which converts a string representing an integer into its corresponding integer value.

The function should:

Ignore leading spaces.
Handle an optional + or - sign.
Read digits until a non-digit character is encountered.
Return 0 if there are no valid digits.

Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42

Example 3:

Input: "4193 with words"
Output: 4193

Example 4:

Input: "words and 987"
Output: 0

Example 5:

Input: "+123"
Output: 123"""
"""def atoi(s):
    s=s.strip()
    list1=[]
    list2=['-']
    for i in s:
        if i.isdigit():
            list1.append(i)
        elif i in list2 and len(list1)==0:
            list1.append(i)
        else:
            break
    if list1==[] or list1=='+' or list1=='-':
        return 0
    return int("".join(list1))
"""
def atoi_number(s):
    s=s.strip()
    list1=[]
    list2=['+','-']
    for i in s:
        if i.isdigit():
            list1.append(i)
        elif i in list2 and len(list1)==0:
            list1.append(i)
        else:
            break
    if list1==[] or list1==['+'] or list1==['-']:
        return 0
    sign=1
        
    if list1[0]=='-':
        sign=-1
        list1.pop(0)
    elif list1[0]=='+':
        sign=1
        list1.pop(0)
    num=0
    for i in list1:
        num=num*10+(ord(i)-ord('0'))
    num=num*sign
    if num> 2147483647:
        return  2147483647
    elif num <-2147483648:
        return -2147483648
    return num
print(atoi_number("42"))                 # 42
print(atoi_number("+42"))                # 42
print(atoi_number("-123"))               # -123
print(atoi_number("   456"))             # 456
print(atoi_number("4193 with words"))    # 4193
print(atoi_number("words 987"))  
    
