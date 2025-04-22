class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if (prices[i] > prices[i - 1]):
                profit += prices[i] - prices[i - 1]

        return profit

        """
        Intialize profit counter

        Iterate from 2nd element, to last
        If larger price is found after, profit is there so sell immediately
            profit = large - small
        
        return profit
        """