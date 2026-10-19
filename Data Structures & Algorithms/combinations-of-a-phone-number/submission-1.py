letters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        if digits == '':
            return []
        def backtrack(index):
            if index == len(digits):
                curr_arr = ''.join(curr)
                res.append(curr_arr)
                return
            digit = int(digits[index])
            for c in letters[digit]:
                curr.append(c)
                backtrack(index + 1)
                curr.pop()

        backtrack(0)
        return res