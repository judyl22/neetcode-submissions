class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        union_find = Union_Find(n)
        for a, b in edges:
            if union_find.union(a, b) == False:
                return False
        if union_find.comps != 1:
            return False
        return True
        
class Union_Find:
    def __init__(self, n):
      self.parents = list(range(n))
      self.comps = n
      self.rank = [1] * n

    def find(self, n):
        # if self.parents[n] == n:
        #     return n
        # while self.parents[n] != n:
        #     self.parents[n] = self.parents[self.parents[n]]
        #     n = self.parents[n]
        # return n
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, a, b):
        if self.find(a) == self.find(b):
            return False
        if self.rank[self.parents[a]] > self.rank[self.parents[b]]:
            self.parents[self.parents[b]] = a
            self.parents[b] = a
        elif self.rank[self.parents[a]] < self.rank[self.parents[b]]:
            self.parents[self.parents[a]] = b
            self.parents[a] = b
        else:
            self.parents[self.parents[b]] = a
            self.parents[b] = a
            self.rank[a] += 1
        self.comps -= 1
        return True