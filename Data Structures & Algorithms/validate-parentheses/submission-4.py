class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        s = list(s)
        openning = []
        has_open = ['(', '{', '[']
        for i in range(len(s)):
            close = s.pop()
            if close == ']':
                openning.append('[')
            elif close == '}':
                openning.append('{')
            elif close == ')':
                openning.append('(')
            elif close in has_open:
                if not openning or close != openning.pop():
                    return False
        if openning:
            return False
        return True