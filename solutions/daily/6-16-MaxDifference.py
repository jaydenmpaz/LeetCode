class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        minNum = nums[0]
        for i in range(1, len(nums)):
            res = max(res, nums[i] - minNum)
            minNum = min(minNum, nums[i])

        return res if res != 0 else -1


        # Brute Force
        # res = -1
        # maxDiff = float(-inf)
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[j] < nums[i]:
        #             continue
        #         elif nums[i] < nums[j] and nums[j] - nums[i] > maxDiff:
        #             maxDiff = nums[j] - nums[i]
        

        # return maxDiff if maxDiff != float(-inf) else res