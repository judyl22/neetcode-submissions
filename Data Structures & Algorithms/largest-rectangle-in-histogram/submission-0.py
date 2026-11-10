class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        stack.append((0, heights[0]))
        largest = 0
        for i in range(1, n):
            curr_height = heights[i]
            old_index = i
            while stack and curr_height < stack[-1][1]:
                old_index, height = stack.pop()
                width = i - old_index
                area = height * width
                largest = max(largest, area)
            stack.append((old_index, heights[i]))
        while stack:
            index, height = stack.pop()
            width = n - index
            area = height * width
            largest = max(largest, area)
        return largest