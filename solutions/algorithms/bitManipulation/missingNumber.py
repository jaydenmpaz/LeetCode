class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # XOR from 1 to n
        for i in range(1, n + 1):
            ans ^= i
        # XOR all elements in nums
        for num in nums:
            ans ^= num
        # We will be left with the missing number
        return ans