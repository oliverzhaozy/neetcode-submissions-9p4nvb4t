# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        dummy = ListNode()
        tail = dummy

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next

        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2

        return dummy.next
        


