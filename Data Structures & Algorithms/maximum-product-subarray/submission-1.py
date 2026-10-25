class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1
        max_prod = 1
        res = nums[0]
        for num in nums:
            if num == 0:
                min_prod, max_prod = 1, 1
            temp_min = min_prod
            min_prod = min(num * min_prod, num * max_prod, num)
            max_prod = max(num * max_prod, num * temp_min, num)
            if max_prod > res:
                res = max_prod
        return res