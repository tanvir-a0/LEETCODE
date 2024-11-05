# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_equal(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        return self.check_equal(root1.left, root2.left) and self.check_equal(root1.right, root2.right)

    def traverse(self, root, subroot):
        if root is None:
            return False
        if self.check_equal(root, subroot):
            return True
        return self.traverse(root.left, subroot) or self.traverse(root.right, subroot)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        return self.traverse(root, subRoot)
        
