# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root):
            # Base case
            if not root:
                return 0

            left_branch = right_branch = 0
            left_branch = max(left_branch, dfs(root.left))
            right_branch = max(right_branch, dfs(root.right))
            self.res = max(self.res, left_branch + right_branch + root.val)
            return root.val + max(left_branch, right_branch)
        
        dfs(root)
        return self.res