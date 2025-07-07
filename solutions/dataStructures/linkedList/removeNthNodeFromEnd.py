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

        # Move fast pointer n + 1 steps ahead, so slow points to node before
        # the one we want to remove
        for i in range(n + 1):
            if (fast):
                fast = fast.next

        # Iterate fast pointer to end of linked list, keeping gap of n nodes
        while fast:
            slow = slow.next
            fast = fast.next

        # Actively removes the nth node by setting next pointer to next.next
        slow.next = slow.next.next

        # Return the head of the linked list
        return dummy.next