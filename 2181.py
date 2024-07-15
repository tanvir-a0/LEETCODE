# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = head.next, head.next
        sum = 0
        while current:
            x = current.val
            if x!= 0:
                sum = sum + x
            else:
                previous.val = sum
                previous.next = current.next
                previous = previous.next
                sum = 0

            current = current.next
            print(x)
        
        return head.next
        