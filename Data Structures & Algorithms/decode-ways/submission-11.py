class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # one = dp[i], two = dp[i + 1], three = dp[i + 2]
        # we want to set dp[n] to 1, which is dp[i + 1] to 1
        # because we start at i = n - 1 in the for loop
        one, two, three = 0, 1, 0
        for i in range(n - 1, -1, -1):            
            if s[i] == '0':
                one = 0
            elif i + 2 <= n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                one = two + three
            else:
                one = two
            two, three = one, two
        return one