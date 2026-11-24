# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy
        for _ in range(length - n):
            cur = cur.next
            
        prev = cur
        cur = cur.next
        nxt = None
        if cur and cur.next:
            nxt = cur.next
        prev.next = nxt
        
        return dummy.next