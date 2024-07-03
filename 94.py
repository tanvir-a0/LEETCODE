# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        
        def loop(node, result):
            if node is not None:
                loop(node.left, result)
                result.append(node.val)
                loop(node.right, result)

        result = []
        loop(root, result)
        return result
            