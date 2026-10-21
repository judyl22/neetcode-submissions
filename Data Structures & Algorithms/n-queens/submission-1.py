class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col_set = set()
        row_set = set()
        neg_dia_set = set() # row - col
        pos_dia_set = set() # row + col
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                board_temp = []
                for row_arr in board:
                    board_temp.append(''.join(row_arr))
                res.append(board_temp)
                return
            for col in range(n):
                if col not in col_set and (row - col) not in neg_dia_set and (row + col) not in pos_dia_set:
                    col_set.add(col)
                    neg_dia_set.add(row - col)
                    pos_dia_set.add(row + col)
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    col_set.remove(col)
                    neg_dia_set.remove(row - col)
                    pos_dia_set.remove(row + col)
                    board[row][col] = '.'
        
        backtrack(0)
        return res