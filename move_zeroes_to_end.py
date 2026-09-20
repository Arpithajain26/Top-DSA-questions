"""Move Zeroes to the End — LeetCode #283

Question:
Given an integer array nums, move all 0s to the end of the array while maintaining the relative order of the non-zero elements.

You must modify the array in-place without creating another array.

Example 1:

Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Example 2:

Input:  [0]
Output: [0]

Example 3:

Input:  [1, 0, 2, 0, 3]
Output: [1, 2, 3, 0, 0]"""
def move_zeroes_end(nums):
    j=-1
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    if j==-1:
        return nums
    for i in range(j+1,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
print(move_zeroes_end([1,0,2,0,3]))
def move_zeroes_to_end(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    for i in range(j+1,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
print(move_zeroes_to_end([1,0,2,0,3]))