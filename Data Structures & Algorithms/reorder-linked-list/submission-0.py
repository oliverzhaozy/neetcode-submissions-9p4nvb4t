# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_length = 0
        left, left_end, right = head, head, head
        
        # Check length of list
        while right:
            right = right.next
            list_length += 1

        # Reset right ptr to head
        right = head

        # Move right ptr to the node which should appear last 
        for _ in range(math.ceil((list_length - 1) / 2)):
            left_end = left_end.next 

        # Set the middle node to point to NULL so as to "cut" both halves of the linked lists
        right = left_end.next
        left_end.next = None

        # Reverse linked list for nodes after the above node
        prev = None
        while right:
            next_node = right.next
            right.next = prev 
            prev = right
            right = next_node

        # Since right now points to NULL, prev points to the head of the reversed second list
        while prev:
            tmp1, tmp2 = left.next, prev.next
            left.next = prev
            prev.next = tmp1
            left, prev = tmp1, tmp2
            
        return
            


