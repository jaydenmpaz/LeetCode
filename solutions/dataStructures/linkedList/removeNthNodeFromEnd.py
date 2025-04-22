# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast pointer n + 1 steps ahead of slow
        for i in range(n + 1):
            if (fast):
                fast = fast.next
        
        # Iterate both pointers till fast reaches end of list
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node (currently at slow.next.next)
        slow.next = slow.next.next

        return dummy.next