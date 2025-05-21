class Solution {
    public int bestTimeToBuyAndSellStock(int[] prices) {
        int n = len(prices);
        int max_profit = 0
        int min_buy = prices[0]

        for (int i = 1; i < prices.length; i++) {
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        }
            
        return max_profit
}