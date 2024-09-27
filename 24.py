# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while True:
            if head == None:
                break
            if head.next != None:
                #Then switch them
                head.val, head.next.val =  head.next.val, head.val

                if head.next.next != None:
                    head = head.next.next
                else:
                    break
            else:
                break
            
        return temp
                
        
