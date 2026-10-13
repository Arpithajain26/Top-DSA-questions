def swap_two_numbers(nums):
    i=0
    j=len(nums)-1
    while i<j:
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    return nums
print(swap_two_numbers([1,2,4,12,3]))