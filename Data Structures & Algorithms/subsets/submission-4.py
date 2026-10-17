class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = [[]]
        for num in nums:
            for i in range(len(path)):
                one_path = path[i]
                path.append(one_path + [num])
        return path