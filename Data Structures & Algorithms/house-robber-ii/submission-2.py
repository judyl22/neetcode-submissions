class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_1d(nums):
            if len(nums) == 1:
                return nums[0]
            one = nums[0]
            two = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                new_two = max(nums[i] + one, two)
                one = two
                two = new_two
            return two

        if len(nums) <= 3:
            return max(nums)
        return max(rob_1d(nums[1:]), rob_1d(nums[:-1]))