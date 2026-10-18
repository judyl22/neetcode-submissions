class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        candidates.sort()

        def dfs(index, curr, total):
            if total > target:
                return
            if total == target:
                path.append(curr.copy())
                return
            if index >= len(candidates):
                return
            # if we use the number, we move on to the next
            curr.append(candidates[index])
            dfs(index + 1, curr, total + candidates[index])
            curr.pop()
            # if we decide not to use the number, we will not use any duplicates of this number to cause duplicate path
            add_index = 1
            while (index + add_index < len(candidates) and
                candidates[index] == candidates[index + add_index]):
                add_index += 1 
            dfs(index + add_index, curr, total)
        
        dfs(0, [], 0)
        return path