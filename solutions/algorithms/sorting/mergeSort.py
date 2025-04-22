# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # LeetCode 148
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Find the middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Separate into 2 halves
        mid = slow.next
        slow.next = None

        # Recursively call on each
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        return self.merge(left, right)


    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        temp.next = l1 if l1 else l2

        return dummy.next