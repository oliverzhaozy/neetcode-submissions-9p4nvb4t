# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.get_height(root)
        return self.diameter

    
    def get_height(self, node):
        if not node:
            return 0

        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)

        self.diameter = max(leftHeight + rightHeight, self.diameter)
        return 1 + max(leftHeight, rightHeight)