class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_highest_arr = [0] * n
        left_highest = 0
        right_highest_arr = [0] * n
        right_highest = 0
        for i in range(n):
            left_highest_arr[i] = left_highest
            right_highest_arr[n - 1 - i] = right_highest
            left_highest = max(left_highest, height[i])
            right_highest = max(right_highest, height[n - 1 - i])
        tot_water = 0
        for i in range(n):
            curr_water = min(left_highest_arr[i], right_highest_arr[i]) - height[i]
            tot_water += max(curr_water, 0)
        return tot_water
