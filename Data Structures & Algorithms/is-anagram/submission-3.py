class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_arr = []
        for c in s:
            s_arr.append(c)
        t_arr = []
        for c in t:
            t_arr.append(c)
        s_arr.sort()
        t_arr.sort()
        for i in range(len(s_arr)):
            if s_arr[i] != t_arr[i]:
                return False
        return True