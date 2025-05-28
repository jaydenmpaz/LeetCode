class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        
        return prev1

    """
    INTUITION DYNAMIC PROGRAMMING
        Get the length of array
        initialize 2 running values, prev1 and prev2
        
        for every house:
            set temp variable to prev1
            calculate new prev1 for current house, equal to the max between prev2 + current and prev1
            set prev2 to old temp

        return prev1
    """