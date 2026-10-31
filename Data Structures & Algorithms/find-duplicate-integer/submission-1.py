class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast pointer both starts at node 0 (index 0)
        # because the arr can only contain number 1 ~ n
        # no number will be 0 -> no node will point to index 0
        # so index 0 will never be a part of the cycle
        slow, fast = 0, 0
        while slow != fast or slow == 0:
        # the pointers are going to be the index in the arr
        # instead of the actual num val
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0 # second slow pointer starts at index 0
        while nums[slow] != nums[slow2]:
            slow = nums[slow]
            slow2 = nums[slow2]
        return nums[slow]
