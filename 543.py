# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node):
        if node is None:
            return 0
        l = self.depth(node.left)
        r = self.depth(node.right)
        return max(l,r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth(root.left) + self.depth(root.right) 
        
        
