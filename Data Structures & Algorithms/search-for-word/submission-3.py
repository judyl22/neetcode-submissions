class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(row, col, index):
            if min(row, col) < 0 or row == row_num or col == col_num or  board[row][col] != word[index] or (row, col) in visited:
                return False
            if index == len(word) - 1 and board[row][col] == word[-1]:
                return True
            visited.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                if backtrack(row + dr, col + dc, index + 1):
                    return True
            visited.remove((row, col))
            return False

        row_num = len(board)
        col_num = len(board[0])
        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False