class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        inDegree = [0] * numCourses
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[pre].append(crs)
            inDegree[crs] += 1
        
        def dfs(crs):
            result.append(crs)
            inDegree[crs] = -1
            for neigh in preMap[crs]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    dfs(neigh)

        for i in range(numCourses):
            if inDegree[i] == 0:
                dfs(i)
        if len(result) != numCourses:
            return []
        return result