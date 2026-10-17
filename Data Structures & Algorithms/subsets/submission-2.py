class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = [[]]
        for num in nums:
            for i in range(len(path)):
                one_path = path[i]
                new_one_path = one_path.copy()
                new_one_path.append(num)
                path.append(new_one_path)
        return path