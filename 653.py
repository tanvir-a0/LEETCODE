# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []

    def find_list(self, root):
        if root is not None:
            #print(root.val, self.lst)
            self.lst.append(root.val)
            self.find_list(root.left)
            self.find_list(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.find_list(root)
        #print(self.lst)
        self.lst.sort()
        print(self.lst)

        if len(self.lst) == 1:
            return False

        left = 0
        right =  len(self.lst) - 1
        while True:
            if left == right:
                summ = self.lst[left] 
            else:
                summ = self.lst[left] + self.lst[right]
            #print(f"summ: {summ}, left: {left}, right: {right}")
            if summ == k:
                return True
            if summ < k:
                left = left + 1
            if summ > k:
                right = right - 1
            
            if left >= right:
                break
            if left < 0:
                break
            if right >= len(self.lst):
                break
        
        return False
            
        
