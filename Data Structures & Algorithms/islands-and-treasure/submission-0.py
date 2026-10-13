class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # nested for loop
        #   if pos == 0:
        #       append queue, also append length as 0
        # while queue:
        #       queue pop
        #       if not valid and not inf:
        #            continue
        #       change length += 1, change grid
        #       directions arr
        #       for direct in directions:
        #           append new pos to queue, and also length
        # return grid

        row_num = len(grid)
        col_num = len(grid[0])
        visited = deque()
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == 0:
                    visited.append((r, c, 0))
        while visited:
            r, c, length = visited.popleft()
            if min(r, c) < 0 or r == row_num or c == col_num:
                continue
            # if grid[r][c] != (2**31-1) and grid[r][c] != 0:
            #     continue
            if grid[r][c] != (2**31-1) and grid[r][c] != 0 or (grid[r][c] == 0 and length != 0):
                continue
            elif grid[r][c] == (2**31-1):
                grid[r][c] = length
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                visited.append((r + dr, c + dc, length + 1))