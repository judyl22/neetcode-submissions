class DSU:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return True
        if self.rank[roota] < self.rank[rootb]:
            self.par[roota] = rootb
        elif self.rank[roota] > self.rank[rootb]:
            self.par[rootb] = roota
        else:
            self.par[roota] = rootb
            self.rank[rootb] += 1
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for a, b in edges:
            if dsu.union(a, b):
                return [a, b]
        