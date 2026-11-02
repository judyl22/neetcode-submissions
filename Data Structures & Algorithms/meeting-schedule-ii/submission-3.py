"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_room = 0
        events = []
        for interval in intervals:
            events.append([interval.start, 1])
            events.append([interval.end, -1])
        events = sorted(events, key=lambda event: (event[0], event[1]))
        room = 0
        for event in events:
            if event[1] == 1:
                room += 1
                max_room = max(max_room, room)
            else:
                room -= 1
        return max_room
        