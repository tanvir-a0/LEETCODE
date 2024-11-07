"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, root = None, current_floor = 1):
        if root is None:
            return current_floor
        print(root.val, current_floor)
        floor_of_child = []
        for child in root.children:
            floor_of_child.append(self.traverse(root = child, current_floor = current_floor + 1))

        if len(floor_of_child) == 0:
            return current_floor
        return(max(floor_of_child))

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        return self.traverse(root = root, current_floor = 1)
        
