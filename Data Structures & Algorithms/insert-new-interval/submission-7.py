class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        res = []
        for i, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            if start > new_end:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif end < new_start:
                res.append(interval)
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
                newInterval = [new_start, new_end]
        res.append(newInterval)
        return res
        