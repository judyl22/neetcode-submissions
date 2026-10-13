class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # brute force: O((nm)^2)
        row_num = len(heights)
        col_num = len(heights[0])
        pacific_queue = deque()
        for c in range(col_num):
            pacific_queue.append((0, c, heights[0][c]))
        for r in range(row_num):
            pacific_queue.append((r, 0, heights[r][0]))
        pacific_set = set()

        atl_queue = deque()
        for c in range(col_num):
            atl_queue.append((row_num - 1, c, heights[row_num - 1][c]))
        for r in range(row_num):
            atl_queue.append((r, col_num - 1, heights[r][col_num - 1]))
        atl_set = set()

        def bfs(queue, visited):
            while queue:
                r, c, height_diff = queue.popleft()
                if height_diff < 0:
                    continue
                visited.add((r, c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (min(new_r, new_c) < 0 or new_r == row_num or 
                    new_c == col_num or (new_r, new_c) in visited):
                        continue
                    height_diff = heights[new_r][new_c] - heights[r][c]
                    queue.append((new_r, new_c, height_diff))

        bfs(pacific_queue, pacific_set)
        bfs(atl_queue, atl_set)
        both_set = []
        for r, c in pacific_set:
            if (r, c) in atl_set:
                both_set.append([r, c])
        return both_set
        