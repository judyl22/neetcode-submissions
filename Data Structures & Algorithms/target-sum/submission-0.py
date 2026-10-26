class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(index, amount):
            if index == len(nums):
                if amount == target:
                    return 1
                else:
                    return 0
            if (index, amount) in memo:
                return memo[(index, amount)]
            memo[(index, amount)] = backtrack(index + 1, amount + nums[index]) + backtrack(index + 1, amount - nums[index])
            return memo[(index, amount)]
            
        return backtrack(0, 0)