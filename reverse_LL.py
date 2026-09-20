class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        temp=head
        prev=None
        while temp:
            front=temp.next 
            temp.next=prev
            prev=temp
            temp=front
        return prev
"""
        stack=[]
        temp=head
        while temp:
            stack.append(temp)
            temp=temp.next 
        if not stack:
            return None 
        head=stack.pop() 
        temp=head
        while stack:
            temp.next=stack.pop()
            temp=temp.next
            
        temp.next=None 
        return head"""

    

# Create Linked List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


# Call function
solution = Solution()
result = solution.reverseList(head)


# Print Linked List
while result:
    print(result.val, end=" → ")
    result = result.next

print("None")