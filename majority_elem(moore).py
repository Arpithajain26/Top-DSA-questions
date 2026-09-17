""""Majority Element — Coding Question

Question:
Given an integer array nums of size n, find the majority element.

The majority element is the element that appears more than n/2 times in the array.

You may assume that the majority element always exists.

Example 1:

Input:  nums = [3, 2, 3]
Output: 3

Example 2:

Input:  nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2"""


def majority_element(nums):
    mpp={}
    n=len(nums)
    for i in nums:
        mpp[i]=mpp.get(i,0)+1
    for key,value in mpp.items():
        if value>(n//2):
            return key
    return
print(majority_element([3,2,3]))