class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n + 1)]
        res[0] = ['']
        res[1] = ['()']
        for i in range(2, n + 1):
            for j in range(i):
                left = res[j]
                right = res[i - 1 - j]
                for one_left in left:
                    for one_right in right:
                        res[i].append('(' + one_left + ')' + one_right)
        return res[n]