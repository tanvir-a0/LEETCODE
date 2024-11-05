# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_child_sum(self, root, sum = 0):
        if root is None:
            return sum
        else:
            sum = sum + root.val
        
        sum = sum + self.get_child_sum(root.left) + self.get_child_sum(root.right)
        return sum

    def traverse(self, new_node, root):
        if root is None:
            return 0

        #print(root.val, abs(self.get_child_sum(root.left) - self.get_child_sum(root.right)))
        new_node.val = abs(self.get_child_sum(root.left) - self.get_child_sum(root.right))
        new_node.left = TreeNode()
        new_node.right = TreeNode()
        self.traverse(new_node.left, root.left)
        self.traverse(new_node.right, root.right)
    
    def traverse1(self, root, sum = 0):
        if root is None:
            return 0
        
        sum = sum + root.val
        #print("result val: ", root.val, "sum: ", sum)
        sum = sum + self.traverse1(root.left)
        sum = sum + self.traverse1(root.right)

        return  sum
    def findTilt(self, root: Optional[TreeNode]) -> int:
        new_node = TreeNode()
        self.traverse(new_node, root)
        return self.traverse1(new_node)
