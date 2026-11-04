class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = {i: [] for i in range(1, n + 1)}
        for time in times:
            ui, vi, ti = time
            neighbors[ui].append((vi, ti))
        visited = {}
        heap = [(0, k)]
        longest = 0
        while heap:
            dist, src = heapq.heappop(heap)
            if src in visited:
                continue
            longest = max(longest, dist)
            visited[src] = dist
            for neigh, next_dist in neighbors[src]:
                heapq.heappush(heap, (dist + next_dist, neigh))
        if len(visited) != n:
            return -1
        return longest
        