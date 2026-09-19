"""Find the Unique Element

Question:
Given an integer array nums where every element appears twice except for one element that appears only once, find and return the element that appears only once.

Example 1:

Input:  [2, 2, 1]
Output: 1

Example 2:

Input:  [4, 1, 2, 1, 2]
Output: 4

Example 3:

Input:  [1]
Output: 1

Constraint:

Exactly one element appears once.
All other elements appear exactly twice"""
def find_unique_elm(nums):
    nums.sort()
    for i in range(0,len(nums)-2,2):
        if nums[i]!=nums[i+1]:
            return nums[i]
    return nums[-1]
print(find_unique_elm([4,1,2,1,2]))

def find_unique_element(nums):
    nums.sort()
    for i in range(0,len(nums)-2,2):
        if nums[i]!=nums[i+1]:
            return nums[i]
    return nums[-1]
print(find_unique_element([4,1,2,1,2]))

