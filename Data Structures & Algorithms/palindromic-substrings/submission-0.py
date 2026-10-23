class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0
        n = len(s)

        # even length
        for i in range(n):
            start, end = i, i
            while start >= 0 and end <= n - 1:
                if s[start] == s[end]:
                    tot += 1
                else:
                    break
                start -= 1
                end += 1
        
        # odd length
        for i in range(n - 1):
            start, end = i, i + 1
            while start >= 0 and end <= n - 1:
                if s[start] == s[end]:
                    tot += 1
                else:
                    break
                start -= 1
                end += 1
        
        return tot