class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        if not nums1:
            nums = nums2
        elif not nums2:
            nums = nums1
        if nums:
            length = len(nums)
            if length == 1:
                return nums[0]
            half = length // 2
            if length % 2 == 0:
                return (nums[half - 1] + nums[half]) / 2
            else:
                return nums[half]
        n = len(nums1)
        m = len(nums2)
        count = n + m
        if count % 2 == 0:
            half = count // 2
        else:
            half = count // 2 + 1
        curr_count = 0
        small = min(nums1[0], nums2[0])
        small_pot1 = 0
        small_pot2 = 0
        while curr_count < half:
            curr_count += 1
            if small_pot1 < n and small_pot2 < m:
                if nums1[small_pot1] <= nums2[small_pot2]:
                    small = nums1[small_pot1]
                    small_pot1 += 1
                else:
                    small = nums2[small_pot2]
                    small_pot2 += 1
            elif small_pot1 < n:
                small = nums1[small_pot1]
                small_pot1 += 1
            elif small_pot2 < m:
                small = nums2[small_pot2]
                small_pot2 += 1
        curr_count = 0
        big = max(nums1[-1], nums2[-1])
        big_pot1 = n - 1
        big_pot2 = m - 1
        while curr_count < half:
            curr_count += 1
            if big_pot1 >= 0 and big_pot2 >= 0:
                if nums1[big_pot1] >= nums2[big_pot2]:
                    big = nums1[big_pot1]
                    big_pot1 -= 1
                else:
                    big = nums2[big_pot2]
                    big_pot2 -= 1
            elif big_pot1 >= 0:
                big = nums1[big_pot1]
                big_pot1 -= 1
            elif big_pot2 >= 0:
                big = nums2[big_pot2]
                big_pot2 -= 1
        return (small + big) / 2