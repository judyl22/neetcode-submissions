class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        range_start = range_end = 0
        for i in range(len(nums)):
            curr_num = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                range_start = range_end
            else:
                range_start = 0
            range_end = len(res)
            for j in range(range_start, range_end):
                temp = res[j][:]
                temp.append(curr_num)
                res.append(temp)
        return res