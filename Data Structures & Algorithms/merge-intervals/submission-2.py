class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            events.append([start, 1])
            events.append([end, -1])
        events = sorted(events, key=lambda event: (event[0], -event[1]))
        in_event = 0
        temp_start = 0
        res = []
        for i, event in enumerate(events):
            time, count = event[0], event[1]
            if count == 1:
                if in_event == 0:
                    temp_start = time
                in_event += 1
            else:
                in_event -= 1
                if in_event == 0:
                    res.append([temp_start, time])
        return res