# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find Middle of Linked List
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        curr = slow

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_


        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True