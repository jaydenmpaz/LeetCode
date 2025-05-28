class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def get_max(nums):
            prevRob = 0
            maxRob = 0

            for cur in nums:
                temp = max(maxRob, prevRob + cur)
                prevRob = maxRob
                maxRob = temp
            
            return maxRob

        
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])

    """ 
    INTUITION
        2 DECISIONS

        Rob the current house (which means you can't rob the previous one),
        OR
        Skip the current house (and keep the max loot so far).

        USE A HELPER FUNCTION TO MAKE 3 SEPARATE CALLS,
        ONE WHERE WE DO NOT INCLUDE THE FIRST HOUSE
        ONE WHERE WE DO NOT INCLUDE THE LAST HOUSE
        AND SPECIAL CASE WHERE THERE IS ONLY ONE VALUE IN INPUT
    """