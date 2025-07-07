# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Cycle Detection Algorithm
        # If the linked list ends, loop terminates
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the pointers meet, cycle is detected
            if slow == fast:
                # To find the tail, we set slow to head and loop,
                # moving pointers by one node until slow and fast are equal again
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # Return None if no cycle is detected
        return None