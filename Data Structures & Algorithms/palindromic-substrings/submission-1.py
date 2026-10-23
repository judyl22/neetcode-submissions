class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        check = [[False] * n for _ in range(n)]
        tot = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or check[i + 1][j - 1] == True):
                    tot += 1
                    check[i][j] = True
        return tot