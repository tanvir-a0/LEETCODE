import math
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head
        
        current = head
        
        while current and current.next:
            val1 = current.val
            val2 = current.next.val

            new_val = gcd(val1, val2)

            new_node = ListNode(new_val)

            new_node.next = current.next
            current.next = new_node

            # Move current to the node after the newly inserted node
            current = current.next.next
        
        return head
