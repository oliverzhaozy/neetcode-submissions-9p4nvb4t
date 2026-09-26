# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            # Base case
            if not root:
                return False
            
            if not dfs(root.right):
                root.right = None
            if not dfs(root.left):
                root.left = None
            if root.val == target and not root.left and not root.right:
                return False
            return True 
        
        dfs(root)
        if root.val == target and not root.left and not root.right:
            return None
        return root
