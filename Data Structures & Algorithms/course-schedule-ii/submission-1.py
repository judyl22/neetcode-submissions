class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        inDegree = [0] * numCourses
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            inDegree[crs] += 1
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.popleft()
            result.append(pre)
            for neigh in preMap[pre]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)
        
        if len(result) != numCourses:
            return []
        return result