class Solution:
    def isPalindrome(self, s: str) -> bool:
        half_len = (len(s) + 1) // 2
        seen = 0
        while s:
            first_let = s[0]
            last_let = s[-1]
            while first_let.isalnum() == False:
                s = s[1:]
                if not s:
                    return True
                first_let = s[0]
            while last_let.isalnum() == False:
                s = s[:-1]
                if not s:
                    return True
                last_let = s[-1]
            print(first_let)
            print(last_let)
            print()
            if first_let.casefold() != last_let.casefold():
                return False
            s = s[1:-1]
        return True
