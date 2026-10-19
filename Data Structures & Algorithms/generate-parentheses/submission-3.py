class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        res = []
        for left_num in range(n):
            right_num = n - 1 - left_num
            for left_res in self.generateParenthesis(left_num):
                for right_res in self.generateParenthesis(right_num):
                    res.append('(' + left_res + ')' + right_res)
        return res