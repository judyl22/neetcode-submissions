class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []

        def dfs(index, curr_path):
            if index == len(nums):
                path.append(curr_path.copy())
                return
            dfs(index+1, curr_path)
            curr_path.append(nums[index])
            dfs(index+1, curr_path)
            curr_path.pop()

        dfs(0, [])
        return path