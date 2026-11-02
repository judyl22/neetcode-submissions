class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]
            if index + nums[index] >= n - 1:
                memo[index] = 1
                return 1
            end = index + nums[index]
            res = float('inf')
            for i in range(index + 1, min(end, n - 2) + 1):
                res = min(res, 1 + dfs(i))
            memo[index] = res
            return res
        
        return dfs(0)