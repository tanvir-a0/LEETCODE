import statistics
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travarse(self, head = None, total_traversed = {}):
        if head is None:
            return total_traversed

        if head.val in total_traversed.keys():
            total_traversed[head.val] = total_traversed[head.val] + 1
        else:
            total_traversed[head.val] = 1

        self.travarse(head = head.left, total_traversed = total_traversed)
        self.travarse(head = head.right, total_traversed = total_traversed)
        return total_traversed

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        x = self.travarse(head = root, total_traversed = {})
        print(x)

        max_count = 0
        max_obj =  []
        for key, value in x.items():
            if value > max_count:
                max_count = value
        for key, value in x.items():
            if value == max_count:
                max_obj.append(key)
        
        return max_obj

        
