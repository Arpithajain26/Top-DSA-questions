"""LeetCode #20 — Valid Parentheses

Question:
Given a string s containing only the characters (, ), {, }, [ and ], determine whether the input string is valid.

A string is valid if:

Every opening bracket has a corresponding closing bracket.
Brackets close in the correct order.
Each closing bracket matches the most recent unmatched opening bracket.

Examples:

Input:  s = "()"
Output: True
Input:  s = "()[]{}"
Output: True
Input:  s = "(]"
Output: False
Input:  s = "([{}])"
Output: True
Input:  s = "([)]"
Output: False
Your task"""
def valid_paranthesis(s):
    stack=[]
    for ch in s:
        if ch in '[({':
            stack.append(ch)
        else:
            if not stack:
                return False
            top=stack.pop()
            if (ch==']' and top!='[') or (ch==')' and top!='(') or (ch=='}' and top!='{'):
                return False
    return len(stack)==0
print(valid_paranthesis("()[]{}"))