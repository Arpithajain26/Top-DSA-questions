# bubble sort compares adjacent elements and swaps them in they are in the wrong order
def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
print(bubble_sort([5,3,8,1,2]))