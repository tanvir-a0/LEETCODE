# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.return_li = []

    def postorderTraversal(self, root):
        if root is not None:
            
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.return_li.append(root.val)

        #self.return_li.reverse()
        return self.return_li
        