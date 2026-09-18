"""LeetCode #33 — Search in Rotated Sorted Array

Question:

You are given an integer array nums that was originally sorted in ascending order but has been rotated at an unknown position.

Given a target integer target, return the index of target if it exists in nums. Otherwise, return -1.

You must solve the problem in O(log n) time.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1"""
def search_in_rotated_array(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(search_in_rotated_array([4,5,6,7,0,1,2],3))