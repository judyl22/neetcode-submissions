class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        needs = {}
        output = set()
        for i, num in enumerate(nums):
            needs[i] = -num
        for i, need in needs.items():
            nums_slice = nums[:i] + nums[i+1:]
            left = 0
            right = len(needs) - 2
            while left < right:
                if nums_slice[left]+nums_slice[right] == need:
                    group = sorted([nums_slice[left], -need, nums_slice[right]])
                    output.add(tuple(group))
                    left = left + 1
                elif nums_slice[left]+nums_slice[right] < need:
                    left = left + 1
                else:
                    right = right - 1
        return [list(x) for x in output]