"""Question: Detect a Loop in a Linked List

Given the head of a singly linked list, determine whether the linked list contains a loop (cycle).

A loop exists if, while traversing the linked list, you encounter a node that you have already visited.

Example 1:

1 → 2 → 3 → 4
        ↑   ↓
        ← ←

Output: True

Example 2:

1 → 2 → 3 → 4 → None

Output: False"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
print(detect_loop(head1))