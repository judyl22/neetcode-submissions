class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        dp = set([0])
        for num in nums:
            temp_set = set()
            for one_sum in dp:
                if one_sum + num == target:
                    return True
                temp_set.add(one_sum)
                temp_set.add(num + one_sum)
            dp = temp_set
        return False
        