class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one = nums[0]
        two = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = two
            two = max(nums[i] + one, two)
            one = temp
        return two