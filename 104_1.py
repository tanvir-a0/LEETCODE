#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def max_height(self, root):
        if root == None:
            return 0
        
        l = self.max_height(root.left)
        r = self.max_height(root.right)
        return max(l,r) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_height(root)
        
        