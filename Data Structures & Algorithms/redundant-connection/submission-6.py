class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = {i : [] for i in range(n)}
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        visited = set()
        cycle = set()
        cycle_start = -1

        def dfs(child, parent):
            nonlocal cycle_start
            if child in visited:
                cycle_start = child
                cycle.add(child)
                return False
            visited.add(child)
            for neigh in graph[child]:
                if neigh == parent:
                    continue
                if not dfs(neigh, child):
                    if child == cycle_start:
                        cycle_start = -1
                    if cycle_start != -1:
                        cycle.add(child)
                    return False
            return True
        
        dfs(1, -1)
        last_edge = []
        for child, parent in edges:
            if child in cycle and parent in cycle:
                last_edge = [child, parent]
        return last_edge