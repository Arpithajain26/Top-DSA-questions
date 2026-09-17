"""Question: Remove Duplicates from an Array

Given an array of integers, remove all duplicate elements and return an array containing only unique elements. The input array may be either sorted or unsorted.

Example 1:

Input:  [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]

Example 2:

Input:  [4, 1, 2, 1, 4, 3]
Output: [4, 1, 2, 3]

Interview follow-up:"""
def remove_duplicates(nums):
    return list(set(nums))
print(remove_duplicates([4,1,2,1,4,3]))