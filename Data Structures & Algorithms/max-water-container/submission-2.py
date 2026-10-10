class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        left = 0
        right = len(heights)-1
        while left < right:
            width = right - left
            high = min(heights[left], heights[right])
            curr = width * high
            if curr > output:
                output = curr
            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return output