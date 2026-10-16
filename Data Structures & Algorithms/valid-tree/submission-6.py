class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        graph = {i: [] for i in range(n)}
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        visited = set()
        stack = []
        stack.append((0, -1))
        while stack:
            child, parent = stack.pop()
            if child in visited:
                return False
            visited.add(child)
            for neigh in graph[child]:
                if neigh == parent:
                    continue
                stack.append((neigh, child))
        if len(visited) != n:
            return False
        return True