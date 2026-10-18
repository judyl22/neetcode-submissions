class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        occupied = [False] * len(nums)
        curr = {}

        def dfs(index, occupied, curr):
            if index == len(nums):
                permutation = [0] * len(nums)
                for num, new_index in curr.items():
                    permutation[new_index] = num
                res.append(permutation)
                return
            num = nums[index]
            for i in range(len(occupied)):
                if occupied[i] == False:
                    curr[nums[index]] = i
                    occupied[i] = True
                    dfs(index + 1, occupied, curr)
                    curr.pop(nums[index])
                    occupied[i] = False
        
        dfs(0, occupied, curr)
        return res