# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        length = 0

        # Find length of linked list
        while ptr:
            ptr = ptr.next
            length += 1

        # If the head needs to be removed
        if length == n:
            return head.next

        # Traverse ptr2 to the node which is to be removed, and ptr1 to the node before
        ptr1, ptr2 = head, head
        for i in range(length - n - 1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr2 = ptr2.next
        
        # Remove the node
        tmp = ptr2.next
        ptr2.next = None
        ptr1.next = tmp

        return head

