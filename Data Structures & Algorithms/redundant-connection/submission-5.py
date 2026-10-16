class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        inDegree = [0] * n
        graph = {i : [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            inDegree[node1] += 1
            inDegree[node2] += 1
        
        queue = deque()
        for i in range(n):
            if inDegree[i] == 1:
                queue.append((i, -1))
        while queue:
            child, parent = queue.popleft()
            inDegree[child] -= 1
            for neigh in graph[child]:
                if neigh == parent:
                    continue
                inDegree[neigh] -= 1
                if inDegree[neigh] == 1:
                    queue.append((neigh, child))
        cycle = set()
        for i in range(n):
            if inDegree[i] != 0:
                cycle.add(i)
        last_edge = []
        for a, b in edges:
            if a in cycle and b in cycle:
                last_edge = [a, b]
        return last_edge
