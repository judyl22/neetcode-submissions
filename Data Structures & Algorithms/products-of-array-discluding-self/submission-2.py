class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        has_zero = False
        zero_num = 0
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                zero_num = zero_num + 1
                has_zero = True
        if zero_num > 1:
            return [0] * len(nums)
        output = []
        for num in nums:
            if num == 0:
                output.append(prod)
            elif has_zero:
                output.append(0)
            else:
                output.append(prod // num)
        return output