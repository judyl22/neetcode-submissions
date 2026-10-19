class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        if digits == '':
            return []
        res = []
        for digit in digits:
            num = int(digit)
            if not res:
                for letter in letters[num]:
                    res.append(letter)
            else:
                temp = []
                for letter in letters[num]:
                    for s in res:
                        temp.append(s + letter)
                res = temp
        return res