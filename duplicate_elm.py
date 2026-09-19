"""🟢 Duplicate Elements — LeetCode Question

Question:
Given an integer array nums, determine whether any value appears at least twice in the array.

Return True if there is at least one duplicate element; otherwise, return False.

Example 1:

Input:  nums = [1, 2, 3, 1]
Output: True
Explanation: 1 appears twice.

Example 2:

Input:  nums = [1, 2, 3, 4]
Output: False
Explanation: All elements are distinct.

Example 3:

Input:  nums = [1, 1, 1, 3, 3]
Output: True

Expected approach: Use a set to keep track of elements already seen.

Time: O(n)"""
def duplicate_element(nums):
    list1=[]
    for i in nums:
        if i in list1:
            return True
        list1.append(i)
    return False
print(duplicate_element([1,1,1,2,3]))
# another approach
def duplicates(nums):
    return len(nums)!=len(set(nums))
print(duplicates([1,1,1,3,3]))
def duplicates1(nums):
    return len(nums)!=len(set(nums))
print(duplicates1([1,2,3,4,5,6,1]))