class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, visited, height):
            visited.add((r, c))
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if min(new_r, new_c) < 0 or new_r == row_num or new_c == col_num or heights[new_r][new_c] < heights[r][c] or (new_r, new_c) in visited:
                    continue
                dfs(new_r, new_c, visited, heights[new_r][new_c])
        
        row_num = len(heights)
        col_num = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pacific_visited = set()
        atl_visited = set()
        # pacific
        for c in range(col_num):
            dfs(0, c, pacific_visited, heights[0][c])
        for r in range(row_num):
            dfs(r, 0, pacific_visited, heights[r][0])
        for c in range(col_num):
            dfs(row_num - 1, c, atl_visited, heights[row_num - 1][c])
        for r in range(row_num):
            dfs(r, col_num - 1, atl_visited, heights[r][col_num - 1])
        
        both_visited = []
        for r, c in pacific_visited:
            if (r, c) in atl_visited:
                both_visited.append([r, c])
        return both_visited