class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(index, curr):
            res.append(curr[:])
            for i in range(index, len(nums)):
                if nums[i] == nums[i - 1] and index != i:
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res