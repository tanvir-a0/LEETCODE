# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_element(self, head, lis):
        if head is None:
            return lis
        #print(lis)
        lis.append(head.val)
        return self.find_element(head.next, lis)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis = self.find_element(head, [])
        for i in range(0, len(lis)//2):
            if lis[i] != lis[len(lis) - i - 1]:
                return False
        return True
        
