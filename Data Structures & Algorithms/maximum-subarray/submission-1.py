class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # def dfs(i, flag):
        #     if i+1 == len(nums):
        #         return max(0, nums[i]) if flag else nums[i]
        #     elif flag:
        #         return max(0, nums[i] + dfs(i+1, True))
        #     else:
        #         return max(dfs(i+1, False), nums[i] + dfs(i+1, True))
        
        # return dfs(0, False)

        # divide and conquet logic:
        # Does best subarray include m?
        # → use leftSum + nums[m] + rightSum

        # Does it not include m?
        # → then it must be completely in left half or right half
        # → recurse into that side

        def dfs(left, right):
            if left > right:
                return float('-inf')
            middle = (left + right) // 2
            # find left best sum
            left_sum = right_sum = curr_sum = 0
            for i in range(middle - 1, left - 1, -1):
            # we don't want to include middle
                curr_sum = curr_sum + nums[i]
                left_sum = max(left_sum, curr_sum)
            # find right best sum
            curr_sum = 0
            for i in range(middle + 1, right + 1):
                curr_sum = curr_sum + nums[i]
                right_sum = max(right_sum, curr_sum)
            return max(dfs(left, middle - 1),
                        dfs(middle + 1, right),
                        left_sum + nums[middle] + right_sum)

        return dfs(0, len(nums) - 1)

