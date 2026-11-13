# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        mid = math.ceil(length / 2)
        cur2 = head
        for _ in range(mid - 1):
            cur2 = cur2.next
        nxt2 = cur2.next
        cur2.next = None
        cur2 = nxt2
        
        # reverse the second half of the linked list
        prev = None
        while cur2:
            nxt2 = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = nxt2
        cur2 = prev

        # start reordering nodes
        cur = head
        while cur2:
            nxt = cur.next
            cur.next = cur2
            cur = nxt

            nxt2 = cur2.next
            cur2.next = cur
            cur2 = nxt2


        
