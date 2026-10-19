class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        closing = 0
        curr = []
        opening = 0

        def backtrack():
            nonlocal opening
            nonlocal closing
            if opening == n:
                for i in range(closing):
                    curr.append(')')
                curr_copy = ''.join(curr)
                res.append(curr_copy)
                for i in range(closing):
                    curr.pop()
                return
            if closing != 0:
                curr.append(')')
                closing -= 1
                backtrack()
                curr.pop()
                closing += 1
            opening += 1
            closing += 1
            curr.append('(')
            backtrack()
            curr.pop()
            opening -= 1
            closing -= 1
        
        backtrack()
        return res