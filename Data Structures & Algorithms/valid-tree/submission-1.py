class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        graph = {i: [] for i in range(n)}
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        visited = set()
        def dfs(child, parent):
            if child in visited:
                return False
            visited.add(child)
            if graph[child] == []:
                return True
            for neigh in graph[child]:
                if neigh != parent and dfs(neigh, child) == False:
                    return False
            return True
        
        if dfs(0, -1) == False:
            return False
        if len(visited) != n:
            return False
        return True