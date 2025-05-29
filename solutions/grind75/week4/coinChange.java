class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        Arrays.sort(coins);

        // Loop for every amount
        for (int i = 1; i <= amount; i++) {
            // Loop for every coin amount
            for (int coin : coins) {
                // Coin value > amount, break loop early
                if (coin > i) break;

                // Otherwise, calculate difference
                int diff = i - coin;
                // If dp is reachable, update dp with the current minimum between current val and dp diff + 1
                if (dp[diff] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[diff] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}

