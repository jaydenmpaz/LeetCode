class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res
            

"""
    INTUITION
        - Sort the original array
        - Initialize pointers, i will start at the beginning, j will be element after i, and k will be last element
        - Begin iteration, skip duplicate elements
        - Check if nums[i] + nums[j] + nums[k]
        - If greater, increment j, if less decrement k, if equal append result, skip duplicate elements
        - Return result
"""
