class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        col_num = len(matrix[0])
        right = row_num * col_num - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // col_num
            col = mid % col_num
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
