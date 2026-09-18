"""Question:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that exactly one solution exists.
You cannot use the same element twice.
Return the answer in any order.

Example 1:

Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

Example 2:

Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:

Input:  nums = [3, 3], target = 6
Output: [0, 1]"""
def two_sum(nums,target):
    mpp={}
    for i in range(len(nums)):
        num=target-nums[i]
        if num in mpp:
            return [i,mpp[num]]
        mpp[nums[i]]=i
    return
print(two_sum([2, 7, 11, 15],9))