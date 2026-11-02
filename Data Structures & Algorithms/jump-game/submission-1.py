class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i, num in enumerate(nums):
            farthest = max(farthest, num + i)
            if num == 0 and i != n - 1:
                if farthest <= i:
                    return False
        return True
        