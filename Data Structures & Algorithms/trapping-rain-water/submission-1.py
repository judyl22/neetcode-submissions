class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = 0
        right = n - 1
        tot_water = 0
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left <= max_right:
                left += 1
                tot_water += max(max_left - height[left], 0)
                max_left = max(max_left, height[left])
            else:
                right -= 1
                tot_water += max(max_right - height[right], 0)
                max_right = max(max_right, height[right])
        return tot_water
