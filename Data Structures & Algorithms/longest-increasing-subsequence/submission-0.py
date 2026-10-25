class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            max_length = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_length = max(max_length, 1 + dp[j])
            dp[i] = max_length
        return max(dp)