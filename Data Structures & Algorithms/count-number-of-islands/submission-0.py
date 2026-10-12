class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0

        def dfs(grid, r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
                dfs(grid, r+1, c)
                dfs(grid, r-1, c)
                dfs(grid, r, c+1)
                dfs(grid, r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    island += 1
                    dfs(grid, r, c)
        return island