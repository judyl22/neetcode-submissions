class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            in_degree[crs] += 1
        num_visited = 0
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            crs = queue.popleft()
            num_visited += 1
            for neigh in preMap[crs]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        if queue:
            return False
        if num_visited != numCourses:
            return False
        return True

