"""Maximum Subarray — LeetCode #53

Question:
Given an integer array nums, find the subarray with the largest sum and return its sum.

A subarray is a contiguous part of the array.

Example 1:

Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation:
The subarray [4,-1,2,1] has the maximum sum:

4 + (-1) + 2 + 1 = 6

Example 2:

Input:  nums = [1]
Output: 1

Example 3:

Input:  nums = [5,4,-1,7,8]
Output: 23

Because [5,4,-1,7,8] has the largest sum: 23."""
def max_subarray(nums):
    sum=0
    max_sum=0
    for i in range(len(nums)):
        sum+=nums[i]
        max_sum=max(max_sum,sum)
        if sum<0:
            sum=0
            
    
    return max_sum
print(max_subarray([5,4,-1,7,8]))
def max_subarray1(nums):
    sum=0
    max_sum=0
    for i in nums:
        sum+=i
        max_sum=max(max_sum,sum)
        if sum<0:
            sum=0
    return max_sum
print(max_subarray1([5,4,-1,7,8]))