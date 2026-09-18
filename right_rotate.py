def right_rotate(nums,k):
    k=k%len(nums)
    nums[:]=reversed(nums[:])
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    return nums
"""1. nums = [1,2,3,4,5,6,7], k = 3
   Output: [5,6,7,1,2,3,4]

2. nums = [1,2,3,4,5], k = 2
   Output: [4,5,1,2,3]

3. nums = [1,2,3,4], k = 1
   Output: [4,1,2,3]"""
print(right_rotate([1,2,3,4,5,6,7],3))
print(right_rotate([1,2,3,4,5],2))