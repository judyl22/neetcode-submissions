class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        new_start = newInterval[0]
        new_end = newInterval[1]
        res = []
        temp_start = new_start
        temp_end = new_end
        add = False
        overlap = False
        for start, end in intervals:
            if add:
                res.append([start, end])
            elif overlap:
                if start > new_end:
                    res.append([temp_start, temp_end])
                    res.append([start, end])
                    add = True
                else:
                    temp_end = max(temp_end, end)
            else:
                if end < new_start:
                    res.append([start, end])
                elif start > new_end:
                    res.append([new_start, new_end])
                    res.append([start, end])
                    add = True
                else:
                    temp_start = min(start, new_start)
                    temp_end = max(end, new_end)
                    overlap = True
        if not add:
            res.append([temp_start, temp_end])
        return res