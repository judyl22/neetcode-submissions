class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            coin = coins[i]
            for j in range(1, amount + 1):
                # don't use the current coin
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                # use the current coin
                if j - coin >= 0:
                    dp[i][j] += dp[i][j - coin]
        return dp[-1][-1]