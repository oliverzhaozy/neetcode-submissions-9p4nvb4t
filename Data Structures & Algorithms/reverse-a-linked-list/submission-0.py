# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        next_node = None
        while current is not None:
            # [0, 1, 2, 3]
            next_node = current.next # 1
            current.next = prev # None
            prev = current # 0 
            current = next_node # 1 
        return prev
