class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        i = 2
        while i <= len(cost):
            temp = dp[1]
            dp[1] = min(cost[i - 2] + dp[0], cost[i - 1] + temp)
            dp[0] = temp
            i += 1
        return dp[1]