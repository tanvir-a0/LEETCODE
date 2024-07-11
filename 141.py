# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        visited_li = []
        if head is None:
            return False
            
        while True:
            #print(head.val)

            visited_li.append(head)

            head = head.next
            
            if head in visited_li:
                return True
            
            if head is None:
                return False
                break
        return False
            

        