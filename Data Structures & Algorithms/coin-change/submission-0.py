class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            res = 1e9
            if amount in memo:
                return memo[amount]
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dp(amount - coin))
            memo[amount] = res
            return memo[amount]
        
        min_coin = dp(amount)
        if min_coin >= 1e9:
            return -1
        else:
            return min_coin