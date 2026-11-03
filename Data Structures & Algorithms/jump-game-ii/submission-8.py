class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        old_right = 0
        right = nums[0]
        step = 1
        while right < n - 1:
            step += 1
            for i in range(old_right + 1, right + 1):
                old_right = right
                right = max(right, i + nums[i])
        return step
        