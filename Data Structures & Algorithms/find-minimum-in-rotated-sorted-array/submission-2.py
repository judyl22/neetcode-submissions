class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 1, 2] rotated from [1, 2, 3, 4, 5]
        # [3, 4, 5] is the left portion
        # [1, 2] is the right portion
            # if we know we are in the right portion
            # the left pointer will be the smalles
        n = len(nums)
        left = 0
        right = n - 1
        res = float('inf')
        while left <= right:
            res = min(res, nums[left])
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]: # the mid is in the left portion
                left = mid + 1
            else: # the mid is in the right portion
                res = min(res, nums[left])
                right = mid
        return res
