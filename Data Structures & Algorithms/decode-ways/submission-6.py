class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        nums = [int(dig) for dig in list(s)]
        decode = {i: -1 for i in range(n)}

        def dp(index):
            if index == n:
                return 1
            if decode[index] != -1:
                return decode[index]
            if s[index] == '0':
                decode[index] = 0
                return decode[index]
            if s[index] == '1' and index + 2 <= n:
                decode[index] = dp(index + 1) + dp(index + 2)
                return decode[index]
            if s[index] == '2' and index + 2 <= n and s[index + 1] in '0123456':
                decode[index] = dp(index + 1) + dp(index + 2)
                return decode[index]
            decode[index] = dp(index + 1)
            return decode[index]
        
        return dp(0)

            