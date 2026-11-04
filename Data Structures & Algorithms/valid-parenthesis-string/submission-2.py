class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                opening.append((c, i))
            elif c == '*':
                stars.append((c, i))
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
            c_open, i_open = opening.pop()
            c_star, i_star = stars.pop()
            if i_open > i_star:
                return False
        return True
