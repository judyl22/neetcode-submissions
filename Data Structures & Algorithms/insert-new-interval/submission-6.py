class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        res = []
        i = 0
        while i < len(intervals) and new_start > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start, new_end])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res