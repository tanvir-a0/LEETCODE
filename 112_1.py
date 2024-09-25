# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travarse(self, root,path = [], targetSum = 0, sums = []):
        if root == None:
            pass
        elif root.left == None and root.right == None:
            print( root.val, path , sum(path) + root.val, sums)
            sums.append(sum(path) + root.val)
        else:
            self.travarse(root.left, path = path + [root.val], targetSum = targetSum, sums = sums)
            self.travarse(root.right,path = path + [root.val], targetSum = targetSum, sums = sums)
        
        return sums

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
            
        x = self.travarse(root = root,path = [], targetSum = targetSum, sums = [])
        print( x )
        if targetSum in x:
            return True
        
        return False

        

        