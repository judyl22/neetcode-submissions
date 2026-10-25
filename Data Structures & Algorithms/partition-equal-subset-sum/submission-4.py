class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        check = {}

        def dp(index, target):
            if target == 0:
                return True
            if index >= len(nums) or target < 0:
                return False
            if (index, target) in check:
                return check[(index, target)]
            if dp(index + 1, target) or dp(index + 1, target - nums[index]):
                check[(index, target)] = True
                return True
            check[(index, target)] = False
            return False
        
        return dp(0, target)