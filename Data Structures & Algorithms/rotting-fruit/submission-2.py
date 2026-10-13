class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # nested loop
        #       if fruit, both fresh or rotten: num_fruit + 1
        #       if rotten, append to queue, also current day
        # visited set
        # while queue:
        #       queue pop
        #       if not valid or if visited:
        #           continue
        #       append to visit
        #       directions arr
        #       for direction in directions:
        #           append to queue, with day + 1
        # if len(visited) != num fruit: return -1
        # return day

        row_num = len(grid)
        col_num = len(grid[0])
        visited_queue = deque()
        visited_set = set()
        num_fruit = 0
        tot_day = 0
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    num_fruit += 1
                if grid[r][c] == 2:
                    visited_queue.append((r, c, 0))
        while visited_queue:
            r, c, day = visited_queue.popleft()
            if min(r, c) < 0 or r == row_num or c == col_num or grid[r][c] == 0 or (r, c) in visited_set:
                continue
            grid[r][c] = 2
            visited_set.add((r, c))
            tot_day = day
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                visited_queue.append((r + dr, c + dc, day + 1))
        if len(visited_set) != num_fruit:
            return -1
        return tot_day
