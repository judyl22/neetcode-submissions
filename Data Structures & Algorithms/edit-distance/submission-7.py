class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        dp[-1][-1] = 0
        for i in range(m):
            dp[-1][i] = m - i
        for i in range(n):
            dp[i][-1] = n - i
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]