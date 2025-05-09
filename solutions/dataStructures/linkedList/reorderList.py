# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return

        # First we need to find the middle
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Next, we need to reverse the second half of the list, this will help with our merging step
        cur = slow.next
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        slow.next = None

        # Now merge the two lists
        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
        
        """
        INTUITION
        WE CAN SEE A PATTERN. WE ARE ALTERNATING FROM BOTH ENDS OF THE LIST!
        SO WE CAN ASSUME WE NEED TO DO THREE THINGS:
        - FIND MIDDLE POINT TO DIVIDE LIST INTO 2
        - REVERSE THE SECOND HALF (SEE EX: L0, LN, L1, LN-1...)
        - MERGE THE FIRST HALF AND REVERSED SECOND HALF TOGETHER
        """