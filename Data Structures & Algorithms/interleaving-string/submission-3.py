class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
             
        s1_index = s2_index = s3_index = 0 
        memo = {}       
        def backtrack(s3_index, s1_index, s2_index):
            if s3_index == len(s3):
                return True
            if (s3_index, s1_index, s2_index) in memo:
                return memo[(s3_index, s1_index, s2_index)]

            c = s3[s3_index]
            if s1_index < len(s1) and c == s1[s1_index]  :
                res = backtrack(s3_index + 1, s1_index + 1, s2_index)
                memo[(s3_index, s1_index, s2_index)] = res
                if res:
                    return True

            if s2_index < len(s2) and c == s2[s2_index]:
                res = backtrack(s3_index + 1, s1_index, s2_index + 1)
                memo[(s3_index, s1_index, s2_index)] = res
                if res:
                    return True

            memo[(s3_index, s1_index, s2_index)] = False   
            return False

        return backtrack(s3_index, s1_index, s2_index)
        