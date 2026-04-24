# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.getHeight(root)
        return self.balanced 

    def getHeight(self, root):
        # Base case
        if not root:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
            return -1

        return 1 + max(leftHeight, rightHeight)
        