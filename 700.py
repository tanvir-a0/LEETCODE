# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, val):
        if root is None:
            return 
        
        if root.val == val:
            return root

        return self.traverse(root.left, val) or self.traverse(root.right, val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traverse(root, val)
        
