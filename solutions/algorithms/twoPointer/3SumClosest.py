class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        # We are storing the actual result sum in res, not its index or difference from target
        # Exactly one solution, we can initiazlize with first 3 sum
        res = nums[0] + nums[1] + nums[2] 

        # 3 Sum Algorithm, 1 hard index, and 2 pointers
        for i in range(n):
            l = i + 1
            r = n - 1

            while l < r:
                # Calcualte the current sum and its difference
                current = nums[i] + nums[l] + nums[r]
                difference = abs(current - target)

                # If this sum is closer to target, update the result
                if difference < abs(res - target):
                    res = current
                if current < target:
                    l += 1
                elif current > target:
                    r -= 1
                else:
                    return target

        return res

