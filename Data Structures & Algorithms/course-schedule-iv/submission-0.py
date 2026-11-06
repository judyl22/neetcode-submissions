class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for pre, crs in prerequisites:
            in_degree[crs] += 1
            adj_list[pre].append(crs)
        prereq_map = [set() for _ in range(numCourses)]

        crs_queue = deque()
        for crs in range(numCourses):
            if in_degree[crs] == 0:
                crs_queue.append(crs)
        
        while crs_queue:
            pre = crs_queue.popleft()
            for crs in adj_list[pre]:
                prereq_map[crs].add(pre)
                prereq_map[crs].update(prereq_map[pre])

                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    crs_queue.append(crs)
        
        answer = []
        for pre, crs in queries:
            if pre in prereq_map[crs]:
                answer.append(True)
            else:
                answer.append(False)
        return answer

        
        