"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Interleave copied nodes inside original list
        cur = head
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next
        
        # Assign the random pointers of the copied nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # Separate the copied list from the original list
        dummy = Node(0, head)
        cur = dummy
        while cur.next:
            nxt = cur.next.next
            cur.next = cur.next.next
            cur = nxt

        return dummy.next