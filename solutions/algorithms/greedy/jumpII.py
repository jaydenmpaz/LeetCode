class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy approach. Track total jumps made, end of current jump range, and furthest index we can reach
        """
        jumps = 0
        currEnd = 0
        currFarthest = 0

        for i in range(len(nums) - 1):
            # Update farthest position we can reach with any index in current range
            # i + nums[i] is how far we can jump from current position, think actual place in array
            currFarthest = max(currFarthest, i + nums[i])

            # Current jump range is met, we must make another jump
            if (i == currEnd):
                jumps += 1
                currEnd = currFarthest # Set currEnd to currFarthest for new jump range
        

        return jumps