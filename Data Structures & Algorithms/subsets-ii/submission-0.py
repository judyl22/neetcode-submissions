class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[index])
            backtrack(index + 1, curr)
            curr.pop()

            index += 1
            while index != len(nums) and nums[index] == nums[index - 1]:
                index += 1
            backtrack(index, curr)
        
        backtrack(0, [])
        return res