"""Merge Sorted Array

Question:
You are given two sorted integer arrays nums1 and nums2.

nums1 contains m valid elements followed by n empty spaces (0s).
nums2 contains n valid elements.
Merge nums2 into nums1 so that nums1 becomes a single sorted array in non-decreasing order.
The merging must be done in-place, without using another array.

Example 1:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]

Example 2:

Input:
nums1 = [1], m = 1
nums2 = [], n = 0

Output:
[1]

Example 3:

Input:
nums1 = [0], m = 0
nums2 = [1], n = 1

Output:
[1]"""
def merge_sorted_array(num1,m,num2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1
    while j>=0:
        num1[k]=num2[j]
        j-=1
        k-=1
    return num1
print(merge_sorted_array([1,2,3,0,0,0],3, [2,5,6],3))
def merge_two_sorted_array1(num1,m,num2,n):
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1
    while j>=0:
        num1[k]=num2[j]
        j-=1
        k-=1
    return num1
print(merge_two_sorted_array1([1,2,3,0,0,0],3, [2,5,6],3))