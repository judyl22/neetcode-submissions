class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda pair: pair[0])
        num = 0
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            prev_interval = intervals[i - 1]
            if prev_interval[1] <= interval[0]:
                continue
            else:
                num += 1
                interval[1] = min(interval[1], prev_interval[1])
        return num