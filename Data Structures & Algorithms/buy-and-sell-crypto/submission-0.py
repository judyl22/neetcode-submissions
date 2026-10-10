class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        one_price = 0
        max_profit = 0
        two_price = 1
        while two_price < len(prices):
            if prices[two_price] >= prices[one_price]:
                curr_profit = prices[two_price] - prices[one_price]
                if curr_profit > max_profit:
                    max_profit = curr_profit
                two_price += 1
            else:
                one_price = two_price
                two_price = one_price + 1
        return max_profit