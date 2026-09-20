"""longest Common Prefix — Problem

Problem:
Given an array of strings strs, find the longest common prefix shared by all the strings.

If there is no common prefix, return an empty string "".

Example 1:

Input:  ["flower", "flow", "flight"]
Output: "fl"

Example 2:

Input:  ["dog", "racecar", "car"]
Output: """""
def longest_common_prefix(s):
    word=s[0]
    for i in range(len(word)):
        for ch in s[1:]:
            if i==len(ch) or word[i]!=ch[i]:
                return word[0:i]
    return word
print(longest_common_prefix(["flower","flow","flight"]))
def longest_common_prefic(s):
    words=s[0]
    for i in range(len(words)):
        for ch in s[1:]:
            if i==len(ch) or words[i]!=ch[i]:
                return words[0:i]
    return words
print(longest_common_prefic(["flower","flow","flight"]))