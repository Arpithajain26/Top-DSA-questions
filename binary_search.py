"""🔍 Binary Search – Coding Question

Question:
Write a Python program to search for a given element in a sorted array using the Binary Search algorithm.

If the element is found, return its index. Otherwise, return -1.

Example 1:

Input:
arr = [1, 3, 5, 7, 9, 11]
target = 7

Output:
3

Explanation:
The element 7 is present at index 3.

Example 2:

Input:
arr = [1, 3, 5, 7, 9, 11]
target = 6

Output:
-1

Constraint:
The array must be sorted in ascending order.

Expected approach: Use Binary Search with O(log n) time complexity."""
def binary_search(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
print(binary_search( [1, 3, 5, 7, 9, 11],7))