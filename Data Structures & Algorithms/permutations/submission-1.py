class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        curr = []

        def dfs(pick, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(pick)):
                if pick[i] == False:
                    pick[i] = True
                    curr.append(nums[i])
                    dfs(pick, curr)
                    pick[i] = False
                    curr.pop()
        
        dfs(pick, curr)
        return res