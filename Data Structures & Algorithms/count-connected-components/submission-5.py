class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        for parent, child in edges:
            graph[child].append(parent)
            graph[parent].append(child)
        visited = set()
        num = 0

        def bfs(child):
            queue = deque()
            queue.append(child)
            while queue:
                child = queue.popleft()
                visited.add(child)
                for neigh in graph[child]:
                    if neigh not in visited:
                        queue.append(neigh)
        
        for i in range(n):
            if i not in visited:
                bfs(i)
                num += 1
        return num