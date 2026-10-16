class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = {i : [] for i in range(n+1)}

        def dfs(child, parent):
            if child in visited:
                return False
            visited.add(child)
            for nei in graph[child]:
                if nei == parent:
                    continue
                if not dfs(nei, child):
                    return False
            return True
        
        for child, parent in edges:
            graph[child].append(parent)
            graph[parent].append(child)
            visited = set()
            if dfs(child, parent) == False:
                return [child, parent]