class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.comps = n

    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return
        if self.rank[a_root] < self.rank[b_root]:
            self.par[a_root] = b_root
        elif self.rank[a_root] > self.rank[b_root]:
            self.par[b_root] = a_root
        else:
            self.par[a_root] = b_root
            self.rank[b_root] += 1
        self.comps -= 1

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        return dsu.comps