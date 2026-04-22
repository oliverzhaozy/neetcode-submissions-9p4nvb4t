# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None
        
        # Search for the node:
        # If key is on the left branch
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        # If key is on the right branch
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key is found
        else:
            # If target node has 0 or 1 child
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            # If target node has 2 children
            else:
                lowestValue = self.lowestValueNode(root.right)
                root.val = lowestValue
                root.right = self.deleteNode(root.right, lowestValue)
        return root


    def lowestValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val