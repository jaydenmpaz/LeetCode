class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Filter out negative numbers
        nums = [n for n in nums if n > 0]

        # Calculate the index, check if index is within array bounds and mark negative
        for n in nums:
            idx = abs(n) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1

        # Identify the first missing positive integer
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        # First missing positive integer is one greater than the array size
        return len(nums) + 1