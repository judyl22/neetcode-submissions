class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # init stack and max area
        # nested for loop
        #   if curr == 1:
        #       stack[]
        #       append curr to stack
        #       init area
        #       while stack:
        #           pos= stack pop
        #           if invalid:
        #               continue
        #           grid r, c = 0
        #           area += 1
        #           directions arr, for direct in directions:
        #               append to stack
        #       update max_area
        #  return max_area
        
        stack = []
        max_area = 0
        row_num = len(grid)
        col_num = len(grid[0])
        for curr_row in range(row_num):
            for curr_col in range(col_num):
                if grid[curr_row][curr_col] == 1:
                    area = 0
                    stack = []
                    stack.append((curr_row, curr_col))
                    while stack:
                        r, c = stack.pop()
                        if min(r, c) < 0 or r == row_num or c == col_num or grid[r][c] == 0:
                           continue
                        area += 1
                        grid[r][c] = 0
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        for dr, dc in directions:
                            stack.append((r + dr, c + dc))
                    max_area = max(max_area, area)
        return max_area 
