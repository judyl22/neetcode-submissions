class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if sum(subset) > target:
                return
            subset.append(nums[index])
            dfs(index)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res