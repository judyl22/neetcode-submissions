class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        check = {}

        def dp(index):
            if index == n:
                return True
            if index in check:
                return check[index]
            for word in wordDict:
                length = len(word)
                if s[index:index + length] == word and dp(index + length):
                    check[index] = True
                    return check[index]
            check[index] = False
            return False
        
        return dp(0)