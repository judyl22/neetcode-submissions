class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist_dict = {i : [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                point1 = points[i]
                point2 = points[j]
                dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                dist_dict[i].append((j, dist))
                dist_dict[j].append((i, dist))
        visited = set()
        min_heap = []
        for point2, dist in dist_dict[0]:
            heapq.heappush(min_heap, (dist, point2))
        visited.add(0)
        tot_dist = 0
        while len(visited) != n:
            dist, point1 = heapq.heappop(min_heap)
            if point1 in visited:
                continue
            tot_dist += dist
            visited.add(point1)
            for point2, new_dist in dist_dict[point1]:
                heapq.heappush(min_heap, (new_dist, point2))
        return tot_dist