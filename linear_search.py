def linear_search(nums,k):
    for i in nums:
        if i==k:
            return i
    return -1
print(linear_search([1,2,3,4,5,6],3))
def linear_search(nums,target):
    for i in nums:
        if target==i:
            return "found"
    return "not found"
print(linear_search([1,2,3,4,5,6,7],4))