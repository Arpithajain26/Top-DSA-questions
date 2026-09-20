"""Sort Colors — LeetCode #75

Question:

Given an array nums containing n objects colored red, white, or blue, represented by the integers:

0 → Red
1 → White
2 → Blue

Sort the array in-place so that objects of the same color are adjacent, with the colors in the order 0, 1, 2.

You must solve the problem without using a sorting function such as sort() or sorted().

Example 1:

Input:  nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input:  nums = [2,0,1]
Output: [0,1,2]"""
def sort_colors(nums):
    low=0
    high=len(nums)-1
    mid=0
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1

        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
print(sort_colors([2,0,2,1,1,0]))
def sort_colors1(nums):
    low=0
    high=len(nums)-1
    mid=0
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

print(sort_colors1([2,0,2,1,1,0]))