class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(day, flag):
            if day >= n:
                return 0
            if (day, flag) in memo:
                return memo[(day, flag)]
            if flag: # if have coin
                # sell
                profit1 = dp(day + 2, False) + prices[day]
                # not sell
                profit2 = dp(day + 1, flag)
                memo[(day, flag)] = max(profit1, profit2)
                return  memo[(day, flag)]
            else: # if not have coin
                # buy
                profit1 = dp(day + 1, True) - prices[day]
                profit2 = dp(day + 1, flag)
                memo[(day, flag)] = max(profit1, profit2)
                return  memo[(day, flag)]
        
        return dp(0, False)

