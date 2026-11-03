class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(target)
        m = len(triplets)
        for i in range(m):
            triplets[i].append(0)
        for i in range(n):
            for j in range(m):
                if triplets[j][i] > target[i]:
                    triplets[j][-1] = -1
        for i in range(n):
            found = False
            for j in range(m):
                if triplets[j][-1] == -1:
                    continue
                if triplets[j][i] == target[i]:
                    found = True
            if not found:
                return False
        return True