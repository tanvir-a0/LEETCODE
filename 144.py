# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.return_li = []

    def preorderTraversal(self, root):
        if root is not None:
            self.return_li.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.return_li
        