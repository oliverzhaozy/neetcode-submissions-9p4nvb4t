# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {} # maps node to index for inorder array
        for i in range(len(inorder)):
            index_map[inorder[i]] = index_map.get(inorder[i], i)
        
        self.pre_i = 0
        def dfs(in_left, in_right):
            # Base case
            if in_left > in_right:
                return None
            
            root_val = preorder[self.pre_i]
            root = TreeNode(root_val)
            self.pre_i += 1

            mid = index_map[root_val]
            root.left = dfs(in_left, mid - 1)
            root.right = dfs(mid + 1, in_right)
            return root
        
        return dfs(0, len(preorder) - 1)