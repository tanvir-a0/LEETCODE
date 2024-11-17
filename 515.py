# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largest_value_in_level(self, root, label_dict, current_label):
        if root is None:
            return label_dict

        if current_label in label_dict:
            label_dict[current_label].append(root.val)
        else:
            label_dict[current_label] = []
            label_dict[current_label].append(root.val)

        self.largest_value_in_level(root.left, label_dict, current_label+1)
        self.largest_value_in_level(root.right, label_dict, current_label+1)

        
        #print(label_dict)
        return label_dict

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dic = self.largest_value_in_level(root = root, label_dict = {}, current_label = 0)
        #print(dic)

        result_li = []
        for key, value in dic.items():
            result_li.append(max(value))
        
        return result_li
        
