class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]

        def isPal(i, j):
            if j < i:
                return False
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(len(s)):
            for j in range(len(s)):
                dp[i][j] = isPal(i, j)

        def backtrack(start):
            if start == len(s):
                res.append(curr.copy())
                return
            for end in range(start, len(s)):
                if dp[start][end] == True:
                    curr.append(s[start:end+1])
                    backtrack(end+1)
                    curr.pop()


        res = []
        curr = []
        backtrack(0)
        return res