# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Initial will hold the dummy node
        # Current will hold our addition values
        initial = ListNode()
        current = initial
        carry = 0

        # Iterate through numbers
        while l1 or l2 or carry:  # Checks carry for edge case
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Current place's addition value
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)

            # Update Pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return initial.next

