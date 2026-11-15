class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n <= m:
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1
            temp = n
            n, m = m, n
        count = n + m
        half = count // 2
        left = 0
        right = n - 1
        while True:
            mid = (left + right) // 2
            mid2 = half - (mid + 1) - 1
            
            short_left = float('-inf') if mid < 0 else short[mid]
            short_right = float('inf') if mid + 1 >= n else short[mid + 1]
            long_left = float('-inf') if mid2 < 0 else long[mid2]
            long_right = float('inf') if mid2 + 1 >= m else long[mid2 + 1]
            
            if short_left <= long_right and long_left <= short_right:
                if count % 2 == 0:
                    small = max(short_left, long_left)
                    big = min(short_right, long_right)
                    return (small + big) / 2
                else:
                    return min(short_right, long_right)
            elif short_right < long_left:
                left = mid + 1
            elif long_right < short_left:
                right = mid - 1
        