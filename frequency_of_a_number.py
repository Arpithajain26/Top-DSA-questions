"""Question: Frequency of a Number

Given an integer array nums and an integer target, find how many times target appears in the array.

Return the frequency (count) of target.

Example 1:

Input:  nums = [1, 2, 2, 3, 2, 4], target = 2
Output: 3

Example 2:

Input:  nums = [5, 1, 5, 5, 2], target = 5
Output: 3

Example 3:

Input:  nums = [1, 2, 3, 4], target = 6
Output: 0

Function:

def frequency(nums, target):
    # write your code"""
def frequency_of_a_number(nums,target):
    count=0
    for i in nums:
        if i==target:
            count+=1
    return count
print(frequency_of_a_number([1,2,3,4],6))
