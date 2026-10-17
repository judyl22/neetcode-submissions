class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index, total):
            if index >= len(nums):
                return
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            subset.append(nums[index])
            dfs(index, total + nums[index])
            subset.pop()
            dfs(index + 1, total)

        dfs(0, 0)
        return res