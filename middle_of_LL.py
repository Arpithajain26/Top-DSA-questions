"""🧩 Middle of the Linked List — LeetCode #876

Question:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
You can assume the linked list is non-empty.

Example:

Input: 1 → 2 → 3 → 4 → 5
Output: 3 → 4 → 5

Input: 1 → 2 → 3 → 4 → 5 → 6
Output: 4 → 5 → 6"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
        return slow
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Call the function
result = Solution().middleNode(head)

# Print the result
print(result.val)