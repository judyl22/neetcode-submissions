class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = 1
        seen = set()
        seen.add(s[left])
        longest = 1
        curr_len = 1
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                curr_len = len(seen)
                if curr_len > longest:
                    longest = curr_len
            else:
                while seen and s[right] in seen:
                    seen.remove(s[left])
                    left = left + 1
                seen.add(s[right])
            right += 1
        return longest