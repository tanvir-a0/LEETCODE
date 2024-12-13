# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def count_total_node(self, head, count):
#         if head is None:
#             return count
#         return self.count_total_node(head.next, count + 1)

#     def traverse_and_remove(self, head, n, current = 0, previous_node = None):
#         if current == n:
#             print("found the one: ", head.val)
#             print("head: ", head, " previous_node: ", previous_node)
#             if previous_node is None:
#                 head = None
#                 return
#             else:
#                 previous_node.next = head.next
#                 return
        
#         if head is not None:
#             self.traverse_and_remove(head.next, n, current = current + 1, previous_node = head)

#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         total_node = self.count_total_node(head, count = 0)
#         print(total_node)
#         self.traverse_and_remove(head = head, n = total_node - n, current = 0)
#         return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head

        back = temp
        forward = temp

        for _ in range(n+1):
            back = back.next

        #print(back,"\n", forward)

        while back is not None:
            back = back.next
            forward = forward.next
        
        #print(back,"\n", forward)

        forward.next = forward.next.next

        return temp.next
