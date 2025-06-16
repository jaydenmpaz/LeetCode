class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(currentSum, maxSum)

        return maxSum

"""
The key idea is that at every index, you either:
Continue the existing subarray (currentSum + nums[i]) or Start a new subarray (nums[i]).
This ensures that currentSum always holds the best possible sum ending at i, making maxSum store the maximum sum encountered.
"""