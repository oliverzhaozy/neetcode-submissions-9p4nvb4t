# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        ptr1, ptr2 = list1, list2
        cur = dummy
        
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                cur.next = ptr1
                cur = cur.next
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                cur = cur.next
                ptr2 = ptr2.next
        
        if ptr1:
            cur.next = ptr1
        if ptr2:
            cur.next = ptr2
        
        return dummy.next


            