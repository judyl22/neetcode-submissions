class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        s_set = set(s)
        longest = 0
        for c in s_set:
            left = 0
            right = 0
            count = 0
            not_match = 0
            while right < len(s):
                count += 1
                if s[right] != c:
                    not_match += 1
                if not_match <= k:
                    if count > longest:
                        longest = count
                else:
                    while left < len(s)-1 and not_match > k:
                        if s[left] != c:
                            not_match -= 1
                        left += 1
                        count -= 1
                right += 1
        return longest
                