class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_dict = {}
        dist_set = set()
        for point in points:
            x, y = point[0], point[1]
            dist = (abs(x) ** 2 + abs(y) ** 2) ** (1/2)
            if dist in dist_dict:
                dist_dict[dist].append(point)
            else:
                dist_dict[dist] = [point]
            dist_set.add(dist)
        dist_list = list(dist_set)
        heapq.heapify(dist_list)
        res = []
        while k > 0:
            dist = heapq.heappop(dist_list)
            res.extend(dist_dict[dist])
            k -= len(dist_dict[dist])
        return res
        