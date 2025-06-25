class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = set()

        for j in range(n):
            if nums[j] == key:
                high = min(n - 1, j + k)
                low = max(0, j - k)
                for i in range(low, high + 1):
                    res.add(i)
        
        return sorted(res)

        # Brute force approach
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if nums[j] == key and abs(i - j) <= k:
        #             ans.append(i)
        #             break
        # return ans