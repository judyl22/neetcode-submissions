class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits_copy = []
        carry = 1
        for i in range(n - 1, -1, -1):
            new_digit = digits[i] + carry
            if new_digit >= 10:
                digits_copy.append(new_digit % 10)
                carry = 1
            else:
                digits_copy.append(new_digit)
                carry = 0
        if carry:
            digits_copy.append(1)
        digits_copy.reverse()
        return digits_copy