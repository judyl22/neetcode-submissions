class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_index = (0, 0)
        max_length = 0

        # even length
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        max_index = (left, right)
                    left -= 1
                    right += 1
                else:
                    break
        
        # odd length
        for i in range(len(s)):
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_length = right - left + 1
                        max_index = (left, right)
                    left -= 1
                    right += 1
                else:
                    break
        
        return s[max_index[0]:max_index[1]+1]