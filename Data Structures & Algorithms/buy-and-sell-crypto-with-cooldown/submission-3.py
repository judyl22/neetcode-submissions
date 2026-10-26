class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        # [can buy, can sell]
        dp[-2][0] = 0
        dp[-2][1] = prices[-1]
        for i in range(n - 2, -1, -1):
            # can buy
            # actually buy
            profit1 = dp[i + 1][1] - prices[i]
            # not buy
            profit2 = dp[i + 1][0]
            dp[i][0] = max(profit1, profit2)
            # can sell
            # actually sell
            profit1 = dp[i + 2][0] + prices[i]
            # not sell
            profit2 = dp[i + 1][1]
            dp[i][1] = max(profit1, profit2)
        return dp[0][0]