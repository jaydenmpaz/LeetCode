class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # Detect if cycle exists within our input
        # Effectively, we are using indexes as pointers
        # Setting indexes is equivalent to taking the next
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find location where pointers intersect of the cycle
        # Iterating one step at a time from the head point before collision
        # Results in eventually reaching the value
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow