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
        dummy = Node(0)
        cur, new = head, dummy
        node_map = {None: None}

        # first pass: create the nodes and next pointers
        while cur:
            newNode = Node(cur.val)
            new.next = newNode
            node_map[cur] = newNode
            new = new.next
            cur = cur.next
        
        # second pass: link the random pointers
        cur, new = head, dummy.next
        while cur:
            new.random = node_map[cur.random]
            new = new.next
            cur = cur.next

        return dummy.next