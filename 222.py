# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node is None:
            return 0
        left_count = self.traverse(node.left)
        right_count = self.traverse(node.right)
        print("node: ", node.val, " sum: ", left_count + right_count + 1)
        return left_count + right_count + 1
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)
        
