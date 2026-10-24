class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        target = 1
        while target <= amount:
            smallest = amount + 1
            for coin in coins:
                if coin <= target:
                    need = target - coin
                    smallest = min(smallest, dp[need])
            dp[target] = 1 + smallest
            target += 1
        if dp[amount] == amount + 2:
            return -1
        return dp[amount]