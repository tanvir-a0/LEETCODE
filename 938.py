# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, low, high):
        if root is None:
            return 0
        
        # Initialize the sum with 0
        sum = 0
        
        # Add root's value if it is within the range
        if low <= root.val <= high:
            sum += root.val
        
        # Traverse left and right subtrees and accumulate the sum
        sum += self.traverse(root.left, low, high)
        sum += self.traverse(root.right, low, high)
        
        return sum
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.traverse(root, low, high)
