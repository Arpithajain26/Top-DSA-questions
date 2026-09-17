"""Question: Left Rotate an Array

Problem Statement:
Given an array of integers and an integer k, write a program to left rotate the array by k positions.

A left rotation means that the elements at the beginning of the array are moved to the end.

Example:

Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[3, 4, 5, 1, 2]

Another example:

Input:
arr = [10, 20, 30, 40, 50]
k = 3

Output:
[40, 50, 10, 20, 30]"""
def left_rotate(arr,k):
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    arr[:]=reversed(arr[:])
    return arr
print(left_rotate([10,20,30,40,50],3))


# right rotation
"""Problem Statement:
Given an array of integers and an integer k, write a program to right rotate the array by k positions.

A right rotation means that the elements at the end of the array are moved to the beginning.

Example 1:

Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]

Example 2:

Input:
arr = [10, 20, 30, 40, 50]
k = 3
[50,40,30,20,10]
Output:
[30, 40, 50, 10, 20]
"""
def right_rotation(arr,k):
    arr[:]=reversed(arr[:])
    arr[:k]=reversed(arr[:k])
    arr[k:]=reversed(arr[k:])
    return arr
print(right_rotation([10,20,30,40,50],3))