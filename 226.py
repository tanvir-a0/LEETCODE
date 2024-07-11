# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convert(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        
        node.left, node.right = node.right, node.left
        
        self.convert(node.left)
        self.convert(node.right)


    def invertTree(self, root):
        if root is None:
            return 
        print(root.val)
        head = root
        self.convert(root)
        return head 
            

        