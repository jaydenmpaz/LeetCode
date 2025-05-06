class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize Hash Map
        prev = {}

        # One Pass Solution
        for i, n in enumerate(nums):
            difference = target - n
            if difference in prev:
                return [prev[difference], i]
            prev[n] = i

        return []