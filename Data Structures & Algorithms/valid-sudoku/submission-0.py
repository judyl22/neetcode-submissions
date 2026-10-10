class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_items = set()
            for item in row:
                if item == '.':
                    continue
                if item in row_items:
                    return False
                else:
                    row_items.add(item)
        for i in range(9):
            col_items = set()
            for j in range(9):
                item = board[j][i]
                if item == '.':
                    continue
                if item in col_items:
                    return False
                else:
                    col_items.add(item)
        for i in range(9):
            block_row = i // 3
            block_col = i % 3
            rows = board[block_row * 3:block_row * 3 + 3]
            items = []
            for row in rows:
                items = items + row[block_col * 3:block_col * 3 + 3]
            item_set = set()
            for item in items:
                if item == '.':
                    continue
                if item in item_set:
                    return False
                else:
                    item_set.add(item)
        return True