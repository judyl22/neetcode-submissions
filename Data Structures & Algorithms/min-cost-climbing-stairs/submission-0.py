class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost) + 1)

        def dp(index):
            if index == 0 or index == 1:
                cache[index] = 0
                return cache[index]
            if cache[index] != -1:
                return cache[index]
            cache[index] = min(cost[index - 1] + dp(index - 1), cost[index - 2] + dp(index - 2))
            return cache[index]        
        
        return dp(len(cost))
