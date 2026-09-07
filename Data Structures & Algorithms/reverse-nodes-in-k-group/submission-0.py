# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur, prev_group_tail = dummy, dummy

        # finds total length of linked list 
        length = 0
        while cur.next:
            cur = cur.next
            length += 1
        
        # finds how many groups of k nodes there is
        cur = head
        total_cycles = length // k

        for _ in range(total_cycles):
            group_head = cur 
            prev = None
            
            for _ in range(k):
                # reverses the linked list 
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            prev_group_tail.next = prev
            prev_group_tail = group_head
        
        prev_group_tail.next = cur
        return dummy.next