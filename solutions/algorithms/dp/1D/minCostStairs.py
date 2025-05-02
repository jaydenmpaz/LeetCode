class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        n = len(cost)

        if (n <= 2):
            return min(first, second)
        
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr

        
        return min(first, second)

    
    """
    INTUITION DYNAMIC PROGRAMMING
    
    Take the cheaper step of the first 2
    If there is less than 2 step, then take the min

    now we iterate
    from step 2 onward,
        calculate the current cost, which is current step + the min of previous 2
        set first to second
        and second to curr


    return our final first and second calculated values
"""