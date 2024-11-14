# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getmaxdepth(self, root, depth):
        if root is None:
            return depth
        return max(self.getmaxdepth(root.left, depth+1), self.getmaxdepth(root.right, depth+1))
    
    def get_bottom_left(self, root, target_depth, depth):
        if root is None:
            return None
        
        print("current depth: ", depth, " target depth: ", target_depth)
        if depth == target_depth:
            return root.val

        value=self.get_bottom_left(root.left, target_depth, depth+1)
        if value is not None:
            return value
        value = self.get_bottom_left(root.right, target_depth, depth+1)
        if value is not None:
            return value
        
        return value

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = self.getmaxdepth(root, 0)
        print(depth)

        return self.get_bottom_left(root = root, target_depth = depth, depth = 1)
        
