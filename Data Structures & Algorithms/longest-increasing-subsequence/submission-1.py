class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length[i] = max(length[i], 1 + length[j])
        return max(length)