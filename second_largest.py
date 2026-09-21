def find_second_largest(nums):
    max_elm=max(nums)
    min_elm=nums[0]
    for i in nums:
        if i<max_elm and i>min_elm:
            min_elm=i
    return min_elm
print(find_second_largest([1,2,3,2,4,2,4,67,54]))