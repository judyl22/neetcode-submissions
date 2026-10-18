class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index):
            if index == len(nums):
                res.append(nums[:])
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        
        dfs(0)
        return res