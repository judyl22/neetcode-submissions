class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                opening.append(i)
            elif c == '*':
                stars.append(i)
            else:
                if opening:
                    opening.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        if len(opening) > len(stars):
            return False
        while opening:
            i_open = opening.pop()
            i_star = stars.pop()
            if i_open > i_star:
                return False
        return True
