class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        n1 = len(word1)
        n2 = len(word2)
        memo = {}

        def dp(index1, index2):
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            if index2 == n1 and index1 == n2:
                memo[(index1, index2)] = 0
                return 0
            if index2 == n2:
                memo[(index1, index2)] = n1 - index1
                return memo[(index1, index2)]
            if index1 == n1:
                memo[(index1, index2)] = n2 - index2
                return memo[(index1, index2)]
            if word1[index1] == word2[index2]:
                memo[(index1, index2)] = dp(index1 + 1, index2 + 1)
                return memo[(index1, index2)]
            # if not the same, either remove, insert, or replace
            res = min(dp(index1 + 1, index2 + 1), dp(index1 + 1, index2), dp(index1, index2 + 1))
            memo[(index1, index2)] = 1 + res
            return memo[(index1, index2)]
        
        return dp(0, 0)

