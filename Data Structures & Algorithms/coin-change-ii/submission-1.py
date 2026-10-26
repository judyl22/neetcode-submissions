class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(index, amount):
            if amount == 0:
                return 1
            if index >= n or amount < 0:
                return 0
            if (index, amount) in memo:
                return memo[(index, amount)]
            path = dfs(index, amount - coins[index]) + dfs(index + 1, amount)
            memo[(index, amount)] = path
            return path
        
        return dfs(0, amount)
            