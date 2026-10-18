class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []

        def dfs(index, curr, total):
            if total == target:
                path.append(curr.copy())
                return
            if total > target or index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                if  total + candidates[i] > target:
                    break
                if index != i and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                dfs(i + 1, curr, total + candidates[i])
                curr.pop()
        
        dfs(0, [], 0)
        return path
        