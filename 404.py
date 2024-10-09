# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, left_sum = 0):
        if root is None:
            return left_sum
        print("current node: ", root.val)
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                left_sum = left_sum + root.left.val
        left_sum = self.traverse(root.left, left_sum)
        left_sum = self.traverse(root.right, left_sum)
        return left_sum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = self.traverse(root = root, left_sum = 0)
        print(result)
        return result
        
