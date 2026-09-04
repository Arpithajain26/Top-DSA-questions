# selecction sort: selection sort repeatedly finds the smallest element and swaps them at the correct position
def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if nums[min_index]>nums[j]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
print(selection_sort([5,3,8,1,2]))
