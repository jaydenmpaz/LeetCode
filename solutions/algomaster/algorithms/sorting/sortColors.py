class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        
        idx = 0

        for i in range(3):
            freq = mapping.get(i, 0)
            nums[idx: idx + freq] = [i] * freq
            idx += freq

        