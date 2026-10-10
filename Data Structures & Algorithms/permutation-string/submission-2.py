class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c_dic = {}
        for c in s1:
            if c not in c_dic:
                c_dic[c] = 1
            else:
                c_dic[c] = c_dic[c] + 1
        c_dic = dict(sorted(c_dic.items()))
        left = 0
        c_dic_copy = {}
        for right in range(len(s2)):
            if s2[right] not in c_dic_copy:
                c_dic_copy[s2[right]] = 1
            else:
                c_dic_copy[s2[right]] += 1
            right += 1
            if right - left > len(s1):
                c_dic_copy[s2[left]] -= 1
                if c_dic_copy[s2[left]] == 0:
                    c_dic_copy.pop(s2[left])
                left += 1
            c_dic_copy = dict(sorted(c_dic_copy.items()))
            if dict(sorted(c_dic_copy.items())) == c_dic:
                return True
        return False