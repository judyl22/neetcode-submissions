class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        n = len(nums)           
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        for i, num in enumerate(nums):
            num = abs(num)
            if num >= 1 and num <= n:
                correct_i = num - 1
                if nums[correct_i] < 0:
                    continue
                nums[correct_i] = -nums[correct_i]
                if nums[correct_i] == 0:
                    nums[correct_i] = float('-inf')
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1
        return n + 1
