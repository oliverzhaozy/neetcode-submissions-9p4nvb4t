"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def helper(sr, sc, er, ec): # sr = start row, sc = start col, er = end row, ec = end col
            # Base case
            first_val = grid[sr][sc]
            is_same = True

            for row in range(sr, er + 1):
                for col in range(sc, ec + 1):
                    if grid[row][col] != first_val:
                        is_same = False
            if is_same == True:
                value = False if first_val == 0 else True
                return Node(value, True)
            
            # Recursive case
            node = Node(True, False)
            mid_r = (sr + er) // 2
            mid_c = (sc + ec) // 2
            node.topLeft = helper(sr, sc, mid_r, mid_c) # topLeft
            node.topRight = helper(sr, mid_c + 1, mid_r, ec) # topRight
            node.bottomLeft = helper(mid_r + 1, sc, er, mid_c) # bottomLeft
            node.bottomRight = helper(mid_r + 1, mid_c + 1 , er, ec) # bottomRight
            return node
        
        return helper(0, 0, n - 1, n - 1)
        