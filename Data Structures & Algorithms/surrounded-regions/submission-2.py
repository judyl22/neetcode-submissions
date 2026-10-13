class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # nested loop to search through the board
        # if there is an O cell not at the edge, immediately to bfs
        # put in queue, create visited-set
        # flag = False
        # while queue:
        #   popleft
        #   if invalid or in visited: continue
        #   if is edge node: flag = True, break
        #   for neigh in neightbors:
        #       append neighbors to queue
        # if flag == false:
        #   turn everything in the visited_set into X
        # continue the nested loop, linear search on board

        def bfs(r, c, visited):
            region_queue = deque()
            region_queue.append((r, c))
            while region_queue:
                r, c = region_queue.popleft()
                if min(r, c) < 0 or r == row_num or c == col_num or (r, c) in visited or board[r][c] == 'X':
                    continue
                if r == 0 or r == row_num - 1 or c == 0 or c == col_num - 1:
                    return True
                visited.add((r, c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    region_queue.append((r + dr, c + dc))
            return False

        row_num = len(board)
        col_num = len(board[0])
        for r in range(1, row_num - 1):
            for c in range(1, col_num - 1):
                if board[r][c] == 'O':
                    visited = set()
                    flag = bfs(r, c, visited)
                    if flag == False:
                        for curr_r, curr_c in visited:
                            board[curr_r][curr_c] = 'X'
        
        
