# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        len = 0
        while True:
            len = len + 1
            head = head.next
            if head == None:
                break
        if len == 1:
            return temp

        head = temp
        if len % 2 == 0:
            x = 0
            while True:
                x = x + 1
                head = head.next
                if x == int(len/2):
                    return head
                    break
                if head == None:
                    break

        else:
            x = 0
            while True:
                x = x + 1
                head = head.next
                if x == int(len/2):
                    print("here")
                    return head
                    break
                if head == None:
                    break

        