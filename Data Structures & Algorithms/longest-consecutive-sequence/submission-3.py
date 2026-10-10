class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        curr = 1
        last = nums[0]
        for num in nums[1:]:
            if num == last+1:
                curr += 1
                if curr > longest:
                    longest = curr
            elif num != last:
                curr = 1
            last = num
        return longest