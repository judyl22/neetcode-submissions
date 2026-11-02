"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda i: i.start)
        heap = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            if heap:
                latest_end = heap[0]
                if latest_end <= start:
                    heapq.heapreplace(heap, end)
                    continue
            heapq.heappush(heap, end)
        return len(heap)
        