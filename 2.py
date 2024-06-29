class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while True:
            var1 = l1.val if l1 else 0
            var2 = l2.val if l2 else 0
            carry, out = divmod(var1 + var2 + carry , 10)

            current.next = ListNode(out)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 == None and l2 == None and carry == 0:
                break

        return dummy_head.next


        
