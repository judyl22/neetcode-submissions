class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        cache = {}
        cache[1] = 1
        cache[2] = 2

        def dp(n, cache):
            if n in cache:
                return cache[n]
            cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
            return cache[n]

        return dp(n, cache)