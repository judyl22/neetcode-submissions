class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        # memo 2d arr: row num = len(text1), col num = len(text2)
        memo = [[-1] * len(text2) for _ in range(len(text1))] 

        for i1 in range(len(text1) - 1, -1, -1):
            for i2 in range(len(text2) - 1, -1, -1):
                if text1[i1] == text2[i2]:
                    memo[i1][i2] = 1
                    if i1 + 1 < len(text1) and i2 + 1 < len(text2):
                        memo[i1][i2] = memo[i1][i2] + memo[i1 + 1][i2 + 1]
                else:
                    memo[i1][i2] = 0
                    if i1 + 1 < len(text1):
                        memo[i1][i2] = max(memo[i1][i2], memo[i1 + 1][i2])
                    if i2 + 1 < len(text2):
                        memo[i1][i2] = max(memo[i1][i2], memo[i1][i2 + 1])
        return memo[0][0]