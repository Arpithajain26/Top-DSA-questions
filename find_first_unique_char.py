"""Question: Find the First Unique Character

Given a string s, find the first character that appears only once in the string.

Return the index of that character. If there is no unique character, return -1.

Examples:

Input:  s = "leetcode"
Output: 0
Explanation: 'l' appears only once and is the first unique character.
Input:  s = "loveleetcode"
Output: 2
Explanation: 'v' is the first character that appears only once.
Input:  s = "aabb"
Output: -1
Explanation: There is no unique character.

Expected approach: Use a frequency count (hash map/dictionary)."""
def find_first_unique_char(s):
    mpp={}
    for i in s:
        mpp[i]=mpp.get(i,0)+1
    for i in range(len(s)):
        if mpp[s[i]]==1:
            return i
    return -1
print(find_first_unique_char("leetcode"))

def find_first_unique(s):
    mpp={}
    for i in s:
        mpp[i]=mpp.get(i,0)+1
    for i in range(len(s)):
        if mpp[s[i]]==1:
            return i
    return -1
print(find_first_unique("loveleetcode"))