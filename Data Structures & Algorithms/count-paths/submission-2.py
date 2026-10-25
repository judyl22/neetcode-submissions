class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        def dp(row, col):
            if row == m or col == n:
                return 0
            if memo[row][col] != 0:
                return memo[row][col]
            if row == m - 1 and col == n - 1:
                memo[row][col] = 1
                return 1
            path = dp(row + 1, col) + dp(row, col + 1)
            memo[row][col] = path
            return path
        
        dp(0, 0)
        return dp(0, 0)