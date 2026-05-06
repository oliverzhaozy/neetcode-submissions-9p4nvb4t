# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # Have a fast and slow ptr to find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Set the middle node to point to NULL so as to "cut" both halves
        right = slow.next
        slow.next = None

        # Reverse linked list for nodes after the middle
        prev = None
        while right:
            next_node = right.next
            right.next = prev 
            prev = right
            right = next_node

        # Merge the two halves
        left = head
        while prev:
            tmp1, tmp2 = left.next, prev.next
            left.next = prev
            prev.next = tmp1
            left, prev = tmp1, tmp2