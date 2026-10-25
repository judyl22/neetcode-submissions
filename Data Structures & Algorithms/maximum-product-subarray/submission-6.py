class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = res_reverse = 1
        max_prod = max(nums)
        for i in range(n):
            if nums[i] == 0:
                res = res_reverse = 1
            else:
                res = res * nums[i]
                res_reverse = res_reverse * nums[n - 1 - i]
                max_prod = max(max_prod, res, res_reverse)
        return max_prod