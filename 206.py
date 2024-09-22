# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()

        if head is None:
            return head
        else:
            temp = ListNode(head.val, None)
            head = head.next
        while head is not None:
            #print(head.val)
            temp = ListNode(head.val, temp)
            head = head.next
        temp1 = temp
        while temp is not None:
            print(temp.val)
            temp = temp.next
        
        return temp1
        