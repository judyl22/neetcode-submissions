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
        if len(nums) == 1 or nums[left] < nums[right]:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[left] < nums[mid]: # the mid is in the left portion
                left = mid + 1
            else: # the mid is in the right portion
                right = mid - 1
