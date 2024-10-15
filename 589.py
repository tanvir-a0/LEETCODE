
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def traverse(self, node = None, order_li = []):
        if node is None:
            return order_li

        order_li.append(node.val)
        for j in node.children:
            order_li = self.traverse(node = j, order_li = order_li)
        
        return order_li

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
            
        print(root.children)
        x = self.traverse(node = root, order_li = [])
        return x

        
