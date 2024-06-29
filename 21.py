class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        
        while True:

            if list2 == None:
                current.next = list1
                break
            if list1 == None:
                current.next = list2
                break

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            current = current.next
            

        
        return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create test lists
list1 = create_linked_list([2, 4, 6])
list2 = create_linked_list([1, 3, 5, 7, 9])

# Initialize Solution
solution = Solution()

# Merge lists
merged_list = solution.mergeTwoLists(list1, list2)

# Print merged list
print_linked_list(merged_list)
