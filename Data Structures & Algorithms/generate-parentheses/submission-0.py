class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for left in range(n):
            left_strings = self.generateParenthesis(left)
            right_strings = self.generateParenthesis(n-1 - left)
            for left_str in left_strings:
                for right_str in right_strings:
                    ans.append("("+left_str+")"+right_str)
        return ans