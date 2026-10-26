class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        num_sum = sum(nums)
        if target > num_sum or target < -num_sum:
            return 0
        dp = [[0] * (num_sum * 2 + 1) for _ in range(len(nums) + 1)]
        dp[0][num_sum] = 1
        for i in range(len(nums)):
            for j in range(num_sum * 2 + 1):
            # since the col num of dp is 2 * nums_sum + 1
                if dp[i][j] != 0:
                    if j + nums[i] <= num_sum * 2:
                        dp[i + 1][j + nums[i]] += dp[i][j]
                    if j - nums[i] >= 0:
                        dp[i + 1][j - nums[i]] += dp[i][j]
        return dp[-1][target + num_sum]