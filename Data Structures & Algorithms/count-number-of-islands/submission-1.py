class UnionFind:
    def __init__(self, n):
        self.parents = {i : i for i in range(n)}
        self.rank = {i : 1 for i in range(n)}
        self.count = n

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return False
        rank_a = self.rank[parent_a]
        rank_b = self.rank[parent_b]
        if rank_a > rank_b:
            self.parents[parent_b] = parent_a
        elif rank_b > rank_a:
            self.parents[parent_a] = parent_b
        else:
            self.parents[parent_a] = parent_b
            self.rank[parent_b] += 1
        self.count -= 1
        return True
    
    def get_count(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        union_find = UnionFind(row_num * col_num)
        island_num = 0
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] != '1':
                    union_find.count -= 1
                if grid[r][c] == '1':
                    old_pos = r * col_num + c
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if min(new_r, new_c) < 0 or new_r == row_num or new_c == col_num:
                            continue
                        if grid[new_r][new_c] == '1':
                            new_pos = new_r * col_num + new_c
                            union_find.union(old_pos, new_pos)
        return union_find.get_count()

        