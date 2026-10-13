class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            visited.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre) == False:
                    return False
            visited.remove(crs)
            pre_map[crs] = []
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
        