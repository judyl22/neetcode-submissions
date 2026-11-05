class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}
    
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
        return True     

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                point1 = points[i]
                point2 = points[j]
                dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges.append((dist, i, j))
        tot_dist = 0
        union_find = UnionFind(n)
        edge_num = 0
        edges = sorted(edges, key=lambda x: x[0])
        for dist, point1, point2 in edges:
            if union_find.union(point1, point2) == False:
                continue
            tot_dist += dist
            edge_num += 1
            if edge_num == n - 1:
                break
        return tot_dist

        
        