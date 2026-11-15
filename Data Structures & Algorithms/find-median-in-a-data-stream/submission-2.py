class MedianFinder:

    def __init__(self):
        self.smaller_max = [] # smaller half has max heap
        self.larger_min = [] # larger half has min heap
        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.smaller_max or num < -self.smaller_max[0]:
            heapq.heappush(self.smaller_max, -num)
        else:
            heapq.heappush(self.larger_min, num)

        if len(self.smaller_max) - len(self.larger_min) > 1:
            num = -heapq.heappop(self.smaller_max)
            heapq.heappush(self.larger_min, num)
        if len(self.larger_min) - len(self.smaller_max) > 1:
            num = heapq.heappop(self.larger_min)
            heapq.heappush(self.smaller_max, -num)
        
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.smaller_max[0] + self.larger_min[0]) / 2
        if len(self.smaller_max) > len(self.larger_min):
            return -self.smaller_max[0]
        else:
            return self.larger_min[0]
        