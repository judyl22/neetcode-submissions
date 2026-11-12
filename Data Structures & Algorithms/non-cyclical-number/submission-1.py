class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr_num = 0
        while curr_num != 1:
            curr_num = 0
            while n:
                curr_num += (n % 10) ** 2
                n = n // 10
            if curr_num in seen:
                return False
            seen.add(curr_num)
            n = curr_num
        return True