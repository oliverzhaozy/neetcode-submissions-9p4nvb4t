# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif self.isSameTree(root, subRoot):
            return True

        checkLeft = self.isSubtree(root.left, subRoot)
        checkRight = self.isSubtree(root.right, subRoot)
        return checkLeft or checkRight


    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif root.val != subRoot.val:
            return False

        checkLeft = self.isSameTree(root.left, subRoot.left)
        checkRight = self.isSameTree(root.right, subRoot.right)

        return checkLeft and checkRight