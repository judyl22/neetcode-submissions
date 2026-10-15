class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        num = 0
        visited = set()
        def dfs(child, parent):
            if child in visited:
                return
            visited.add(child)
            for neigh in graph[child]:
                if neigh == parent:
                    continue
                dfs(neigh, child)

        for child in range(n):
            if child in visited:
                continue
            num += 1
            dfs(child, -1)
        return num