class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        check = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                check[i][j] = s[i] == s[j] and (j - i <= 1 or check[i + 1][j - 1] == True)
                if check[i][j] and j - i > end - start:
                    start, end = i, j
        return s[start:end+1]
