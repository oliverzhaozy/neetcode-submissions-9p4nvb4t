# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        res.append([root.val])

        while queue:
            curr_level = []

            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    curr_level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    curr_level.append(node.right.val)
                
            res.append(curr_level)
        
        res.pop()
        return res