class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # init max_area
        # nested for loop:
            # if pos is 1:
                # area = dfs(pos)
                # update max_area
        # return max_area

        # def dfs(pos):
        #   if pos not valid:
        #       return 0
        #   return 1 + dfs of all directions
        max_area = 0
        row_num = len(grid)
        col_num = len(grid[0])

        def dfs(r, c, ):
            nonlocal area
            if min(r, c) < 0 or r == row_num or c == col_num or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # for dr, dc in directions:
            #     area += dfs(r + dr, c + dc)
            # return 1 + area
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1)

        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == 1:
                    area = 0
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area